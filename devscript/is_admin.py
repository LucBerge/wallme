import ctypes
import os

try:
	is_admin = os.getuid()==0
except AttributeError:
	is_admin = stypes.windll.shell32.IsUserAnAdmin() != 0
print(is_admin)

