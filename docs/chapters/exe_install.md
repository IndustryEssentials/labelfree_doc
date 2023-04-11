## 部署步骤

### 1.服务器要求

- 操作系统要求：win7?
- 内存要求：最低要求 8G
- 部署目录空间要求： 50G（取决于标注数据集的大小）




<!-- <iframe width="1080" height="360" src="//player.bilibili.com/player.html?aid=553987860&bvid=BV1Qv4y1P7Uc&cid=715679290&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe> -->


### 2.网络端口要求：

labelfree正常运行需要网络环境提供如下的网络端口配置要求，管理员可根据实际环境中组件部署的方案，在网络侧和主机侧开放相关端口：

| 组件  | 默认端口 | 说明                            |
| ----- | -------- | ------------------------------- |
| nginx | 8080     | 浏览器访问端口                  |
| mysql | 13306     | 默认安装的数据库对外提供的端口  |
| minio | 19000     | 默认安装的 minio对外提供的端口  |
| redis | 16379     | 默认安装的 Redis 对外提供的端口 |

### 3.安装步骤

1 下载安装包

下载地址：

  - [国际下载](https://github.com/IndustryEssentials/label-free/releases/download/4.1.0/labelfree_app.zip) 

  - [国内备用下载](https://www.123pan.com/s/cUhcVv-3GOF3.html){target=_blank}（国内用户使用）

2 安装
双击安装包，解压后双击`LabelFree.exe`启动。

**访问**

```
http://YOUR_HOST_IP:8080
```

默认管理员账号、密码

```
labelfree@viesc.com 
labelfree@2022
```

![](./../assets/images/5yaj3f.png)
