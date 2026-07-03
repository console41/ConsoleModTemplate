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


def RegisterConsoleModClient():
    from ...config.configUtils import DIR_ROOT as BASE_DIR_ROOT
    return clientApi.RegisterSystem(MOD_NAME, CLIENT_SYSTEM_NAME,
                                    BASE_DIR_ROOT + '.library.consoleMod.system.client.client.Main')


def Listen(funcOrStr=None, namespace=clientApi.GetEngineNamespace(), systemName=clientApi.GetEngineSystemName(),
           priority=0):
    clientSystem = clientApi.GetSystem(MOD_NAME, CLIENT_SYSTEM_NAME)  # type: Main

    def wrapper(func):
        clientSystem.eventList.append(
            (namespace, systemName, funcOrStr if isinstance(funcOrStr, str) else func.__name__, func, priority))
        return func

    return wrapper(funcOrStr) if callable(funcOrStr) else wrapper
