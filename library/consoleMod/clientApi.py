# -*- coding: utf-8 -*-
import mod.client.extraClientApi as clientApi

from .config.configUtils import *
from .system.client.client import Main


def RegisterConsoleModClient():
    from ...config.configUtils import DIR_ROOT as BASE_DIR_ROOT
    return clientApi.RegisterSystem(CONSOLE_MOD_MOD_NAME, CONSOLE_MOD_CLIENT_SYSTEM_NAME,
                                    BASE_DIR_ROOT + '.library.consoleMod.system.client.client.Main')


def Listen(funcOrStr=None, namespace=clientApi.GetEngineNamespace(), systemName=clientApi.GetEngineSystemName(),
           priority=0):
    clientSystem = clientApi.GetSystem(CONSOLE_MOD_MOD_NAME, CONSOLE_MOD_CLIENT_SYSTEM_NAME)  # type: Main

    def wrapper(func):
        clientSystem.eventList.append(
            (namespace, systemName, funcOrStr if isinstance(funcOrStr, str) else func.__name__, func, priority))
        return func

    return wrapper(funcOrStr) if callable(funcOrStr) else wrapper
