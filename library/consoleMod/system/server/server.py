# -*- coding: utf-8 -*-
from ...constant.serverConstant import *

updateFunc = []
destroyFunc = []


class Main(serverApi.GetServerSystemCls()):
    def __init__(self, namespace, systemName):
        super(Main, self).__init__(namespace, systemName)
        self.eventList = []

    @staticmethod
    def Update():
        for func in updateFunc:
            func()

    @staticmethod
    def Destroy():
        for func in destroyFunc:
            func()
