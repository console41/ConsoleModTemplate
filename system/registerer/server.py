# -*- coding: utf-8 -*-

def AddServerSystem(systemName, namespace, clsPath):
    def __wrapper(cls):
        return cls

    serverSystems.append((systemName, namespace, clsPath))
    return __wrapper


serverSystems = []
