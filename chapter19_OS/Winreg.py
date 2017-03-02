# 윈도우 레지스트리 다루는 모듈
import winreg

with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "Software\\Python\\PythonCore") as key:
    pass


