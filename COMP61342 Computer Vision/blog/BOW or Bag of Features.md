

- Interest Point Detector

  SIFT或者Harris是特征点的查找方法

- Interest Point Descriptor

- K-means clustering

- SVM

![WeChat866ce74476ddff5824642d84e2e25db0](/Users/guohuanjie/Documents/UoM Learning/COMP61342 Computer Vision/blog/BOW or Bag of Features.assets/WeChat866ce74476ddff5824642d84e2e25db0.png)

![WeChat07c7d1b5fa37500d89f0c55c6ef29aac](/Users/guohuanjie/Documents/UoM Learning/COMP61342 Computer Vision/blog/BOW or Bag of Features.assets/WeChat07c7d1b5fa37500d89f0c55c6ef29aac.png)

> what is the words in the pics?

用harris corner detection或者SIFT去检测图像中的特征点，我们会获得很多的patch。

![WeChatc35ed01fa072b2aa9ec6f24933b72e3d](/Users/guohuanjie/Documents/UoM Learning/COMP61342 Computer Vision/blog/BOW or Bag of Features.assets/WeChatc35ed01fa072b2aa9ec6f24933b72e3d.png)

得到patch后，进过descriptor处理后，patch被转成向量。  这时候用聚类方法，得到多个类，每个类的中心点，被称为一个word!

![WeChat39f4c679e2492087cdde4cac5dbf9d68](/Users/guohuanjie/Documents/UoM Learning/COMP61342 Computer Vision/blog/BOW or Bag of Features.assets/WeChat39f4c679e2492087cdde4cac5dbf9d68.png)

综上所述，图片先用Harris或者SIFT提取interest of point后， 用聚类算法规划成多个cluster， 多个patch共用一个word! 最后，用直方图统计一张图片的word出现次数。再用KNN进行分类，得到图片的类别。



![WeChat3b916a5241fbe7f5d8e252841c8478dc](/Users/guohuanjie/Documents/UoM Learning/COMP61342 Computer Vision/blog/BOW or Bag of Features.assets/WeChat3b916a5241fbe7f5d8e252841c8478dc.png)

![WeChat3fed2900103c58e6443e3d861f3364fc](/Users/guohuanjie/Documents/UoM Learning/COMP61342 Computer Vision/blog/BOW or Bag of Features.assets/WeChat3fed2900103c58e6443e3d861f3364fc.png)



> bow

- **orderless** document representation



## Step 1: feature extraction

- Detect Interest Points
  - SIFT
  - Harris
  - Dense( take every nth pixel as interest point)
- Computer Descriptor arount each interest point
  - SIFT
  - HOG (https://zhuanlan.zhihu.com/p/40960756)



![WeChatbb6d948f4cd14df85fb5b53c5cea00de](/Users/guohuanjie/Documents/UoM Learning/COMP61342 Computer Vision/blog/BOW or Bag of Features.assets/WeChatbb6d948f4cd14df85fb5b53c5cea00de.png)

## Step 2: Quantization

![WeChat476e557282d880a1d1d61e380be92b19](/Users/guohuanjie/Documents/UoM Learning/COMP61342 Computer Vision/blog/BOW or Bag of Features.assets/WeChat476e557282d880a1d1d61e380be92b19.png)

对point of interests进行聚类后， 选取各个类的聚类中心作为word, 组成visual vocabulary。

-  Cluster descriptors
  - K-means (随机选择N个点开始聚类)
- Assign each visual word to a cluster
- Build frequency histogram

![WeChat893bc7cf4830aad284f7506a3075c163](/Users/guohuanjie/Documents/UoM Learning/COMP61342 Computer Vision/blog/BOW or Bag of Features.assets/WeChat893bc7cf4830aad284f7506a3075c163.png)

![WeChata8227ee240757dc230191dd52ece8000](/Users/guohuanjie/Documents/UoM Learning/COMP61342 Computer Vision/blog/BOW or Bag of Features.assets/WeChata8227ee240757dc230191dd52ece8000.png)

![WeChata2002a984e910613be3d571afa9d53fa](/Users/guohuanjie/Documents/UoM Learning/COMP61342 Computer Vision/blog/BOW or Bag of Features.assets/WeChata2002a984e910613be3d571afa9d53fa.png)

## Step 3: Classification

- SVM
- KNN

