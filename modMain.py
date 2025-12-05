# -*- coding: utf-8 -*-

from mod.common.mod import Mod

from .config.configUtils import *


@Mod.Binding(name=MOD_NAME, version=VERSION)
class Main(object):
    @staticmethod
    def LoadServerModule():
        """
        加载服务端模块 import该模块即可加载
        """
        from .system.server import server

    @staticmethod
    def LoadClientModule():
        """
        加载客户端模块 import该模块即可加载
        """
        from .system.client import client

    @Mod.InitServer()
    def ServerInit(self):
        from .library.consoleMod.serverApi import RegisterConsoleModServer
        # 注册consoleMod服务端系统
        serverSystem = RegisterConsoleModServer()
        # 加载服务端模块 将监听数据存入服务端系统实例里
        self.LoadServerModule()
        # 加载完成 调用初始化监听器
        serverSystem.InitialListener()

    @Mod.DestroyServer()
    def ServerDestroy(self):
        pass

    @Mod.InitClient()
    def ClientInit(self):
        # 注释同上
        from .library.consoleMod.clientApi import RegisterConsoleModClient
        clientSystem = RegisterConsoleModClient()
        self.LoadClientModule()
        clientSystem.InitialListener()

    @Mod.DestroyClient()
    def ClientDestroy(self):
        pass
