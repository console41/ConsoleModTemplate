import mod.client.extraClientApi as clientApi

PLAYER_ID = clientApi.GetLocalPlayerId()
LEVEL_ID = clientApi.GetLevelId()
COMPONENT_FACTORY = clientApi.GetEngineCompFactory()

TimeComp = COMPONENT_FACTORY.CreateTime(LEVEL_ID)
TextNotifyComp = COMPONENT_FACTORY.CreateTextNotifyClient(LEVEL_ID)
ItemComp = COMPONENT_FACTORY.CreateItem(PLAYER_ID)
CustomAudioComp = COMPONENT_FACTORY.CreateCustomAudio(LEVEL_ID)
GameComp = COMPONENT_FACTORY.CreateGame(LEVEL_ID)
OperationComp = COMPONENT_FACTORY.CreateOperation(LEVEL_ID)
EngineTypeComp = COMPONENT_FACTORY.CreateEngineType
TextNotifyClientComp = COMPONENT_FACTORY.CreateTextNotifyClient(LEVEL_ID)
PostProcessComp = COMPONENT_FACTORY.CreatePostProcess(LEVEL_ID)
ConfigClientComp = COMPONENT_FACTORY.CreateConfigClient(LEVEL_ID)

ENUM = clientApi.GetMinecraftEnum()
