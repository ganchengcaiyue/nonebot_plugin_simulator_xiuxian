<div align="center">
  <img src="https://s2.loli.net/2022/06/16/opBDE8Swad5rU3n.png" width="180" height="180" alt="NoneBotPluginLogo">
  <br>
  <p><img src="https://s2.loli.net/2022/06/16/xsVUGRrkbn1ljTD.png" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# 修仙1.0

_✨ QQ群聊修仙文字游戏✨_

🧬 插件主要为实现群聊修仙功能！🎉 

<p align="center">
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/nonebot-2.0.0r4+-red.svg" alt="NoneBot">
  <a href="https://pypi.org/project/nonebot_plugin_simulator_xiuxian/">
      <img src="https://img.shields.io/pypi/v/nonebot_plugin_simulator_xiuxian.svg" alt="pypi">
  </a>
</p>
</div>

## 简介

本插件主要为实现群聊修仙功能,最近经常封号，请自行判断后再使用，已默认转成图片模式，如需关闭，可在config.py处调整img字段为false<br>
推荐使用[修仙2.0](https://github.com/QingMuCat/nonebot_plugin_xiuxian_2)

# 设定征集中，有好的想法可以推送给群主,只要你敢想群主都能干~~~

# 启动时会自动下载需要的压缩包到 data <br>需自行解压并命名为 xiuxian 才可正常使用修仙1.0<br>
nonebot_plugin_simulator_xiuxian(0.5.36)及以上 

## 计划

1、移除认为与修仙无关功能，简化修仙命令。<br>
2、新功能开发 /完成度-50%。<br>

## 特色功能

  指令较多，具体查看指令 修仙帮助<br> 
  1、悬赏令系统：发送指令 悬赏令帮助 获取信息<br> 
  2、宗门系统：发送指令 宗门帮助 获取信息<br> 
  3、世界boss系统：发送 世界boss帮助 获取信息<br> 
  4、坊市：查询商店信息，当前商品为用户自行上架拍卖，发送指令 背包帮助 获取信息<br> 
  5、灵庄：银行系统，发送 灵庄帮助 获取信息<br> 
  6、功法：功法系统，发送指令 功法帮助<br> 
  7、炼丹：发送 炼丹帮助 获取对应操作指令，需要炼丹炉，可在世界boss处获取。<br> 
  8、秘境：发送 秘境帮助 获取对应操作指令。<br> 
  9、修仙系统在 重入仙途/灵石出关/结算秘境 时20分之1概率触发<br>
  
## 安装
1、下载插件文件

- 使用脚手架安装(推荐github处拉取源码使用)


```
pip install nonebot_plugin_simulator_xiuxian
nb plugin install nonebot_plugin_simulator_xiuxian
```

- 使用github处拉取源码使用

```
git clone https://github.com/luoyefufeng/nonebot_plugin_simulator_xiuxian.git
```

2、下载数据文件

使用git clone的方法的，进入插件目录，把data文件夹中的全部内容移动到bot的数据文件夹中<br>
使用pip，首次启动会在 data 下载压缩包 (xiuxian_XXX.zip) 解压并命名为 xiuxian 重新启动即可使用<br>
bot的数据文件夹一般为 .env 同级目录下的data文件夹

3、加载插件
pip 下载才
- 然后在pyproject.toml文件中添加(pip 下载添加)

```
plugins = ['nonebot_plugin_simulator_xiuxian']
```

4、如果遇到问题

- 当前首次使用，未自动创建json文件及sql文<br>在[GitHub](https://codeload.github.com/luoyefufeng/xiuxian/zip/refs/heads/main)处下载，目录data -> xiuxian
处下载的文件，放置于bot目录，data -> xiuxian文件夹处<br>
- 当为放置为src/plugins目录使用时<br>修改xiuxian目录下__init__.py文件中的42行：src=''中的内容<br>填写的是存放插件的目录，一般情况下 src='src.plugins.'  如有不同请按照格式修改

5、如解决不了进交流群：760517008 提问，提问请贴上完整的日志,群里回的快！（疯狂暗示）<br> 
   修仙体验群: 766929439

## 配置文件
1、配置文件一般在data/xiuxian文件夹下，自行按照json格式修改即可，一些字段的含义可以进群交流<br>
2、子插件的配置会在插件运行后在子插件文件中生成config.json文件，该文件字段含义在同级目录的xxxconfig.py有备注。注意：修改配置只需要修改json即可，修改.py文件的话需要删除json文件才会生效，任何修改都需要重启bot。

## 更新
- 使用脚手架安装的
```
pip install nonebot_plugin_simulator_xiuxian -U
```
```
pip install nonebot_plugin_simulator_xiuxian --upgrade
```
- 使用github处拉取源码使用的
进入插件目录执行命令：
```
git pull
```


## 功能展示

- 使用 `我要修仙` 指令触发机器人，机器人创建用户信息，生成灵根，境界等信息。
- 发送突破，当修为足够时，可突破境界。
- 发送修仙签到，获取每日初始化的灵石及修为。

![image](https://user-images.githubusercontent.com/44226600/187607785-3ea934f4-2b5c-418e-9b99-e8a8e5562125.png)
![屏幕截图 2024-04-19 033714](https://github.com/luoyefufeng/nonebot_plugin_simulator_xiuxian/assets/127736993/8519dca7-6a49-409a-a386-0a64e1faa500)

## 特别感谢

- [NoneBot2](https://github.com/nonebot/nonebot2)：本插件实装的开发框架。
- [go-cqhttp](https://github.com/Mrs4s/go-cqhttp)：稳定完善的 CQHTTP 实现。
- [xiuxian](https://github.com/s52047qwas/nonebot_plugin_xiuxian) 原版修仙
- [xiuxian2](https://github.com/QingMuCat/nonebot_plugin_xiuxian_2) 修仙2
## 插件依赖


- nonebot2
- nonebot-adapter-onebot
- go-cqhttp

## 支持

大家喜欢的话可以给这个项目点个star

有bug、意见和建议都欢迎提交 [Issues](https://github.com/luoyefufeng/nonebot_plugin_simulator_xiuxian/issues) <br>或者联系进入QQ交流群：760517008<br>修仙1.0体验群：766929439<br>(注：提交bug时加上你的地址)<br>修复bug X<br>干掉发现bug的 √<br>


## 许可证
本项目使用 [MIT](https://choosealicense.com/licenses/mit/) 作为开源许可证

