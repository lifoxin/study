## 本项目基本使用


**生成密钥**

```
ssh-keygen
```

**把 id_rsa.pub 的公钥上传到用户的密钥管理即可**

```
cat .ssh/id_rsa.pub > 用户管理密钥
```
**生成全局配置**

```
git config --global user.name "xxx"
git config --global user.email "xxx@xx"
```

**下载github项目**

```
 mkdir tt && cd tt

 git clone https://github.com/lifoxin/study.git
 
 创建分支
 git checkout -b fix/bug

 git add .

 git commit -m "change what things"
 
 合并fix/bug分支到origin当前分支
 git merge fix/bug origin

 推送origin到master远程分支
 git push origin master
```
**本项目用于测试**

```
rand_name 随机名字
rookie 是菜鸟学习的脚本
script 也是7788的脚本
socket 是tcp/udp访问请求
spider 爬虫脚本
ss 是ss的守护进程
```
