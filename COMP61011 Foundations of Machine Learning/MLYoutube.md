### 1. Cross Validation

Cross Validation allows us to compare different machine learning methods and get a sense of how well they will work in practice.

before: seperate data into 75% and 25%, use 75% to train and 25% to test

more scientific: split into 4 parts, each part is 25%, then train and test for 4 times, get the averaged number.

**N-Fold cross validation!**



### 2. Bias and Variance

![Screenshot 2020-11-11 at 16.55.54](/Users/guohuanjie/Documents/UoM Learning/COMP61011 Foundations of Machine Learning/image/Screenshot 2020-11-11 at 16.55.54.png)



The inability for a ML method to capture the true relationship is called **bias**

In ML, the difference in fits between data sets is called **Variance**

The line fits the training set very well, but not the testing set, we say that the line is **overfit**.

A good model have low bias in training process and low variance in testing process.



### 3.ROC and AUC

### ![Screenshot 2020-11-11 at 17.22.48](/Users/guohuanjie/Documents/UoM Learning/COMP61011 Foundations of Machine Learning/image/Screenshot 2020-11-11 at 17.28.22.png)

判断为+的个数，在所有+中占比， 命中率

True Positive Rate = Sensitivity = True Positives/(True Positives + False Negative)

判断为+中，误判成-的占比，错误率

Specificity =  True Negatives/(True Negatives+False Positives)

False Positive Rate = 1 - Specificity



Precision = True Positives/(True Positions + False Positives)

注意和False Positive Rate 区别

ROC graph

![Screenshot 2020-11-11 at 17.31.32](/Users/guohuanjie/Documents/UoM Learning/COMP61011 Foundations of Machine Learning/image/Screenshot 2020-11-11 at 17.31.32.png)

ROC graph summarizes all of the confusion matrices that each threshold produced.



AUC( Area Under the Curve) ![Screenshot 2020-11-11 at 17.34.17](/Users/guohuanjie/Documents/UoM Learning/COMP61011 Foundations of Machine Learning/image/Screenshot 2020-11-11 at 17.34.17.png)

The AUC makes it easy to compare ROC curve to another. The red curve is better! 



### 4.Logistic Regression

![Screenshot 2020-11-11 at 18.44.38](/Users/guohuanjie/Documents/UoM Learning/COMP61011 Foundations of Machine Learning/image/Screenshot 2020-11-11 at 18.44.38.png)



### 5.K-means clustering

1. select the number of clusters you want to identify in your data
2. randomly select k distinct data points
3. Measure the distance between the 1st point and the k initial clusters.
4. assign the 1st point to the nearest clustter.
5. when the datas all be assigned to different clusters, calculate the mean of each cluster.
6. repeat from 1 using the mean

Q. How do you figure out what value to use for K?

One way to decide is to just try different values for K.

calculate which k make the total variation within each cluster less.

![Screenshot 2020-11-12 at 11.17.47](/Users/guohuanjie/Documents/UoM Learning/COMP61011 Foundations of Machine Learning/image/Screenshot 2020-11-12 at 11.17.47.png)

### 6. K-nearest neighors

1. strat with a data set with known categories
2. add a new cell with unknown category, to the PCA plot
3. we classify the new cell by looking at the nearest annotated cells.

choose odd number to be K

![Screenshot 2020-11-12 at 18.40.51](/Users/guohuanjie/Documents/UoM Learning/COMP61011 Foundations of Machine Learning/image/Screenshot 2020-11-12 at 18.40.51.png)

when K = 1, training error is 0. (Only blue point in blue area)

![Screenshot 2020-11-12 at 22.58.18](/Users/guohuanjie/Documents/UoM Learning/COMP61011 Foundations of Machine Learning/image/Screenshot 2020-11-12 at 22.58.18.png)



now, the error is not 0!

![image-20201112230334713](/Users/guohuanjie/Library/Application Support/typora-user-images/image-20201112230334713.png)



