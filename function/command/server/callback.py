# -*- coding: utf-8 -*-

commandDict = {}


def AddCommandCallback(commandName):
    def wrapper(func):
        commandDict[commandName if isinstance(commandName, str) else func.__name__] = func
        return func

    return wrapper(commandName) if callable(commandName) else wrapper
