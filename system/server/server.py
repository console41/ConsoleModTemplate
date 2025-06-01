# -*- coding: utf-8 -*-
import mod.server.extraServerApi as serverApi

from ...config.configUtils import *
from ..registerer.registererUtils import AddServerSystem

__eventList = []


def Listen(funcOrStr=None, namespace=serverApi.GetEngineNamespace(), systemName=serverApi.GetEngineSystemName(),
           priority=0):
    def wrapper(func):
        __eventList.append(
            (namespace, systemName, funcOrStr if isinstance(funcOrStr, str) else func.__name__, func, priority))
        return func

    return wrapper(funcOrStr) if callable(funcOrStr) else wrapper


def InitListen(instance):
    for namespace, systemName, eventName, callback, priority in __eventList:
        instance.ListenForEvent(namespace, systemName, eventName, instance, callback, priority)


@AddServerSystem(MOD_NAME + 'ServerSystem', MOD_NAME, DIR_ROOT+'.system.server.server.Main')
class Main(serverApi.GetServerSystemCls()):
    def __init__(self, namespace, systemName):
        super(Main, self).__init__(namespace, systemName)
        InitListen(self)
