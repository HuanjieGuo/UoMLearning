> consideration 

- pose
- illumination
  - use normalisation to reduce its impact
- expression
- glass、beard



>  feature extraction

- convolutional kernel
- haar  rectangle

![](http://images2015.cnblogs.com/blog/920180/201603/920180-20160329172709707-1909374643.png)



# Eigenfaces for Recognition(1991)

> PCA等到特征脸的原理

结合自己想想二维空间中点的PCA的处理， 是找一个协方差最小的轴投影， 再取垂直方向再进行投影，第二个可以考虑剔除。 实际上PCA就是重构原点坐标系，重构后原来(x,y)再新坐标系我们用特征值表示。



实际上，特征脸反映了隐含在人脸样本集合内部的信息和人脸的结构关系。将眼睛、面颊、下颌的样本集协方差矩阵的特征向量称为特征眼、特征颌和特征唇，统称特征子脸。特征子脸在特征脸的图像空间中对应生成子空间，称为子脸空间。



在eigenface中，我们重构了坐标系，每一个坐标系的维度eigenvector，就是一张eigenface! 需要多少张eigenface，实际上就是保留前几个保留度最大的eigenvector.



> Drawback of PCA

what PCA does is maximizing the scatter.

However, it is **not only maximizing the scatter between classes, but also within the classes**!  We don't want it  !!!!



> How to improve the eigenface with illumination from different direction?

remove the first three component and use those begining from 4.

# Eigenfaces vs. Fisherfaces(1997)

Fisherfaces use FDA

Maximize the between-class scatter and reduce the within-class scatter

> why choose fisherface ?

fisherface performs better when there are illustration from different direction， which PCA doesn't.



