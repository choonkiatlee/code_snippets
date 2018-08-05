from sklearn.ensemble import RandomForestRegressor
import sklearn
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



def get_regression_scores(model,x_test,y_test):
    '''
    Takes in x_test and y_test and produces precision / recall scores for the random forest
    
    Parameters:
    -----------
    x_test, y_test -- numpy arrays
    
    Returns: 
    --------
    accuracy -- int
    '''

    return sklearn.metrics.r2_score(y_test, model.predict(x_test))

def generate_regression_feature_scores(model, x_test, y_test, ordered_feature_names,base_accuracy, as_percentage=False):
    scores = []
    
    for i in range(10):
        for i in range(x_test.shape[1]):
            x_t = x_test.copy()
            np.random.shuffle(x_t[:,i])
            shuff_acc = get_regression_scores(model, x_t,y_test)
            
            accuracy_score = base_accuracy - shuff_acc
            
            if as_percentage:
                accuracy_score = accuracy_score / base_accuracy
            
            
            scores.append({'feature':ordered_feature_names[i],'accuracy':accuracy_score})
    df = pd.DataFrame(scores)
    return df 

def remove_features(x_train, x_val, x_test, features, ordered_feature_names):
    """
    Removes features from test data. Useful for removing things that could be biased in our collection method,
    e.g. Login_Number

    :param x_train: training data with features x sessions, as provided by split_train_test or fetch_data
    :param x_test: same for test data
    :param features: list of feature names to delete
    :param ordered_feature_names: list of feature names included in x_train and x_test
    :return: revised x_train, x_test and ordered_feature_names without the deleted features
    """
    indices = np.where(np.isin(ordered_feature_names,unwanted_features))
    #print(indices)
    if len(indices) is not 0:
        x_train = np.delete(x_train, indices, axis=1)
        x_test = np.delete(x_test, indices, axis=1)
        x_val = np.delete(x_val,indices,axis=1)
        ordered_feature_names = np.delete(ordered_feature_names, indices, axis=None)
    return x_train,x_val, x_test, ordered_feature_names

################## Generate Dataset #######################################
np.random.seed(0)

no_features = 50
no_correlated_features = 10
no_useful_features = 2

size = 700

mean = 0
variance = np.random.rand()+2

X = np.zeros((size,no_features))

# Set actual variables to be uniformly sampled
X[:,:no_useful_features] = np.random.uniform(0, variance, (size, no_useful_features))

# Set noise variables to be gaussian 
X[:,no_useful_features:] = np.random.normal(mean,variance,(size,no_features-no_useful_features))

print("MEAN: {0}, VARIANCEC: {1}".format(mean,variance))


# Add random uniform noise
#X += np.random.uniform(0,1,(size, no_features))
 
#"Friedamn #1” regression problem
#Y = (10 * np.sin(np.pi*X[:,0]*X[:,1]) + 20*(X[:,2] - .5)**2 +
#     10*X[:,3] + 5*X[:,4] + np.random.normal(0,1))

Y = 10*(X[:,3] + 1.75*X[:,4] + 2* X[:,0] + 1.5*X[:,1] + 1.25*X[:,2])**2 + np.random.normal(0,variance)

#Add 3 additional correlated variables (correlated with X1-X3)
X[:,10:(10+no_correlated_features)] = X[:,:no_correlated_features] + np.random.normal(0, .025, (size,no_correlated_features))
 
names = ["x%s" % i for i in range(1,no_features+1)]

################### Visualise Dataset ######################################

def plot_dataset():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    print()
    
    ax.scatter(X[:,0],X[:,1],Y)
    #ax.scatter(X[:,1],X[:,3],Y)
    
    #ax2 = fig.add_subplot(212,projection='3d')
    #ax2.scatter(X[:,2],X[:,3],Y)
    
#plot_dataset()



################ Generate train / val / test split #########################
#x_train,x_val,x_test = X[:400],X[400:600],X[600:750]
#y_train,y_val,y_test = Y[:400],Y[400:600],Y[600:750]

import math
train_idx = math.floor(size * 0.6)
val_idx = math.floor(size*0.8)
test_idx = math.floor(size*1.0)

x_train,x_val,x_test = X[:train_idx],X[train_idx:val_idx],X[val_idx:test_idx]
y_train,y_val,y_test = Y[:train_idx],Y[train_idx:val_idx],Y[val_idx:test_idx]



############### Feature Selection #########################################
rf = RandomForestRegressor(n_estimators=500)
print(rf.fit(x_train,y_train))

#print(y_test)
forest_test_pred = rf.predict(x_val)  
#print(forest_test_pred)

base_accuracy_score = get_regression_scores(rf,x_val,y_val)
print("Base Model: Accuracy {0}".format(base_accuracy_score))

important_features = pd.Series(data=rf.feature_importances_,index=names)
important_features.sort_values(ascending=False,inplace=True)

df = generate_regression_feature_scores(rf, x_test, y_test, names, base_accuracy_score, as_percentage = False)
#df = df.groupby('feature').mean().sort_values(by='accuracy',ascending=False)

#df.plot()

print("Starting feature removal")

df = df.groupby('feature').mean().sort_values(by='accuracy',ascending=True)
# Select top 5 unwanted features according to different metrics
top_5_unwanted_features = df.loc[df['accuracy'] < 0.01].head(5)
top_5_unwanted_features = df.accuracy.loc[df.accuracy < (df.max().accuracy - 5*df.std().accuracy)].head(5)
top_5_unwanted_features = df.loc[df.accuracy < df.accuracy.max() * 0.25].head(5)  # remove below 10% of max

############## Remove Unwanted Features 5 at a time ###################################

test_scores = []
validation_scores = []

while len(top_5_unwanted_features) > 0:
    
    unwanted_features = np.array(top_5_unwanted_features.index.values).astype(str)
    x_train,x_val,x_test,names = remove_features(x_train, x_val, x_test, unwanted_features, names)
    
    #print(names)
    #print(unwanted_features)
        
    rf = RandomForestRegressor(n_estimators=300)
    rf.fit(x_train,y_train)
    
    base_accuracy_score = get_regression_scores(rf,x_test,y_test)
    test_scores.append(base_accuracy_score)
    print("Base Model on Test Set: Accuracy {0}".format(base_accuracy_score))
    
    base_accuracy_score = get_regression_scores(rf,x_val,y_val)
    validation_scores.append(base_accuracy_score)
    print("Base Model on Validation Set: Accuracy {0}".format(base_accuracy_score))
    
    print("Completed 1 round of feature removal! Removed: \n{0}".format(top_5_unwanted_features.to_string() ))
    
    df = generate_regression_feature_scores(rf, x_test, y_test, names, base_accuracy_score, as_percentage = True)
    df = df.groupby('feature').mean().sort_values(by='accuracy',ascending=True)
    
    # Select top 5 unwanted features according to different metrics
    top_5_unwanted_features = df.loc[df['accuracy'] < 0.01].head(5)
    top_5_unwanted_features = df.accuracy.loc[df.accuracy < (df.max().accuracy - 5*df.std().accuracy)].head(5)
    top_5_unwanted_features = df.loc[df.accuracy < df.accuracy.max() * 0.25].head(5)  # remove below 10% of max
    
    print("{0} features left!".format(len(df.index.drop_duplicates())))
    
plt.plot(test_scores,label='test_scores')
plt.plot(validation_scores,label='validation_scores')
plt.legend()

'''
print ('---------------------------------------------------')
print(important_features.head(10))
    
print('---------------------------------------------------')

print(df.sort_values(by='accuracy',ascending=False).head(10))
'''