import numpy as np
import math
from RBM import RBM
import matplotlib.pyplot as plt

class Layer():
    def __init__(self,prev_layer):
        self.ID=None
        self.n = prev_layer.n+1
        self.input_shape = prev_layer.output_shape
        self.output_shape = prev_layer.output_shape
        self.sparse=False
        return
    def forward(self,x):
        return x
    def backward(self,x):
        return x
class InputLayer(Layer):
    def __init__(self,_input_shape):
        self.ID="Input"
        self.n=0
        self.input_shape = _input_shape
        self.output_shape = _input_shape
        return
class Dense(Layer):
    def __init__(self,prev_layer,units):
        super().__init__(prev_layer)
        self.ID="Dense"
        self.output_shape = (self.input_shape[0],units)
        xavier_bound = np.sqrt(6)/(np.sqrt(self.input_shape[1]+units)) # xavier/golrot wieght initialization
        self.w = np.reshape(np.random.uniform(-xavier_bound,xavier_bound,units*self.input_shape[1]),newshape=(self.input_shape[1],units))
        self.b = np.zeros(units)
        self.dw = np.zeros((self.input_shape[1],units))
        self.last_dw=self.dw
        self.db = np.zeros((units)) 
        self.last_db=self.db
    def forward(self,x):
        self.saved_x = x 
        return x@self.w+self.b
    def backward(self,d_out):
        dx = d_out@(self.w.T)
        #self.prev_dw = self.dw
        self.dw = (self.saved_x.T)@d_out
        self.db = np.sum(d_out, axis=0)
        return dx
    def update(self,scaled_dw,scaled_db,momentum):
        new_dw = scaled_dw + momentum*self.last_dw        
        self.w -= new_dw        
        self.last_dw = new_dw
        new_db = scaled_db + momentum*self.last_db
        self.b -= scaled_db
        self.last_db = new_db
class ReLU(Layer): 
    def __init__(self,prev_layer):
        super().__init__(prev_layer)
        self.ID="ReLU"
    def forward(self,x):
        self.saved_x = x
        return np.maximum(x,0)
    def backward(self,d_out):
        return np.where(self.saved_x<0,0,self.saved_x)
class Sigmoid(Layer):   
    def __init__(self,prev_layer):
        super().__init__(prev_layer)
        self.ID="Sigmoid"
    def enable_sparsity(self,beta,p,eps=0.0001,verbose=False): 
        """
        enables KL sparsity in the layer
        beta: weight of sparsity penalty
        p: level of sparsity
        eps: prevents small numbers to appear in denominators
        """  
        self.sparse=True
        self.beta = beta
        self.p = p
        self.s_eps = eps
        #self.v=verbose
        #self.kl_div=0
    def forward(self,x):
        self.saved_x = np.copy(x)
        s = 1.0/(1 + np.exp(-x)) 
        if(self.sparse==True):
            self.saved_mean_activation=np.mean(s,axis=0)
        return s
    def backward(self,d_out):
        s = 1.0/(1 + np.exp(-self.saved_x)) 
        if(self.sparse==False):
            return s*(1-s)
        else:
            s_mean = self.saved_mean_activation 
            sparse_term = self.beta * (((1-self.p)/(1-s_mean+self.s_eps))-(self.p/(s_mean+self.s_eps)))            
            return s*(1-s),sparse_term
class Tanh(Layer):   
    def __init__(self,prev_layer):
        super().__init__(prev_layer)
        self.ID="Tanh"
    def forward(self,x):
        self.saved_x = x
        return np.tanh(x)
    def backward(self,d_out):
        tanh = np.tanh(self.saved_x)
        return (1-(tanh*tanh))
class Linear(Layer): 
    def __init__(self,prev_layer):
        super().__init__(prev_layer)
        self.ID="Linear"
    def forward(self,x):
        self.saved_x = x
        return x
    def backward(self,d_out):
        return np.ones((self.saved_x.shape))
class MSE_loss():
    def loss(self,y_true,y_pred):
        self.diff = (y_pred-y_true)
        return np.mean(self.diff*self.diff,axis=0)
    def loss_prim(self):
        return self.diff

ActivationDict = {"linear":Linear,"relu":ReLU,"sigmoid":Sigmoid,"tanh":Tanh}

class Network():
    def __init__(self,layer_units,activations=["relu"]):
        if not(isinstance(activations, list)):
            activations=[activations]
        if(len(activations) == 1):
            activations=activations*(len(layer_units)-1)
        elif(len(activations) != len(layer_units)-1): raise
        self.arch = layer_units
        self.activation_types = activations    
        self.output_size = layer_units[-1]
        self.batch_size = None # not needed for NN matrix multiplications
        self.input_size = layer_units[0]
        self.loss_fn=MSE_loss()
        self.lr=0.1
        self.lr_decay=0.0
        self.train_err_hist = []
        self.val_err_hist = []
        self.tied_layers=None
        n_layers=len(layer_units)
        self.layers = [InputLayer((self.batch_size,self.input_size))]
        for i in range(n_layers-2):
            self.layers.append(Dense(self.layers[-1],layer_units[i+1]))
            self.layers.append(ActivationDict[activations[i]](self.layers[-1]))
        #final layer
        self.layers.append(Dense(self.layers[-1],layer_units[-1]))
        self.layers.append(ActivationDict[activations[-1]](self.layers[-1]))
        return
    def tie_layer_weights(self,layer_a,layer_b):
        """
        Tie layers with ids layer_a and layer_b.
        Only one pair of layers can be tied per network.
        """
        assert layer_a != layer_b
        assert self.layers[layer_b].w.shape == (self.layers[layer_a].w.T).shape
        self.layers[layer_b].w = self.layers[layer_a].w.T
        self.tied_dw = None
        self.second_tied_layer_scaled_db = None
        #append values so that the first layer is under the 0 index
        self.tied_layers=[min(layer_a,layer_b),max(layer_a,layer_b)]
    def set_loss_fn(self,f):
        self.loss_fn = f
    def set_lr(self,lr,lr_decay=0.0,momentum=0.0,weight_decay=0.0):
        self.lr = lr
        self.lr_decay=lr_decay
        self.momentum = momentum
        self.weight_decay = weight_decay
    def decay_lr(self):
        self.lr *= (1-self.lr_decay)
    def get_layer_output(self,x,n):
        i=0
        for layer in self.layers:
            x = layer.forward(x)
            if(i==n): break
            else:     i+=1
        return x
    def predict(self,x):            
        return self.get_layer_output(x,len(self.layers))
    def evaluate(self,x,y_true,return_mean=False,metric=None):
        y_pred = self.predict(x)
        if(metric==None): l = self.loss_fn.loss(y_true,y_pred)
        else: l = metric(y_true,y_pred)
        if(return_mean==False): return l
        else: return np.mean(l)
    def train_batch(self,x,y_true):
        err = self.evaluate(x,y_true,return_mean=False)
        self.update_layers_SGD(self.lr,x.shape[0])
        return np.mean(err)
    def update_layers_SGD(self,lr,batch_size):
        dCost = self.loss_fn.loss_prim()
        for i in range(len(self.layers)-1,0,-1): #start from the last layer
            layer = self.layers[i]
            if(layer.ID=="Dense"):                
                dCost = layer.backward(dCost)
                scaled_dw = (layer.dw*self.lr/batch_size)
                scaled_db = (layer.db*self.lr/batch_size) 
                if self.tied_layers is None:
                    layer.update(scaled_dw,scaled_db,self.momentum)                
                else: # if there is a pair of tied layers present
                    if(self.tied_layers[1] == i): # comes first
                        self.tied_dw = np.copy(scaled_dw)
                        self.second_tied_layer_scaled_db = scaled_db                        
                    elif(self.tied_layers[0] == i): # comes second
                        layer.update(self.tied_dw.T + scaled_dw,scaled_db,self.momentum)
                        self.layers[self.tied_layers[1]].update(self.tied_dw + scaled_dw.T,self.
                                                    second_tied_layer_scaled_db,
                                                               self.momentum)
                    else:
                        layer.update(scaled_dw,scaled_db,self.momentum)                
            elif(layer.sparse==True and layer.ID=="Sigmoid"):
                mult,sparse_term = layer.backward(None)
                dCost = dCost*mult + np.tile(sparse_term,(dCost.shape[0],1))
            else:
                dCost *= layer.backward(None)
        return dCost    
    def get_summary(self):
         for layer in self.layers: #start from the last layer
            print(str(layer.n)+": "+layer.ID+"\t in:"+str(layer.input_shape)+"\t out:"+str(layer.output_shape))        
    def fit(self,x,y_true,x_val=None,y_true_val=None,batch_size=8,epochs=10,patience=-1):
        def sample(indexes,n_samples):
            if_new_epoch= len(indexes)<=n_samples
            if(if_new_epoch):                
                batch_ind = np.copy(indexes)
                indexes=np.arange(x.shape[0])
                batch_ind_2,indexes,_ = sample(indexes,n_samples-len(batch_ind))
                batch_ind = np.concatenate((batch_ind,batch_ind_2))
            else:
                removed_indices = np.random.choice(len(indexes),n_samples,replace=False)
                batch_ind = np.copy(indexes[removed_indices])
                indexes=np.delete(indexes,removed_indices)
            return batch_ind,indexes,if_new_epoch
        n_samples = x.shape[0]
        indexes = np.arange(n_samples)
        epoch_counter = 0
        batch_counter = 0
        train_err = 0.0
        val_err = 0.0
        best_val_err = 10e9
        current_patience = 0
        while(epoch_counter<epochs):
            batch_ind,indexes,if_new_epoch = sample(indexes,batch_size)
            train_err += self.train_batch(x[batch_ind],y_true[batch_ind])
            batch_counter +=1
            if if_new_epoch==True:
                #print("\r"+str(epoch_counter),end=": ")
                epoch_counter+=1
                #print("Train err: "+str(np.around(train_err*1.0/batch_counter,5)),end="\t")
                if not(x_val is None): # if testing data present
                    val_err = np.mean(self.evaluate(x_val,y_true_val))
                    #print("Val err:"+str(np.around(val_err,5)),end="\t")
                    if(patience>=0):
                        if(val_err<best_val_err):
                            best_val_err=val_err
                            current_patience=0
                        else:
                            current_patience+=1
                        #print("Patience:"+str(current_patience),end="\r", flush=True)
                print("\r"+str(epoch_counter)+":\t train err: "+str(np.around(train_err*1.0/batch_counter,5))
                     +"\t val err: "+str(np.around(val_err,5))+"\t patience: "+str(current_patience),flush=True,end="\t")
                self.train_err_hist.append(train_err*1.0/batch_counter)
                self.val_err_hist.append(val_err)
                train_err=0
                self.decay_lr()
                if(patience>=0 and current_patience==patience):
                    print("\n Patience condition reached,best validation performance: "+str(best_val_err))
                    break                    
                batch_counter = 0
        return
    
# some helper functions
def copy_dense_weights_from_net(l_source,l_target):
    assert l_source.input_shape == l_target.input_shape
    assert l_source.output_shape == l_target.output_shape
    l_target.w = np.copy(l_source.w)
    l_target.b = np.copy(l_source.b)
def copy_dense_weights_from_rbm(rbm_source,l_target,if_encoder):
    if(if_encoder==1):
        l_target.w = np.copy(rbm_source.W)
        l_target.b = np.copy(rbm_source.b)
    else:
        l_target.w = np.copy(rbm_source.W.T)
        l_target.b = np.copy(rbm_source.a)
def pretrain_autoencoder(net,x,x_val,rbm_lr=0.001,rbm_use_gauss_visible=False,
                         rbm_use_gauss_hidden=True, 
                         rbm_mom=0.5,rbm_weight_decay=0.0000,rbm_lr_decay=0.0,
                         rbm_batch_size=100,
                         rbm_epochs=100,rbm_patience=-1,verbose=1):
                final_arch = net.arch[1:math.ceil(len(net.arch)/2.0)] # without input layer
                n_dense_layers = len(final_arch) 
                rbm_list = []    
                #loop for training the RBMs
                for i in range(n_dense_layers):
                    print("\nFine tuning layer number "+str(i))
                    if(i==0): 
                        x_new = x
                        x_val_new = x_val
                    else: 
                        x_new = rbm_list[-1].get_h(x_new)
                        x_val_new = rbm_list[-1].get_h(x_val_new)
                    rbm = RBM(x_new.shape[1],final_arch[i],use_gaussian_visible_sampling=rbm_use_gauss_visible,
                                  use_gaussian_hidden_sampling=rbm_use_gauss_hidden,
                                  use_sample_vis_for_learning=False)
                    rbm.set_lr(rbm_lr,rbm_lr_decay,momentum=rbm_mom,
                               weight_decay=rbm_weight_decay,)
                    rbm.fit(x_new,x_val_new,batch_size=rbm_batch_size,
                            epochs=rbm_epochs, patience=rbm_patience)
                    rbm_list.append(rbm)
                rbm_iterator = 0
                rbm_iterator_direction = 1
                #loop to copy the weights from rbm to NN
                for n_layer in range(len(net.layers)):
                    if(net.layers[n_layer].ID=="Dense"):  
                        copy_dense_weights_from_rbm(rbm_list[rbm_iterator],net.layers[n_layer],rbm_iterator_direction)                            
                        if(rbm_iterator == len(rbm_list)-1 and rbm_iterator_direction==1):rbm_iterator_direction=-1
                        else: rbm_iterator+=rbm_iterator_direction
                print("Pre training finished!")
                return rbm_list
#this function plots the digit reconstructions and the required MSE errors
def plot_results(model,x_test,hidden_units=None):
    if(isinstance(model,Network)):
        reco =model.predict(x_test)
    else:
        reco =model.reconstruct(x_test,force_sample_visible=False)
    perf_array = np.array([np.mean((reco[i]-x_test[i])*(reco[i]-x_test[i])) for i in range(100)])
    mean = np.mean(perf_array)
    fig = plt.figure(figsize=(10,5))
    ax=plt.subplot(121)
    f = ax.imshow(np.reshape(perf_array,newshape=(10,10)))
    f.set_cmap('Reds')
    f.axes.get_xaxis().set_visible(False)
    if hidden_units is None:
        plt.title("MSE: "+str(np.round(mean,4)))
    else:
        plt.title("Units: "+str(hidden_units)+" MSE: "+str(np.round(mean,4)))
    ax = plt.subplot(122)
    digits = np.zeros((10*28,10*28))
    for i in range(100):
        digits[28*(i//10):28*(i//10)+28,28*(i%10):28*(i%10)+28]=np.reshape(reco[i],newshape=(28,28))
    f = ax.imshow(digits)
    f.axes.get_xaxis().set_visible(False)
    f.axes.get_yaxis().set_visible(False)
    plt.show()
    return mean            
