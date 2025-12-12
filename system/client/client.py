# -*- coding: utf-8 -*-
from ...config.configUtils import *
from ...library.consoleMod.config.configUtils import *
from ...constant.clientConstant import *
from ...library.consoleMod.clientApi import *

clientSystem = clientApi.GetSystem(CONSOLE_MOD_MOD_NAME, CONSOLE_MOD_CLIENT_SYSTEM_NAME)

NotifyToServer = clientSystem.NotifyToServer
CreateEngineSfx = clientSystem.CreateEngineSfx
CreateEngineSfxFromEditor = clientSystem.CreateEngineSfxFromEditor
CreateEngineParticle = clientSystem.CreateEngineParticle
CreateEngineEffectBind = clientSystem.CreateEngineEffectBind
DestroyEntity = clientSystem.DestroyEntity
CreateClientEntityByTypeStr = clientSystem.CreateClientEntityByTypeStr
DestroyClientEntity = clientSystem.DestroyClientEntity
BroadcastEvent = clientSystem.BroadcastEvent
