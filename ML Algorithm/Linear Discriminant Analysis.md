try from one feature, observe how it separate two classes.

try to use two features, and obeserve

try to use three ...



- In this case we are not super insterested in the genes with the most variation.
- Instead, we are interested **maximizing the seperatibility** between the two groups so we can make the best decision.
- (main idea)LDA is like PCA, but it focus on **maximzing the seperatibility among known categories**.



![WeChat2e509fea90049b96991dce7690f2707e.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gqdx3y3g85j31vc18gqv5.jpg)

How to deduce the 2-D graph?

- ignore y axis.
- try to a line to project these points. (**Maximize the seperatibility**!!!! what pca do is to find the max variation)

![WeChat39bc8148b78ad56caebe1131e0193530.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gqdx5ue1zvj31pg14ghdt.jpg)

![WeChat8eed86bbc0adc34a7c472005c0c13244.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gqdx7584byj31do0s4wvw.jpg)

> how LDA creates a new axis

two criteria( considered simultaneously)

1. Maximize the distance between means
2. Minimize the variation (which LDA calls "scatter and is represented by s^2") within each category.

![WeChat945fa03929585560c9d21c3231951c70.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gqdxc6gp51j318w0uwe81.jpg)

we want it to be large!

![WeChat77c241b35795215e87a417ace7c24213.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gqdxfitjssj31v8194npe.jpg)

> 3D project

![WeChat0318de7764c2d5fc710bc416254970cf.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gqdxi3lg6pj31fs1007wh.jpg)

![WeChat8144a33a48a39172a6e3ea4d63537be2.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gqdxin5r84j31d80qk4qp.jpg)

> what if we have 3 categories

1.  The first difference

   -  calculate the mean to all of the  data
   - Then measure the distances between a point that is central in each category and the main central point.

   ![WeChat3553193a8894fbc1294c1aa72a53acb7.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gqdxmrfjh1j31kw0r81kx.jpg)

   

2. The second difference

   - LDA creates 2 axes to separate the data. Because the **3 central points** for each category define **a plane**.

![WeChata6415493f4749122b45f841013883b52.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gqdxqqbzhgj31540ssx38.jpg)



> Similarities between PCA and LDA

-  Both rank the new axes in order of importance
- Both can let you dig in and see which genes are friving the new axes

> In summary

- LDA is like PCA -both try to reduce dimensions
  - PCA looks at the genes with the most variation
  - LDA tries to maximize the separation of known categories

