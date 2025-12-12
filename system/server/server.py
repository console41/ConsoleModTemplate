# -*- coding: utf-8 -*-
from ...config.configUtils import *
from ...library.consoleMod.config.configUtils import *
from ...constant.serverConstant import *
from ...library.consoleMod.serverApi import *

serverSystem = serverApi.GetSystem(CONSOLE_MOD_MOD_NAME, CONSOLE_MOD_SERVER_SYSTEM_NAME)

NotifyToClient = serverSystem.NotifyToClient
NotifyToMultiClients = serverSystem.NotifyToMultiClients
BroadcastToAllClient = serverSystem.BroadcastToAllClient
BroadcastEvent = serverSystem.BroadcastEvent
CreateEngineEntityByNBT = serverSystem.CreateEngineEntityByNBT
CreateEngineItemEntity = serverSystem.CreateEngineItemEntity
CreateEngineEntityByTypeStr = serverSystem.CreateEngineEntityByTypeStr
DestroyEntity = serverSystem.DestroyEntity
