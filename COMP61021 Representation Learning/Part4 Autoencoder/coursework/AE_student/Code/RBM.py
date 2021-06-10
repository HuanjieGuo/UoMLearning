import numpy as np

class RBM(object):
    """
    Restricted Boltzmann Machine (RBM) implemented according to 
    http://www.cs.toronto.edu/~hinton/absps/guideTR.pdf . All the references are linked to
    this file.
    
    Parameters
    ----------
    n_hid : int, optional
        Number of binary hidden units
    lr : float, optional
        Learning rate to use during learning. It is recommended to use 100 times smaller
        lr when using gaussian sampling
    use_gaussian_visible_sampling: bool, optional
        Use gaussian sampling to reconstruct real-valued visible units. See sec. 13.2.
        Data has to be normalized with 0 mean and 1 variance.
    use_vis_prob_for_learning: bool, optional
        Use probabilities instead of binary values of hidden units for calculating the
        positive term of l. See sec 3.3 and 3.2.

    """
    def __init__(self, n_vis,n_hid=1024, 
                 use_gaussian_visible_sampling=False,
                 use_gaussian_hidden_sampling=False,
                 use_sample_vis_for_learning=False):
        self.n_hid = n_hid
        self.n_vis = n_vis
        self.W = None
        self.a = None
        self.b = None
        self.dW = np.zeros((self.n_vis,self.n_hid)) # W increment for momentum porposes
        self.da = np.zeros((self.n_vis))# a increment for momentum porposes
        self.db = np.zeros((self.n_hid))# b increment for momentum porposes
        self.use_gaussian_visible_sampling=use_gaussian_visible_sampling
        self.use_gaussian_hidden_sampling=use_gaussian_hidden_sampling
        self.use_sample_vis_for_learning = use_sample_vis_for_learning
        self.init_weights()
    def _sigmoid(self, x):
        return 1. / (1. + np.exp(-np.maximum(np.minimum(x, 30), -30)))
    def init_weights(self,W_var=0.01,bias_value=0.0,seed=0):
        np.random.seed(seed)
        self.W = np.random.normal(0,W_var,size=(self.n_vis,self.n_hid))
        self.W = np.reshape(self.W,newshape=(self.n_vis,self.n_hid))
        self.a = np.ones((self.n_vis))*bias_value
        self.b = np.ones((self.n_hid))*bias_value
    def set_lr(self,lr,lr_decay=0.0,momentum=0.0,weight_decay=0.0):
        self.lr = lr
        self.lr_decay=lr_decay
        self.mom = momentum
        self.weight_decay = weight_decay
    def reconstruct(self, v,force_sample_visible=True,return_h=False):
        """        
        Parameters
        ----------
        v: array-like, shape (n_samples, n_visibles)
            visible units
        resample_visible: optional, bool
            whether to force sample the visible units after reconstruction, 
            no matter if use_binary_visible_sampling=False 

        Returns
        -------
        v_reco: array-like, shape (n_samples, n_hiddens)
            Reconstructed v (one Gibbs sampling step).
        """
        h = self.sample_h(self.get_h(v))
        if(force_sample_visible==True):
            v_reco = self.sample_v(self.get_v(h))
        else:
            v_reco = self.get_v(h)
        if(return_h==True):
            return v_reco,h
        else:
            return v_reco
    
    def get_h(self, v):
        if(self.use_gaussian_hidden_sampling==True):
            return (v @ self.W) + self.b #gaussian sampling can have values greater than 1
        else:
            return self._sigmoid((v @ self.W) + self.b)
    
    def sample_h(self, h):
        if(self.use_gaussian_hidden_sampling==True):
            return np.random.normal(h,1.0)
        else:
            return np.random.binomial(1, h)
    def get_v(self, h):
        if(self.use_gaussian_visible_sampling==True):
            return (h @ self.W.T) + self.a #gaussian sampling can have values greater than 1
        else:
            return self._sigmoid((h @ self.W.T) + self.a)
    def sample_v(self, v):
        if(self.use_gaussian_visible_sampling==True):
            return np.random.normal(v,1.0)
        else:
            return np.random.binomial(1,v)
    def _fit(self, v):
        """
        Adjust the parameters using Contrastive Divergence 1(CD1.
        
        Parameters
        ----------
        v: array-like, shape (n_samples, n_visibles)

        Returns
        -------
        MSE error

        """
        
        h_data = self.get_h(v)
        h_data_sampled = self.sample_h(h_data)
        
        v_new = self.get_v(h_data_sampled)
        if(self.use_sample_vis_for_learning==True):
            v_reco = self.sample_v(v_new)
        else:
            v_reco = v_new
                
        h_reco = self.get_h(v_reco)
        
        v_pos = v
        h_pos = h_data        
        v_neg = v_reco        
        h_neg = h_reco
       
        self.dW = self.mom*self.dW + self.lr * ((v_pos.T @ h_pos)-(v_neg.T @ h_neg)) / v.shape[0] - self.weight_decay * self.W
        self.db = self.mom*self.db + self.lr * np.mean(h_pos-h_neg,axis=0)
        self.da = self.mom*self.da + self.lr * np.mean(v_pos-v_neg,axis=0)
        
        self.W += self.dW
        self.b += self.db
        self.a += self.da
        
        return self.get_err(v,v_reco) 
    def get_err(self,true,pred):
        diff = true-pred
        return np.mean(diff*diff) 
    def fit(self, x, x_val,batch_size=10, epochs=10,patience=-1):
            #lr_decay=0.1, 
            #momentum = 0.0,weight_decay=0.0, verbose=False, patience=-1):
        """
        Fit the model to the data X.
        
        Parameters
        ----------
        x array-like, shape (n_samples, n_features)
            Training data, where n_samples in the number of samples
            and n_features is the number of features.
        """
        
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
        if self.W is None:
            self.init_weights()
        #self.lr = lr
        #self.mom = momentum
        #self.weight_decay = weight_decay
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
            batch_train_err = self._fit(x[batch_ind])
            train_err += batch_train_err

            batch_counter +=1
            if if_new_epoch==True:
                #print("\r"+str(epoch_counter),end=": ")
                epoch_counter+=1
                #print("Train err: "+str(np.around(train_err*1.0/batch_counter,5)),end="\t")
                if not(x_val is None):
                    x_val_reco = self.reconstruct(x_val,force_sample_visible=self.use_sample_vis_for_learning)
                    val_err = self.get_err(x_val,x_val_reco)
                    #print("Val err:"+str(np.around(val_err,5)),end="\t")
                    if(patience>=0):
                        if(val_err<best_val_err):
                            best_val_err=val_err
                            current_patience=0
                        else:
                            current_patience+=1
                        #print("Patience:"+str(current_patience),end="\r",flush=True)
                self.lr = self.lr*(1-self.lr_decay)
                print("\r"+str(epoch_counter)+":\t train err: "+str(np.around(train_err*1.0/batch_counter,5))
                     +"\t val err: "+str(np.around(val_err,5))+"\t patience: "+str(current_patience),flush=True,end="\t")
                train_err=0
                if(patience>=0 and current_patience==patience):
                    print("\n Patience condition reached,best validation performance: "+str(best_val_err))
                    break                    
                batch_counter = 0
        return
