import platform
import os
import socket

print("=== REPORTE DEL SISTEMA ===")

print(f"Sistema operativo: {platform.system()}")
print(f"Versión: {platform.version()}")
print(f"Arquitectura: {platform.machine()}")
print(f"Nombre del equipo: {socket.gethostname()}")
print(f"Usuario actual: {os.getlogin()}")
