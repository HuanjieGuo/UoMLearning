#### Chanllenge/Response Authentication

1.客户端向服务器发送一个请求

2.服务器接收到请求后，生成一个8位的Challenge，发送回客户端

3.客户端接收到Challenge后，使用登录用户的密码hash对Challenge加密，作为response发送给服务器

4.服务器校验response，校验方法是：服务器取出该用户的密码hash，使用和客户端相同的算法（DES）加密Challenge，然后比较密文。如果相同则认证成功。



#### 1st  **Protocol – Symmetric-Key based**

Share same key

1. Alice -> I am a Alice   -> Bob
2. Alice <- nonce(Nb)   <- Bob
3. Alice -> Ek(Nb) -> Bob
4. Bob: check the Ek(Nb).



#### 2nd Protocol – Symmetric-Key based

1. Alice -> I am a Alice   -> Bob
2. Alice <- nonce(Nb)   <- Bob
3. Alice -> Ek(Nb) -> Bob
4. Bob: check the Ek(Nb).
5. Alice -> (Na) -> Bob
6. Alice <- (Ek(Na)) <- Bob
7. Alice checks the Ek(Na)



#### 3rd Protocol – Symmetric-Key based

1. Alice -> I am a Alice ,  Na   -> Bob
2. Alice <- nonce(Nb), Ek(Na)   <- Bob
3. Alice Verify
4. Alice -> Ek(Nb) -> Bob
5. Bob verify.





