# A Blockchain Based Credential Store

This project will build a simple blockchain based system for storing and querying peoples' credentials (such as degree certificates, etc.).



------

> Who

- Issuers

  控制那些他发布证书的人，能够发布学历，撤销学历

- learners

  需要对凭证掌握控制权

- trust

  能在不询问学历颁发机构情况下，对学历进行验证



> 隐私保护

采用特殊手段确保只有learner能自由访问，限制其他想利用数据的组织。



> 跳过issuer进行验证

无需签发者参与，学生就可以验证学历。



## 大致思路

- 发布认证token，如100个。初始时全部代币由教育局地址持有。教育局会向认证的大学发送1个代币。
- 学校申请以太坊公钥和密钥，向教育局申请往地址中打入1个认证币，获得挖矿权限。
- 学校申请以太坊公钥和密钥，获取地址后，向教育局申请往地址中打款，获得挖矿权限。
- 学生生成以太坊公钥和私钥。将公钥发送给学校, 并申请将自己学历上链 (K.pub,K.pri)
- 学校用K.pub对学生学历进行加密，上传到以太坊链上。本处要验证上传权限，如持有认证token数量>=1才能上传。 上传后，会有证书编号(区块中显式存储)和学历信息(隐式存储)和学历信息明文的hash值。
- 学生从链上查询自己的学历密文，用私钥解密后，将学历明文发送给企业
- 企业把明文计算hash,在链上和学历编号进行验证即可



