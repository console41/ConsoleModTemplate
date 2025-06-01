# -*- coding: utf-8 -*-

import mod.client.extraClientApi as clientApi

from ...config.configUtils import *
from ..registerer.registererUtils import AddClientSystem

__eventList = []


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


@AddClientSystem(MOD_NAME + 'ClientSystem', MOD_NAME, DIR_ROOT+'.system.client.client.Main')
class Main(clientApi.GetClientSystemCls()):
    def __init__(self, namespace, systemName):
        super(Main, self).__init__(namespace, systemName)
        InitListen(self)
