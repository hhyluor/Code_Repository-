# <font color="orange">Git 简介   </font>
> 学习目标: 
>
> 知道 git 的定义以及大概流程

### <font color="blue">定义   </font>

> Git 是目前世界上最先进的分布式版本控制系统（没有之一）

### <font color="blue">源代码管理的目的   </font>

* 方便多人协同开发
* 方便版本控制

### <font color="blue">Git 的诞生历史( 了解 )   </font>

- 作者是 Linux 之父：Linus Benedict Torvalds
- 当初开发 Git 仅仅是为了辅助 Linux 内核的开发（管理源代码）

![](./images/李纳斯.png)

> git 开发时间表
> - git 的产生是 Linux Torvals 在无奈被逼的情况下创造的，我看了一下时间历程：
>    - 2005 年 4 月3 日开始开发 git
>    - 2005 年 4 月 6 日项目发布
>    - 2005 年 4 月 7 日 Git 开始作为自身的版本控制工具
>    - 2005 年 4 月 18 日发生第一个多分支合并
>    - 2005 年 4 月 29 日 Git 的性能达到 Linux 预期
>    - 2005年 7 月 26 日 Linux 功成身退，将 Git 维护权交给 Git 另一个主要贡献者 Junio C Hamano，直到现在

> Git 迅速成为最流行的分布式版本控制系统，尤其是 2008 年，GitHub 网站上线了，它为开源项目免费提供 Git 存储，无数开源项目开始迁移至 GitHub，包括 jQuery，PHP，Ruby 等等

### <font color="blue">Git 管理源代码特点   </font>

* `Git`是分布式管理.服务器和客户端都有版本控制能力,都能进行代码的提交、合并、...

    ![](./images/分布式版本控制.png)

* .`Git`会在根目录下创建一个`.git`隐藏文件夹，作为本地代码仓库

    ![](./images/本地仓库.png)

### <font color="blue">Git 操作流程图解   </font>

```
Git服务器 --> 本地仓库 --> 客户端 --> 本地仓库 --> Git服务器
```

![](./images/GIT操作图解.png)

### <font color="blue">总结:    </font>

* 使用 git 可以实现源代码的管理
* git 的特点是分布式管理系统
* git 可以实现多人协同开发, 并且能够方便管理各个版本