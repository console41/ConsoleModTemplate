# -*- coding: utf-8 -*-
import mod.client.extraClientApi as clientApi


class Main(clientApi.GetClientSystemCls()):
    def __init__(self, namespace, systemName):
        super(Main, self).__init__(namespace, systemName)
        self.eventList = []

    def InitialListener(self):
        for namespace, systemName, eventName, callback, priority in self.eventList:
            # 将原来的回调函数同名赋值给自身 否则无法使用
            # self.原回调函数名 = 原回调函数
            setattr(self, callback.__name__, callback)
            # 调用原版接口监听事件
            self.ListenForEvent(namespace, systemName, eventName, self, getattr(self, callback.__name__), priority)
