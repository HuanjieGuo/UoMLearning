[Computer Vision Standford](https://www.youtube.com/watch?v=vT1JzLTH4G4&list=PL3FW7Lu3i5JvHM8ljYj-zLfQRF3EO8sYv)

Deep learning (garden)

# Lecture 1 Introduction to CNN

[An amazing CNN Introduction in Youtube](https://www.youtube.com/watch?v=FmpDIaiMIeA&list=PLwSoEwQqOI-v0l_byk2-SLzN8VtmF0l4v)



Convolutional Neural Networks have become an important tool to reconize pattern.

![WeChat5ca86a71be83b89815e3055cbff2e9ab.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gosc0xlmfej31z80l44qp.jpg)



# Lecture 2. Image Classification

## Classifier 1: Nearest neighbour

![3051616405694_.pic_hd.jpg](http://ww1.sinaimg.cn/large/008aPpVGgy1gostg3q7zvj32ck1d0h5j.jpg)

> L1 ( Manhattan)  distance

![3071616405875_.pic_hd.jpg](http://ww1.sinaimg.cn/large/008aPpVGgy1gostjfg0ukj318a0hmgp1.jpg)

Remember to use Math.abs!

![WeChat1918fb1c75d7eb51cb61adc8a14a6045.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gostm0g49dj31do11wx6q.jpg)

> analysis

**Train O(1)**

**Predict O(N)**

Actually we want classifiers that are **fast** at prediction; **slow** for training is ok.

![WeChat93ba171c3b4006e36bc7542211ac2d7c.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gostsmylvfj32bo0zsu0y.jpg)



> L2 (Euclidiean) distance

![WeChat0f31c857a533dd08c098910a2a9f22eb.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gostyan303j321s0vohdt.jpg)

The difference is that in L1, if you rotate the pic, the value will change, but in L2, it doesn't.

Check the differences of L1 and L2 after class.

![WeChatf4c4b8905436cc25d19802c7ce26eadc.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gosu3st3kcj321w0x4hdu.jpg)

from the pic we can found that in L1, there are more curves while in L2, it is more smooth.

remember: when your individual element have **some different meaning, it is better to use L1**. eg.you want represent an employee, his information is about salary, how many years of work.

When all the aspect **have same meaning, it is better to use L2.** eg. image, video

[try it yourself online](http://vision.stanford.edu/teaching/cs231n-demos/knn/)



![WeChatf3c2912d4d97332fadd5af781a072a0a.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gosujhdvssj32b811ob2b.jpg) 

you can use **k-fold cross-validation**.



![WeChatd651df71998996fe32154fcf63c95655.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gosur6vbdxj327w14s7wj.jpg)



![WeChatdf07327a53cab57fb1ad27f5c78540a8.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gosutt4zjkj32c4154kjo.jpg)



tip: **curse of dimensionality** 维数灾难

![WeChate22fe5e3c7da17b6e4c8297d80ff61a6.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gosv1ofzmqj32co14gnpe.jpg)

if you have many dimensions, you need a lot of training data to cover the sapce!





> Curse of dimensionality

![WeChat3106334c6a9c5e1faed700386ac42890.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gosvfps2z4j31xc19ke86.jpg)

It seems like that there are 20*20 possibility for the picture, but actually , you will never get a picture random like the below one. So, it is less than 400 possibilities!

<img src="http://ww1.sinaimg.cn/large/008aPpVGgy1gosvixnx75j30o40l01kx.jpg" alt="WeChat0d1e989d8ed2b796e290d26adc8e6c34.png" style="zoom:25%;" />

- Machine learning methods are statistical by nature
  - count observations in various regions of some space.
  - use counts to construct the predictor f(x)
  - e.g decision trees
- As dimensionality grows: fewer observations per region
  - 1d: 3 regions, 2d: 3^2 regions, 1000d-hopeless

![WeChate12f78cee11d6570c1a21031fa67617a.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gosvr47jf6j31w40lkhdv.jpg)



## Classifier 2: Linear Classifier

![WeChat1ee0274f8044a68d87880a87cf1a701f.png](http://ww1.sinaimg.cn/large/008aPpVGgy1got8cucb8uj31lk0t6hdt.jpg)

![WeChat31aa78a4b334aea72c9ef26f00a19f4b.png](http://ww1.sinaimg.cn/large/008aPpVGgy1got8er2wbej31me0que81.jpg)

**f(x,W) = Wx+b**

![WeChat9bcbb73440fe0fcf6dc213f3f52a0696.png](http://ww1.sinaimg.cn/large/008aPpVGgy1got8n96ym4j30ye0s4qv5.jpg)

![WeChatb517623720706575657faf88d15891ce.png](http://ww1.sinaimg.cn/large/008aPpVGgy1got8oqdsghj31lo0re4qp.jpg)

# Lecture 3.Loss Function and Optimization

1. Define a loss function that quantifiers our unhappiness with the scores across the training data.
2. Come up with a way of efficiently finding the parameters that minimize the loss function (optimization)

![WeChat232d4694ea99c8596c9bcaaab146b66b.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gotgos5ttej30vw0xotre.jpg)

s.j is the label

s.yi is the prediction

loss = s.j - s.yi + 1 means that we want a s.yi that is much biggest than 1.

 ![WeChat7f8b7f12618ab206f351db62c73667e3.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gotgyqfhfcj326014o7wk.jpg)



![WeChatd7f8865b21dba7c8075e595757b7ea7e.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gothc880ovj32000ygnpd.jpg)

Regularization encourages the model to somehow pick a simple W.

![WeChat25712b6a0042f85493af7264139e46aa.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gothotpkrbj325k158u0z.jpg)



![WeChat23a4ada3eb3f8865e1ce00270abe88bf.png](http://ww1.sinaimg.cn/large/008aPpVGgy1goti5pigqij325g1084qr.jpg)

![WeChat3917014e5b3bbf40f7169cf2b26be3b4.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gotibsfs0hj327415g1kz.jpg)

![WeChatce73a9060b571f1b8c638fbf00c91f57.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gotid7t5nrj325o14c7wi.jpg)



![WeChata68852ee81782c3293902ecc21aa76e2.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gotiryfluwj325w11gqv6.jpg)



> how to optimize?

1. Random search
2. Follow the slope

Calculate every step require many computation. So use batch update SGD is a good idea.

![WeChat6bb0e7da36abd932d58994497b82579d.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gotj5ygbzvj3250140b2b.jpg)

![WeChate7e5f00b823031318ac2be76162b53f5.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gotjbdd0u6j32640zcb29.jpg)



# Lecture 5. Convolutional Neural Networks

![WeChat540923d25e467d24ed8f7bb63b31a3ca.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gou3qp7qyoj324c1akhdu.jpg)

zero padding is use to maintain the full size output.

If you don't use it, the output size will get smaller and smaller over times.

![WeChatffcba48adea0ffe9b1794d106c69d018.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gou3y5gfloj325c13w7wi.jpg)



![WeChat9c8f4309fa51c7bfea2f1ab61e0e593e.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gou4fz7s94j31vg12gqv5.jpg)



![WeChataa2829f6b81d1a96c96cb993318ee9d0.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gou4uqozaaj321c12ob29.jpg)



Stride and pooling both can downsample the output.



# Lecture 8. Deep Learning Sottware

![WeChat9533505ffd0fb8d65cf34f1925016e44.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gov7yo87rnj324012wnpe.jpg)



# Lecture 9. CNN Arichitecture



# Lecture 11. Detection and Segmentation

![WeChat75db3b85905340f510e65aa6424e7a0f.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gowxp4lf19j327c0toe82.jpg)

> how to upsampling

![WeChat0c82d98705d524af405b665044df82dd.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gowxs39gw8j32540lw7nh.jpg)

If you want to use max unpooling, you need to remember which element was max!

![WeChat0744d84cb8fbbd9637925912de83f532.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gowxvk09kkj326o12wu0x.jpg)

![WeChatd364fa540ca5cb0fa76e04ac6c47e38e.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gowy5a3f3qj324c10cx6p.jpg)

![WeChat4fcb571125001981a3fe3af84a04bbfd.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gowy8ga7loj32581207wi.jpg)

> Region Proposals

- Find "blobby" image regions that are likely to contain objects
- Relatively fast to run; e.g. Selective Search gives 1000 region proposals in a few seconds on CPU

![3471618241550_.pic_hd.jpg](http://ww1.sinaimg.cn/large/008aPpVGgy1gphdsxfr7oj31ts0h8te7.jpg)

> R-CNN

![WeChat6e223a5b84a72cecae116ab931c072b7.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gphdwakvkyj31ik0us7wi.jpg)

- Ad gic training objectives
  - Fine-tune network with softmax classifier(log loss)
  - Train post-hoc linear SVMs(hinge loss)
  - Train post-hoc bounding-box regressions (least squares)
- Training is slow, takes a lot of disk space
- Inference (detection) is slow

> Fast R-CNN

![WeChat3e6f53f24b4864320eb15cc02a65af09.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gphe6mzrhij31lk0rgqv5.jpg)

![WeChat369f644320b81f0b41b256532c2c0f11.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gphe7opjl5j31h00yckjl.jpg)

> Faster R-CNN

![WeChatc39f5c1cd27ff322fe4c3f08f37340cd.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gpheacdni1j31ww0y8kjm.jpg)

> Detection without Proposals: YOLO/SSD

![WeChatf2fa8488a07c6d638760f97d52daf17e.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gpheg29tf3j31zs0t4x6r.jpg)

## R-CNN

propose a bunch of boxes in the image and see if any of them actually correspond to an object.

![WeChat88e4857a6e0ad106b77cded27e0ed27d.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gphr02uetqj31zo0s4kjo.jpg)

R-CNN should run a segmentation algorithm

1. Generate a set of proposals for boundings boxes
2. Run the images in the bounding boxes through a pre-trained AlexNet and finally an SVM to see what object the image in the box is
3. Run the box through a linear regression model to output tighter coordinates for the box once the object has been classified.



## Fast R-CNN

> background

R-CNN works really well, but is really quite slow for a few simple reasons:

1. It requires a forward pass of the CNN(AlexNet) for every single region proposal for every single image. (That's around 2000 forward passes per image!)
2. It has to train three different models separately - the CNN to generate image features, the classifier that predicts the class, and the regression model to tighten the bounding boxes. This makes the pipeline extremely hard to train.

> Fast R-CNN

**Insight 1: RoI(Region of Interest) Pooling**

Main Ideas:  Why not run the CNN just once per image and then find a way to share that computation across the 2000 proposals?

![WeChat695c0bdf727723d156b85349df0c9b57.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gphq4ksmtxj323812gnpe.jpg)



**insight 2: Combine All Models into One Network**

![img](https://miro.medium.com/max/2460/1*E_P1vAEbGT4HNYjqMtIz4g.png)

Fast R-CNN instead used a single network to compute all three.

## Faster R-CNN

![](https://miro.medium.com/max/1300/0*_nNI03ESXm2P6YXO.)

> Region Proposal Network

Inputs: CNN Feature Map

Outputs: A bounding box per anchor. A score representing how likely the image in that bounding box will be an obejct.



# Lecture 12. Visualizing and Understanding

> Gradient Ascent

Generate a synthetic image that maximally activates a neuron

![WeChat066ec3ce38fe3296a5250ed7523ac010.png](http://ww1.sinaimg.cn/large/008aPpVGgy1gpixw2leuej31hg0fowuv.jpg)





















