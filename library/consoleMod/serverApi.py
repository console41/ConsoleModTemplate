# -*- coding: utf-8 -*-
import mod.server.extraServerApi as serverApi

from .config.configUtils import *
from .system.server.server import Main


def RegisterConsoleModServer():
    from ...config.configUtils import DIR_ROOT as BASE_DIR_ROOT
    return serverApi.RegisterSystem(CONSOLE_MOD_MOD_NAME, CONSOLE_MOD_SERVER_SYSTEM_NAME,
                                    BASE_DIR_ROOT + '.library.consoleMod.system.server.server.Main')


def Listen(funcOrStr=None, namespace=serverApi.GetEngineNamespace(), systemName=serverApi.GetEngineSystemName(),
           priority=0):
    serverSystem = serverApi.GetSystem(CONSOLE_MOD_MOD_NAME, CONSOLE_MOD_SERVER_SYSTEM_NAME)  # type: Main

    def wrapper(func):
        serverSystem.eventList.append(
            (namespace, systemName, funcOrStr if isinstance(funcOrStr, str) else func.__name__, func, priority))
        return func

    return wrapper(funcOrStr) if callable(funcOrStr) else wrapper
