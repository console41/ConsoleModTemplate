# ConsoleModModel 文档

## 简介

本项目是基于我的世界中国版ModSDK的模组模板

脚本共有9个文件夹

### cls

用于存放类

### component

用于存放 [组件](https://mc.163.com/dev/mcmanual/mc-dev/mcdocs/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/Component.html#getcomponentcls)

### config

存放配置 

该模板的配置划分为多个文件 通过`configUtils`整合 也可以直接把这个文件删了 但是不建议这么做

### constant

存放常量 例如`LEVEL_ID`各种ModSDK的组件也可以存放 示例

```python
import mod.server.extraServerApi as serverApi

LEVEL_ID = serverApi.GetLevelId()
COMPONENT_FACTORY = serverApi.GetComponentFactory()
GAME_COMP = COMPONENT_FACTORY.CreateGame(LEVEL_ID)
```

### enum

存放枚举值 可以以enumUtils整合(需自己添加)

### exception

存放错误

### function

存放你自定义或者封装的功能

### pack

存放外部的库(library)/API/SDK 同样以utils整合

### system

存放客户端 服务端系统

## 一些功能

### `AddServerSystem`和`AddClientSystem`

打开modMain可以看到AddServerSystem和AddClientSystem 这两个装饰器可以快捷注册系统 

两者需要传3个参数

| 参数名        | 类型  | 描述                 |
| ---------- | --- | ------------------ |
| namespace  | str | 命名空间 一般为`MOD_NAME` |
| systemName | str | 系统名                |
| clsPath    | str | 类路径                |



### `Listen`和`InitListen`

```python
def Listen(funcOrStr=None, namespace=clientApi.GetEngineNamespace(), systemName=clientApi.GetEngineSystemName(),
           priority=0):
    def wrapper(func):
        __eventList.append(
            (namespace, systemName, funcOrStr if isinstance(funcOrStr, str) else func.__name__, func, priority))
        return func

    return wrapper(funcOrStr) if callable(funcOrStr) else wrapper


def InitListen(instance):
    for namespace, systemName, eventName, callback, priority in __eventList:
        instance.ListenForEvent(namespace, systemName, eventName, instance, callback, priority)

```

`Listen`需传入3个参数

| 参数名        | 类型       | 描述                                           |
| ---------- | -------- | -------------------------------------------- |
| funcOrStr  | func或str | 时间名 不传时默认以下面的函数名作为事件名                        |
| namespace  | str      | 监听的事件命名空间 默认`clientApi.GetEngineNamespace()` |
| systemName | str      | 监听的事件系统名 默认`clientApi.GetEngineSystemName()` |
| priority   | int      | 事件优先级                                        |

`InitListen`在系统__init__时调用 需传入1个参数

| 参数名      | 类型        | 描述     |
| -------- | --------- | ------ |
| instance | 客户端/服务端系统 | 监听类的实例 |

## `AddButtonTouchEvent`与`InitButton`

用法与上者类似

`AddButtonTouchEvent`是一个装饰器 下面是按钮回调函数 自身需传入一个参数

| 参数名  | 类型  | 描述   |
| ---- | --- | ---- |
| path | str | 按钮路径 |

`InitButton`在Create时调用 需传入一个参数

| 参数名      | 类型         | 描述       |
| -------- | ---------- | -------- |
| instance | ScreenNode | 需要监听的UI类 |



## 使用方法

将ModName直接复制到你的行为包 并修改`MOD_NAME`等配置

## 一些功能的原作者

- 7stars - Listen装饰器

注: CallServer等功能被我砍掉了 因为这样不方便查看哪些事件是另一端发来的 所以namespace和systemName需要自己填写

- tyuall - 按钮回调

## 结语

该模板还未经过充分测试 可能有bug 大佬轻喷
