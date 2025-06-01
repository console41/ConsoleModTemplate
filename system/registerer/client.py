# -*- coding: utf-8 -*-

def AddClientSystem(systemName, namespace, clsPath):
    def __wrapper(cls):
        return cls

    clientSystems.append(systemName, namespace, clsPath)
    return __wrapper


clientSystems = []
