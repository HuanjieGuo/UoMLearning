![](/Users/guohuanjie/Documents/UoM Learning/COMP61342 Computer Vision/blog/Harris Corner Detection.assets/WeChatd1073923cb9b37db7b07eac8642f0b3b.png)

窗口在角点附近各个方向**梯度值变化明显**

**高斯核**在此起到平滑过渡！考虑了邻域对变化影响的贡献。 **中心点的影响比边缘点影响更大**。 W在此意义不是很大

前后窗口固定点位相减去，所有的差值做一个sum。反应了窗口移动后，图片亮度的变化情况。我们要找E(u,v)大的！这就是角点。



> 泰勒展开

f(x+u, y+v) ～= f(x,y) + u* fx(x,y) + v* fy(x,y)  (约等于)



![WeChatbc184abb0be4c2a03a0900e6d434c4d4](/Users/guohuanjie/Documents/UoM Learning/COMP61342 Computer Vision/blog/Harris Corner Detection.assets/WeChatbc184abb0be4c2a03a0900e6d434c4d4.png)



在 u v取任意值的时候，我们要让E(u,v)尽量的大！

![WeChatfbdf38ec67655ea9864ca84d25ea8359](/Users/guohuanjie/Documents/UoM Learning/COMP61342 Computer Vision/blog/Harris Corner Detection.assets/WeChatfbdf38ec67655ea9864ca84d25ea8359.png)

这里其实是关于u,v的二次曲线，u和v同时是变量！ 实际上类似于一个椭圆。 这里，M是一个实数！同时 M是一个实对称矩阵，IxIy = IxIy. 实对称矩阵可以正交相似对角化。

![WeChatd5b7de34f33425b4e8f1b7af0b968b17](/Users/guohuanjie/Documents/UoM Learning/COMP61342 Computer Vision/blog/Harris Corner Detection.assets/WeChatd5b7de34f33425b4e8f1b7af0b968b17.png)

最后，我们化解出来椭圆的标准方程。

我们要E(u,v)任何情况最大，lamda1和lamda2要尽可能大，而且要**同时大**。

- 只有一个lamda大 (Edge)
- 两个lamda都很小(flat)
- 两个lamda都很大，并且近似(corner)

图中 lamda^-(1/2) 是因为 1/lamda位置其实是a^2,所以开了根后，得到了lamda^-(1/2)

![WeChatafec3ff764a1f64326251d64c168866b](/Users/guohuanjie/Documents/UoM Learning/COMP61342 Computer Vision/blog/Harris Corner Detection.assets/WeChatafec3ff764a1f64326251d64c168866b.png)



det M = lamda1*lamda2

trace M = lamda1 + lamda2

R = det M - k(trace M)^2   (k自取)  R作为每个像素点的得分

本处衡量标准不是必须，只是为了方便计算

