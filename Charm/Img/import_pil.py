import sys
from _winreg import *

version = sys.version[:3]
install_path = sys.prefix

reg_path = "SOFTWARE\\PYTHON\\Pythoncore\\%s\\" % (version)
install_key = "InstallPath"
python_key = "PythonPath"
python_path = "%s;%s\\Lib\\;%s\\DLLs\\" % (install_path, install_path, install_path)


def RegisterPy():
    try:
        reg = OpenKey(HKEY_CURRENT_USER, reg_path)
    except EnvironmentError as e:
        try:
            reg = CreateKey(HKEY_CURRENT_USER, reg_path)
            SetValue(reg, install_key, REG_SZ, install_path)
            SetValue(reg, python_key, REG_SZ, python_key)
            CloseKey(reg)
        except:
            print("*** Unable to register!")
            return
        print("--- Python, ", version, " is now register!")
        return
    if (QueryValue(reg, install_key) == install_path and
                QueryValue(reg, python_key) == python_path):
        CloseKey(reg)
        print("=== Python ", version, " is already registered!")
        return
    CloseKey(reg)
    print("OK.")


RegisterPy()
