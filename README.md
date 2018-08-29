# 本项目基本使用

## 上传到gitlab用户

### 生成密钥 

```
ssh-keygen
```

### 把 id_rsa.pub 的公钥上传到用户的密钥管理即可

```
cat .ssh/id_rsa.pub > 用户管理密钥
```
## 生成全局配置

```
git config --global user.name "xxx"
git config --global user.email "xxx@xx"
```

## 下载gitlab项目

```
 mkdir tt && cd tt

 git clone git@gitlab.inin88.com:foxin.li/python.git

 git checkout -b fix/bug

 git add .

 git commit -m "change what things"

 git merge fix/bug origin

 git push origin master
```


# 本项目用于测试

```
rand_name 是用于随机名字的python脚本
其他是不同的脚本
```
