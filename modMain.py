# -*- coding: utf-8 -*-

import mod.client.extraClientApi as clientApi
import mod.server.extraServerApi as serverApi
from mod.common.mod import Mod

from ...config.configUtils import *

serverSystems = []
clientSystems = []


def AddServerSystem(namespace, systemName, clsPath):
    serverSystems.append((namespace, systemName, clsPath))


def AddClientSystem(namespace, systemName, clsPath):
    clientSystems.append((namespace, systemName, clsPath))


# 注册系统
AddClientSystem(MOD_NAME, MOD_NAME + '.clientSystem', DIR_ROOT + '.system.client.client.Main')
AddServerSystem(MOD_NAME, MOD_NAME + '.serverSystem', DIR_ROOT + '.system.server.server.Main')


@Mod.Binding(name=DIR_ROOT, version=VERSION)
class Main(object):
    @Mod.InitServer()
    def ServerInit(self):
        for namespace, systemName, clsPath in serverSystems:
            serverApi.RegisterSystem(namespace, systemName, clsPath)

    @Mod.DestroyServer()
    def ServerDestroy(self):
        pass

    @Mod.InitClient()
    def ClientInit(self):
        for namespace, systemName, clsPath in clientSystems:
            clientApi.RegisterSystem(namespace, systemName, clsPath)

    @Mod.DestroyClient()
    def ClientDestroy(self):
        pass
