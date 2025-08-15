# ConsoleModTemplate 文档

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
GameComp = COMPONENT_FACTORY.CreateGame(LEVEL_ID)
```

### enum

存放枚举值

### exception

存放错误

### function

存放你自定义或者封装的功能

### pack

存放外部的库(library)/API/SDK

### system

存放客户端 服务端系统

## 功能

### AddServerSystem

method in consoleModTemplate.modMain

- 参数
  
  | 参数名        | 数据类型 | 说明                 | 默认值 |
  | ---------- | ---- | ------------------ | --- |
  | namespace  | str  | 命名空间 一般为`MOD_NAME` |     |
  | systemName | str  | 系统名                |     |
  | clsPath    | str  | 类路径                |     |

- 返回值
  
  无返回值

### AddClientSystem

method in consoleModTemplate.modMain

- 参数
  
  | 参数名        | 数据类型 | 说明                 | 默认值 |
  | ---------- | ---- | ------------------ | --- |
  | namespace  | str  | 命名空间 一般为`MOD_NAME` |     |
  | systemName | str  | 系统名                |     |
  | clsPath    | str  | 类路径                |     |

- 返回值
  
  无返回值

### Listen

#### 服务端接口

  method in consoleModTemplate.system.server

- 说明
  
  用于快捷添加事件回调函数

- 参数
  
  | 参数名        | 类型        | 说明                    | 默认值                               |
  | ---------- | --------- | --------------------- | --------------------------------- |
  | funcOrStr  | func\|str | 事件名 不传时默认以下面的函数名作为事件名 |                                   |
  | namespace  | str       | 监听的事件命名空间             | `serverApi.GetEngineNamespace()`  |
  | systemName | str       | 监听的事件系统名              | `serverApi.GetEngineSystemName()` |
  | priority   | int       | 事件优先级                 | `0`                               |

#### 客户端接口

  method in consoleModTemplate.system.client

- 说明
  
  用于快捷添加事件回调函数

- 参数
  
  | 参数名        | 类型        | 说明                    | 默认值                               |
  | ---------- | --------- | --------------------- | --------------------------------- |
  | funcOrStr  | func\|str | 事件名 不传时默认以下面的函数名作为事件名 |                                   |
  | namespace  | str       | 监听的事件命名空间             | `clientApi.GetEngineNamespace()`  |
  | systemName | str       | 监听的事件系统名              | `clientApi.GetEngineSystemName()` |
  | priority   | int       | 事件优先级                 | `0`                               |

### InitListen

#### 服务端接口

  method in consoleModTemplate.system.server

- 说明
  
  用于初始化快速监听

- 参数
  
  | 参数名      | 数据类型         | 说明     | 默认值 |
  | -------- | ------------ | ------ | --- |
  | instance | ServerSystem | 需要监听的类 |     |

#### 客户端接口

  method in consoleModTemplate.system.client

- 说明
  
  用于初始化快速监听

- 参数
  
  | 参数名      | 数据类型         | 说明     | 默认值 |
  | -------- | ------------ | ------ | --- |
  | instance | ClientSystem | 需要监听的类 |     |

## AddButtonTouchEvent

客户端

method in consoleModTemplate.system.ui

- 说明
  
  用于给按钮快捷添加回调函数

- 参数
  
  | 参数名  | 类型  | 说明   | 默认值 |
  | ---- | --- | ---- | --- |
  | path | str | 按钮路径 |     |

### InitButton

客户端

method in consoleModTemplate.system.ui

- 说明
  
  用于初始化快速设置按钮回调

- 参数
  
  | 参数名      | 类型         | 说明       | 默认值 |
  | -------- | ---------- | -------- | --- |
  | instance | ScreenNode | 需要监听的UI类 |     |

### AddCommandCallback

服务端

method in consoleModTemplate.function.command.server.callback

- 说明
  
  用于快速给自定义指令添加回调函数

- 参数
  
  | 参数名         | 数据类型      | 说明                      | 默认值 |
  | ----------- | --------- | ----------------------- | --- |
  | commandName | func\|str | 指令的名字 不传时默认以下面的函数名作为指令名 |     |

- 示例
  
  ```python
  @Listen
  def CustomCommandTriggerServerEvent(self, args):
  if command in commandDict:
      commandDict[command](args)
  
  @AddCommandCallback
  def MyCustomCommand(args):
      command = args['command']
      origin = args['origin']
      variant = args['variant']
      param = args['args']
      # 编写业务代码
      pass
  
  @AddCommandCallback('MyCustomCommand')
  def MyCustomFuncName(args):
      command = args['command']
      origin = args['origin']
      variant = args['variant']
      param = args['args']
      # 编写业务代码
      pass
  ```

## 使用方法

- 复制到行为包
  
  ```bash
  cd 行为包路径
  git clone https://github.com/console41/console-mod-template.git
  ```

- 修改文件夹名 
  
  建议为`团队名+功能+Scipts`

- 配置
  
  打开config/modCommon文件 配置`MOD_NAME` `VERSION`等内容
  
  ```python
  MOD_NAME = 'com.功能名.你的名字'
  MOD_NAMESPACE = '模组的命名空间'
  VERSION = '0.0.1' # 版本
  ```

- 打开`system`文件夹 开始写代码

## 结语

我是萌新 大佬轻喷
