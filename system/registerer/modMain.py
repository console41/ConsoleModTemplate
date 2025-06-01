# -*- coding: utf-8 -*-

import mod.client.extraClientApi as clientApi
import mod.server.extraServerApi as serverApi
from mod.common.mod import Mod

from ...config.configUtils import DIR_ROOT, VERSION
from .registererUtils import serverSystems, clientSystems


@Mod.Binding(name=DIR_ROOT, version=VERSION)
class Main(object):
    @Mod.InitServer()
    def ServerInit(self):
        for systemName, namespace, clsPath in serverSystems:
            serverApi.RegisterSystem(namespace, systemName, clsPath)

    @Mod.DestroyServer()
    def ServerDestroy(self):
        pass

    @Mod.InitClient()
    def ClientInit(self):
        for systemName, namespace, clsPath in clientSystems:
            clientApi.RegisterSystem(namespace, systemName, clsPath)

    @Mod.DestroyClient()
    def ClientDestroy(self):
        pass
