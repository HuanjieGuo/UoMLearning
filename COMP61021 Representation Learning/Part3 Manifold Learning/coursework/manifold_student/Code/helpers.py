import numpy as np
import matplotlib.pyplot as plt
from matplotlib import offsetbox
from matplotlib.widgets import Button
class VIS(object):
    def __init__(self, data, proj, fig_vis, img_size=(28,28), cmap='gray'):
        super(VIS, self).__init__()
        
        self.data = data.T
        self.proj = proj.T
        self.fig = fig_vis
        self.cmap = cmap
        self.img_show = False
        self.img_size = img_size
        
        self.ax = self.fig.add_subplot()
        self.fig.canvas.mpl_connect('pick_event', self.onpick)
        
        self._refresh_fig()
        
        self.ax_toggle = plt.axes([0.0, 0.9, 0.15, 0.075])
        self.b_toggle = Button(self.ax_toggle, 'Show images')
        self.b_toggle.on_clicked(self.toggle_image)

        self.shown_images = []
        self.img_boxes = []
         
    def onpick(self, event):
        if self.img_show == False:
            # self._refresh_fig()
            
            idx = event.ind[0]
            if idx not in self.shown_images:
                img = self.data[idx].reshape(self.img_size)
                imagebox = offsetbox.AnnotationBbox(
                        offsetbox.OffsetImage(img, cmap=self.cmap),
                                            self.proj[idx])
                self.ax.add_artist(imagebox)
                self.fig.canvas.draw()

                self.shown_images.append(idx)
                self.img_boxes.append(imagebox)
            else:
                elem_idx = self.shown_images.index(idx)
                self.img_boxes[elem_idx].remove()
                self.img_boxes.pop(elem_idx)
                self.shown_images.pop(elem_idx)

                self.fig.canvas.draw()
            
    def _refresh_fig(self):
        self.ax.clear()
        self.ax.set_title('Click a point')
        self.ax.scatter(self.proj[:,0], self.proj[:,1], c='b', picker=True) 
              
    def toggle_image(self, event):
        self.ax.clear()
        if self.img_show == False:
            self._show_image()
            self.img_show = True
        else:
            self._hide_image()
            self.shown_images.clear()
            self.img_show = False
        
    def _hide_image(self):
        self.b_toggle.label.set_text('Show images')
        self._refresh_fig()
            
    def _show_image(self):
        self.b_toggle.label.set_text('Hide images')
        self._plot_components(self.data, self.proj, 
                              images=self.data.reshape((-1, self.img_size[0], self.img_size[1])),
                              thumb_frac=0.05)
        
    def _plot_components(self, data, proj, images=None,
                    thumb_frac=0.05):

        # proj = model.fit_transform(data)
        self.ax.plot(self.proj[:, 0], self.proj[:, 1], '.k')

        if images is not None:
            min_dist_2 = (thumb_frac * max(self.proj.max(0) - self.proj.min(0))) ** 2
            shown_images = np.array([2 * self.proj.max(0)])
            for i in range(self.data.shape[0]):
                dist = np.sum((self.proj[i] - shown_images) ** 2, 1)
                if np.min(dist) < min_dist_2:
                    # don't show points that are too close
                    continue
                shown_images = np.vstack([shown_images, self.proj[i]])
                imagebox = offsetbox.AnnotationBbox(
                    offsetbox.OffsetImage(images[i], cmap=self.cmap),
                                          self.proj[i])
                self.ax.add_artist(imagebox)

from scipy.sparse.csgraph import reconstruct_path
from mpl_toolkits.mplot3d.art3d import Line3DCollection
from matplotlib.collections import LineCollection
import matplotlib.lines as mlines
class VIS_Shortest_path_2d(object):
    def __init__(self, proj, dist, predecessors, fig_vis):
        super(VIS_Shortest_path_2d, self).__init__()

        assert (proj.shape[0] == 2)
        
        self.proj = proj
        self.dist = dist
        self.pres = predecessors
        self.fig = fig_vis
        self.n_dim = self.proj.shape[1]
        
        self.ax = self.fig.add_subplot()
        self.fig.canvas.mpl_connect('pick_event', self.onpick)

        self.picked_idx = []
        self._plot_connectivity(self.proj, self.dist)

        self.sp_lines = None
        self.euclidean_lines = None
        self.path_idx = []
         
    def onpick(self, event):
            
        idx = event.ind[0]
        # print('picked id:', idx)

        n_picked = len(self.picked_idx)
        if n_picked < 1:
         
            if self.sp_lines != None:
                self.sp_lines.remove()
                self.sp_lines = None
                self.euclidean_lines.remove()
                self.euclidean_lines = None

            self.picked_idx.append(idx)

            msg = 'Index of picked points: %d' % (idx)
            self.ax.set_title(msg)
            # props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
            # self.ax.text(0.05, 0.95, msg, transform=self.ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

            self.fig.canvas.draw()

        elif n_picked == 1:
            self.picked_idx.append(idx)
            s_idx = self.picked_idx[0]
            e_idx = self.picked_idx[1]
            self.path_idx = self._get_path(self.pres, s_idx, e_idx)
            
            segments = [[self.proj[:,self.path_idx[i]], self.proj[:,self.path_idx[i+1]]]
                for i in range(len(self.path_idx)-1)]
            self.sp_lines = LineCollection(segments, linewidths=(3),
                    zorder=0, colors='r')
            self.ax.add_collection(self.sp_lines)

            self.euclidean_lines = LineCollection([[self.proj[:,s_idx], self.proj[:,e_idx]]], linewidths=(3), zorder=0, colors='g')
            self.ax.add_collection(self.euclidean_lines)

            msg = 'Index of picked points: %d, %d' % (self.picked_idx[0], self.picked_idx[1])
            self.ax.set_title(msg)
            # props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
            # self.ax.text(0.05, 0.95, msg, transform=self.ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

            self.fig.canvas.draw()

            self.picked_idx.clear()

        print(self.picked_idx)

    def shortest_path_idx(self):
        return self.path_idx

    def _plot_connectivity(self, X, dist):
        segments_idx = self._get_connected_segments(dist)
        segments = [[X[:,i], X[:,j]]
                for i, j in segments_idx]
        lc = LineCollection(segments, linewidths=(0.3),
                    zorder=0, cmap=plt.cm.Blues)
    
        self.ax.scatter(X[0,:], X[1,:], marker='.', c='b', picker=True)
        self.ax.add_collection(lc)

        sp_line = mlines.Line2D([], [], color='red', label='Shortest path')
        euclidean_line = mlines.Line2D([], [], color='green', label='Euclidean path')
        self.ax.legend(handles=[sp_line, euclidean_line], bbox_to_anchor=(0., 0., 1., .102), loc='lower left',
           ncol=2, mode="expand", borderaxespad=0.)
           
        msg = 'Select two points'
        self.ax.set_title(msg)
     
            
    def _get_connected_segments(self, dist):
        segments = []
        n = dist.shape[0]

        for i in range(n):
            for j in range(i,n):
                if dist[i,j] > 0:
                    seg = [min(i,j), max(i,j)]
                    if seg not in segments:
                        segments.append(seg)
        return segments

    def _get_path(self, Pr, i, j):
        path = [j]
        k = j
        while Pr[i, k] != -9999:
            path.append(Pr[i, k])
            k = Pr[i, k]
        return path[::-1]

import math
class ImageViewer(object):
    def __init__(self, data, index, image_size, fig_vis, max_row=5):
        super(ImageViewer, self).__init__()

        self.data = data.T
        self.idx = index
        self.image_size = image_size
        self.fig = fig_vis
        self.max_row = max_row
        self.dummy_img = np.zeros(image_size)

    def show(self):
        n_idx = len(self.idx)
        rows = math.ceil(n_idx / self.max_row)
        cols = self.max_row
        # print(n_idx, rows, cols)

        ax = self.fig.subplots(nrows=rows, ncols=cols, subplot_kw=dict(xticks=[], yticks=[]))
        for i, axi in enumerate(ax.flat):
            # print(i)
            if i > n_idx-1:
                axi.imshow(self.dummy_img, cmap='gray')
            else:
                img = self.data[self.idx[i],:].reshape(self.image_size)
                axi.imshow(img, cmap='gray')
                
class VIS_Bars(object):
    def __init__(self, data, proj, fig_vis, color='r', image_size=(40,40), both=True):
        super(VIS_Bars, self).__init__()

        self.data = data
        self.proj = proj
        self.fig = fig_vis
        self.color = color
        self.img_size = image_size
        self.ax1 = self.fig.add_subplot(121)
        self.ax2 = self.fig.add_subplot(122)
        self.fig.canvas.mpl_connect('pick_event', self._onpick)

        self.both = both
        self._plot_data(self.proj, self.color)

    def _plot_data(self, Y, color):
        if self.both:
            target = np.zeros(1000)
            target[500:] = 1
            self.ax1.scatter(Y[0,:], Y[1,:], c=target, cmap=plt.cm.get_cmap('bwr', 2), picker=True)
        else:
            self.ax1.scatter(Y[0,:], Y[1,:], c=color, picker=True)
        self.ax1.axis('tight')

        img = np.zeros(self.img_size)
        h = self.ax2.imshow(img)

    def _onpick(self, event):
        ind = event.ind[0]
        # print('onpick scatter:', ind, Y[ind])
        img = self.data[:,ind].reshape(self.img_size)
        self.ax2.imshow(img, cmap='gray', interpolation='bilinear')
        self.fig.canvas.draw()
