# 2 - 3 Syntactic Parsing2: Phrase structure 短语结构

* 句子结构是基于短语的(phrases)
* phrase结构树 展示：
	* 将单词分组成phrases
	* phrases的层次结构

## Phrase structure 短语结构
### 短语phrases的种类
	* NP: 名词短语
	* VP: 动词短语
	* PP: 介词短语
	* AdjP: 形容词短语
	* AdvP: 副词短语

![](2%20-%203%20Syntactic%20Parsing2%20Phrase%20structure%20%E7%9F%AD%E8%AF%AD%E7%BB%93%E6%9E%84/%E6%88%AA%E5%B1%8F2021-02-18%2016.06.21.png)

### 无上下文语法
![](2%20-%203%20Syntactic%20Parsing2%20Phrase%20structure%20%E7%9F%AD%E8%AF%AD%E7%BB%93%E6%9E%84/%E6%88%AA%E5%B1%8F2021-02-18%2016.10.38.png)

## 短语结构分析
### Step1
 标注每个token的语法类别（POS）
![](2%20-%203%20Syntactic%20Parsing2%20Phrase%20structure%20%E7%9F%AD%E8%AF%AD%E7%BB%93%E6%9E%84/%E6%88%AA%E5%B1%8F2021-02-18%2016.37.28.png)

### Step2
有两个主要成分：一个名词短语（NP）和一个动词短语（VP）
找出两者之间的界限
![](2%20-%203%20Syntactic%20Parsing2%20Phrase%20structure%20%E7%9F%AD%E8%AF%AD%E7%BB%93%E6%9E%84/%E6%88%AA%E5%B1%8F2021-02-18%2016.39.04.png)

### Step3
对每个head名词/代词、动词、形容词、副词、介词，投影一个短语节点：
NP, VP, AdjP, AdvP, PP
![](2%20-%203%20Syntactic%20Parsing2%20Phrase%20structure%20%E7%9F%AD%E8%AF%AD%E7%BB%93%E6%9E%84/%E6%88%AA%E5%B1%8F2021-02-19%2012.27.09.png)

### Step4
将剩余的tokens连接到他们所属的节点上
![](2%20-%203%20Syntactic%20Parsing2%20Phrase%20structure%20%E7%9F%AD%E8%AF%AD%E7%BB%93%E6%9E%84/%E6%88%AA%E5%B1%8F2021-02-19%2012.28.18.png)

![](2%20-%203%20Syntactic%20Parsing2%20Phrase%20structure%20%E7%9F%AD%E8%AF%AD%E7%BB%93%E6%9E%84/%E6%88%AA%E5%B1%8F2021-02-19%2012.33.11.png)

## Step5
最后的树
![](2%20-%203%20Syntactic%20Parsing2%20Phrase%20structure%20%E7%9F%AD%E8%AF%AD%E7%BB%93%E6%9E%84/%E6%88%AA%E5%B1%8F2021-02-19%2012.33.43.png)

# 依存结构和短语结构对比
* Dependency structure
	* 有向边：head-dependent关系
	* 边标签：语法作用
	* 词性标注：语法种类

* Phrase structure
	* 非终止的节点：短语（及其层次结构）
	* 词性标注：语法种类
![](2%20-%203%20Syntactic%20Parsing2%20Phrase%20structure%20%E7%9F%AD%E8%AF%AD%E7%BB%93%E6%9E%84/%E6%88%AA%E5%B1%8F2021-02-19%2012.37.08.png)

## 依存结构：内中心 vs 外中心结构
![](2%20-%203%20Syntactic%20Parsing2%20Phrase%20structure%20%E7%9F%AD%E8%AF%AD%E7%BB%93%E6%9E%84/%E6%88%AA%E5%B1%8F2021-02-19%2012.48.03.png)


## Verb valency 动词的价
* 某些动词需要某些类型的从句
* Valency:谓语(动词)控制的参数数量
![](2%20-%203%20Syntactic%20Parsing2%20Phrase%20structure%20%E7%9F%AD%E8%AF%AD%E7%BB%93%E6%9E%84/%E6%88%AA%E5%B1%8F2021-02-19%2012.52.27.png)

## 谓语-参数结构 PAS （Predicate-argument Structures）
* 动词价概念的一般化
* Predicates 谓语可以是任何一个词性(part of speech)，不止是动词
* Argument 参数是用参数符号指定的
![](2%20-%203%20Syntactic%20Parsing2%20Phrase%20structure%20%E7%9F%AD%E8%AF%AD%E7%BB%93%E6%9E%84/%E6%88%AA%E5%B1%8F2021-02-19%2012.55.42.png)


## 我们可以用Parsing解析的结果做什么？
* 关系抽取 Relation extraction
* 信息提取 Information extraction