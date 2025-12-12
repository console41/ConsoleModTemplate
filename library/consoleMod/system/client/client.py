# -*- coding: utf-8 -*-
from ...constant.clientConstant import *


class Main(clientApi.GetClientSystemCls()):
    def __init__(self, namespace, systemName):
        super(Main, self).__init__(namespace, systemName)
        self.eventList = []

    def InitialListener(self):
        for namespace, systemName, eventName, callback, priority in self.eventList:
            newCallbackName = callback.__name__

            if hasattr(self, newCallbackName):
                num = 0
                while True:
                    num += 1
                    newCallbackName = callback.__name__ + '_' + str(num)
                    if not hasattr(self, newCallbackName):
                        break

            def WrapCallback(func):
                """
                [内部函数]生成回调函数包装 防止闭包延迟绑定的问题
                """

                def wrapper(args):
                    return func(args)

                wrapper.func_name = newCallbackName
                return wrapper

            callbackWrapper = WrapCallback(callback)
            # 设置属性
            setattr(self, newCallbackName, callbackWrapper)
            # 调用原版监听接口
            self.ListenForEvent(namespace, systemName, eventName, self, getattr(self, newCallbackName), priority)
