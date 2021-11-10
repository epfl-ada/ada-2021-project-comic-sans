class Data:
    
    def _load_data(self, DATAPATH, polynomial, interactions):
        """
        Function responsible for loading the data.
        //Empty for the moment -> Depends on the previous form of the data (df, array, json, ...)
        """   
        
    def __init__(self, DATAPATH=None, polynomial = False, interactions = False, ):
        
        """
        Function initializing the class
        """

        self.data = None
        self.y = None
        self.y_train = None
        self.y_test = None
        self.tX = None
        self.tX_train = None
        self.tX_test = None
        self.ids = None
        self.weights = None
        self.DATAPATH = DATAPATH
        
        if self.DATAPATH:
            self._load_data(self.DATAPATH)
    
    def build_polynomial(self,degree, add_degree_zero=False):
        """
        Creates polynomial feature expansion to the dataset
        """
        x = self.tX
        if add_degree_zero:
            xN = np.hstack([np.ones([x.shape[0],1]),x])
        else:
            xN = x
        if degree>0:
            for i in range(degree-1):
                xN = np.hstack([xN, x**(i+2)])
        self.tX = np.array(xN)
        
    def build_interactions(self):
        """
        Creates feature interactions terms to the dataset
        """
        x = self.tX
        x_out = np.array(x)
        for i in range(int(x.shape[1])):
            x_i = x[:,0]
            x = np.delete(x, 0, 1)
            x_interact = (x_i*x.T).T
            x_out = np.hstack([x_out,x_interact])
        self.tX = x_out
        
    def normalize(self):
        """
        Standardizes data
        """
        mean = np.nanmean(self.tX,axis=0)
        std = np.nanstd(self.tX,axis=0)        
        self.tX = (self.tX-mean)/std
            
    def split_data(self,percent):
        """
        Given a percentage it splits the dataset at that percentage
        """
        rows = len(self.y)
        split_index = int(np.floor(percent / 100 * rows))
        self.tX_train = self.tX[:split_index,:]
        self.tX_test = self.tX[split_index:,:]
        self.y_train = self.y[:split_index]
        self.y_test = self.y[split_index:]
        self.y = None
        self.tX = None
    
    
    def compute_sigmoid(t):
        """
        Computes the output of the sigmoid function for a given input
        """
        t = np.clip(t, -8,8)
        sigmoid_t = 1 / (1 + np.exp(-t))
        return sigmoid_t

    def compute_logistic_loss(w):
        """
        Computes the logistic loss of a model
        """
        predictions = compute_sigmoid(self.tX_train @ w)
        neg_losses_per_datapoint = self.y_train * np.log(predictions) + (1-self.y_train) * np.log(1-predictions)
        loss = - neg_losses_per_datapoint.sum()
        return loss

    def compute_logistic_gradient(w):
        """
        Computes the logistic gradient of a model
        """
        predictions = compute_sigmoid(self.tX_train @ w)
        grad = self.tX_train.T @ (predictions - self.y_train)
        return grad

    
    def logistic_regression(self, initial_w, max_iters, gamma):
        """
        Logistic regression using gradient descent
        """
        w = initial_w

        for iter_ in range(max_iters):

            loss = compute_logistic_loss(w)
            gradient = compute_logistic_gradient(w)
            w -= gamma * gradient

            if iter_ % 250 == 0:
                    print("Current iteration :%d, loss= %.4f" %(iter_, loss)) 
                    
        self.weights = w
        return w
        
    def predict_labels(self):
        """
        Generates class predictions for the test set based on the weights of the log regression
        """
        y_pred = np.dot(self.tX_test, self.weights)
        y_pred[np.where(y_pred <= 0)] = -1
        y_pred[np.where(y_pred > 0)] = 1
        return y_pred
    
    def compute_accuracy(self):
        """
        Estimates the categorical accuracy of the predicted labels for the test set
        """
        y_pred = predict_labels()
        N_tot = y_pred.shape[0]
        N_true = len(np.where(y_pred == self.y_test)[0])
        categorical_acuracy = N_true/N_tot
        return categorical_acuracy
