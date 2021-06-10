from scipy.optimize import minimize

def conjugate_gradient(D, x0, loss_f, grad_f, max_iter=1000):
    """
    conjugate_gradient
    
    Parameters
    ----------
    D: (n,n) array, where is the number of points
        Matrix of distances between points in original space
        
    x0: initial value
    
    loss_f: loss function to calculate error (stress)
    
    grad_f: gradient function for update rule
    
    max_iter: Maximum number of iterations to perform. 
    
    Returns
    -------
    y: optimal solution
        This is the projected embeddings in target space
    """
    def internal_loss_func(x):
        # current value of points
        y = x.reshape(-1,d)
        
        # calculate the stress
        stress = loss_f(D, y)
        return stress

    def internal_gradient_func(x):
        y = x.reshape(-1,d)
        
        # calculate the gradient
        g = grad_f(D, y)
        return g.reshape(-1)
    
    N, d = x0.shape
    
    res = minimize(internal_loss_func, x0, method='CG', 
                   jac=internal_gradient_func, 
                   options={'disp': True, 'maxiter': max_iter})
    y = res.x.reshape(-1,d)
    return y

def gradient_descent(D, x0, loss_f, grad_f, lr, tol, max_iter):
    y_old = x0
    y = x0
    for i in range(max_iter):
        stress = loss_f(D, y)
       
        g = grad_f(D, y)
        
        y = y_old - lr * g
        new_stress = loss_f(D, y)

        stress_var = (stress-new_stress) / stress
        
        if stress_var < tol:
            msg = "iter: {0}, stress: {1:.2e}, stress variance : {2:.2e}".format(i, stress, stress_var)
            print(msg)
            break
            
        if i % 50 == 0:
            msg = "iter: {0}, stress: {1:.2e}, stress variance : {2:.2e}".format(i, stress, stress_var)
            print(msg)
            
        y_old = y

    return y

