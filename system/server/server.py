# -*- coding: utf-8 -*-
import mod.server.extraServerApi as serverApi

from ...function.serverFunctionUtils import *

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


class Main(serverApi.GetServerSystemCls()):
    def __init__(self, namespace, systemName):
        super(Main, self).__init__(namespace, systemName)
        InitListen(self)

    @Listen
    def CustomCommandTriggerServerEvent(self, args):
        command = args['command']
        origin = args['origin']
        variant = args['variant']
        param = args['args']
        if command in commandDict:
            commandDict[command]()
