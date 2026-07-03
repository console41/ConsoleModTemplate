# -*- coding: utf-8 -*-
import mod.client.extraClientApi as clientApi

from .config.configUtils import *
from .system.client.client import Main, updateFunc, destroyFunc
from .system.ui.main import BaseScreenNode


def SystemUpdate(func):
    updateFunc.append(func)
    return func


def SystemDestroy(func):
    destroyFunc.append(func)
    return func


def RegisterClient():
    from ...config.configUtils import DIR_ROOT as BASE_DIR_ROOT
    clientApi.RegisterSystem(MOD_NAME, CLIENT_SYSTEM_NAME,
                                    BASE_DIR_ROOT + '.library.consoleMod.system.client.client.Main')


class _ListenConfig(object):
    EVENT_NAME = None
    NAMESPACE = None
    SYSTEM_NAME = None
    PRIORITY = None


class _ListenEventPool(list):
    def append(self, func):
        super(_ListenEventPool, self).append(func)
        # 变化时触发
        # 先从func中取出挂载的配置
        config = getattr(func, '_ListenConfig')  # type: _ListenConfig
        eventName = config.EVENT_NAME
        namespace = config.NAMESPACE
        systemName = config.SYSTEM_NAME
        priority = config.PRIORITY
        # 将func挂载到Mod的系统里
        clientSystem = clientApi.GetSystem(MOD_NAME, CLIENT_SYSTEM_NAME)
        # 先检查这个函数名是否已经存在并生成一个唯一的函数名
        baseName = func.__name__
        currentName = baseName
        num = 0
        while hasattr(clientSystem, currentName):
            num += 1
            currentName = baseName + "_" + str(num)

        def MakeWrapper(targetFunc, fixedName):
            def wrapper(args):
                return targetFunc(args)

            wrapper.func_name = fixedName
            return wrapper

        bindFunc = MakeWrapper(func, currentName)
        # 挂载
        setattr(clientSystem, currentName, bindFunc)
        # 监听事件
        clientSystem.ListenForEvent(namespace, systemName, eventName, clientSystem, getattr(clientSystem, currentName),
                                    priority)


_listenEventPool = _ListenEventPool()


def Listen(funcOrStr=None, namespace=clientApi.GetEngineNamespace(), systemName=clientApi.GetEngineSystemName(),
           priority=0):
    def wrapper(func):
        # 创建配置实例
        config = _ListenConfig()
        config.EVENT_NAME = funcOrStr if isinstance(funcOrStr, basestring) else func.__name__
        config.NAMESPACE = namespace
        config.SYSTEM_NAME = systemName
        config.PRIORITY = priority
        # 挂载配置到函数
        setattr(func, '_ListenConfig', config)
        # 加入全局池子，供后续统一遍历注册
        _listenEventPool.append(func)
        return func

    return wrapper(funcOrStr) if callable(funcOrStr) else wrapper
