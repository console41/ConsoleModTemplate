# -*- coding: utf-8 -*-
from ...config.configUtils import *

import mod.client.extraClientApi as clientApi

screenNode = clientApi.GetScreenNodeCls()

__buttonList = []


def AddButtonTouchEvent(path, param={'isSwallow': True}):
    def __wrapper(func):
        __buttonList.append((path, func.__name__, param))
        return func

    return __wrapper

    
def InitButton(instance):
    for path, callback, param in __buttonList:
        control = instance.GetBaseUIControl(path).asButton()
        control.AddTouchEventParams(param)
        control.SetButtonTouchDownCallback(getattr(instance, callback))

class Main(screenNode):
    def __init__(self, namespace, name, param):
        screenNode.__init__(self, namespace, name, param)
        self.uiNode = None

    def Create(self):
        self.uiNode = clientApi.GetUI(DIR_ROOT, UI_NAME)
        InitButton(self)

    def Destroy(self):
        pass

    def Update(self):
        pass
