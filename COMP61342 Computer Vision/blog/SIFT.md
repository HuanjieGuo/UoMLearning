Scale-invariant feature transform



# 建立高斯差分金字塔

![WeChat5873be36a2ded238fe9e81cb43fd842b](/Users/guohuanjie/Documents/UoM Learning/COMP61342 Computer Vision/blog/SIFT.assets/WeChat5873be36a2ded238fe9e81cb43fd842b.png)

图一中，最底层的组用某个高斯核进行卷积，它上面的组是下面组的**降采样**(隔点取点，会被模糊)。  每组都是**先用不同高斯核卷积，再降采样**！

图二中， 每层的维度一样，可以进行相减，得到的就是高斯差分金字塔。同层中，高斯模糊的程度不一样！

金字塔被称为尺度空间



> 在几张图片上找极值点？

假如每层有5张图S，那么高斯差分后-1，本层有4张图，找极值点需要求导，上下的不能求导，因此-2。 所以在2张图片n上找极值点。

```java
S = n+3
```



> 不同高斯核卷积目的

模拟近处清晰，远处模糊。(只有高斯核能模拟)



# 极值点的精确定位

key points位置确定。

1. 阈值化

   abs(val) > 0.5*T/n (n是想提取多少张图片特征， T=0.04 论文中)

   绝对值太小可能是噪声

2. 在高斯差分金字塔中找极值

![WeChat287e7874a2e93d85cf6feca35d63a64c](/Users/guohuanjie/Documents/UoM Learning/COMP61342 Computer Vision/blog/SIFT.assets/WeChat287e7874a2e93d85cf6feca35d63a64c.png)



# 为关键点赋予方向

统计以特征点为圆心，以该特征点所在的高斯图像的尺度的1.5倍为半径的圆内的所有的像素的梯度方向及其梯度幅值，并做1.5 sigma的高斯滤波(离圆心近的方向权重贡献更大）。

![WeChat564c24299ba4643785c58044857c4023](/Users/guohuanjie/Documents/UoM Learning/COMP61342 Computer Vision/blog/SIFT.assets/WeChat564c24299ba4643785c58044857c4023.png)

一个特征点，可以有主方向和辅方向(大于主方向80%才能有)



# 构建关键点描述符

![WeChat8edc111ae6b87e0403a263b0a195927e](/Users/guohuanjie/Documents/UoM Learning/COMP61342 Computer Vision/blog/SIFT.assets/WeChat8edc111ae6b87e0403a263b0a195927e.png)

(4*4)(格子) *8(方向) = 128(描述符)

