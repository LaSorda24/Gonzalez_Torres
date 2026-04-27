import subprocess
import sys


VERDE = "\033[92m"
ROJO = "\033[91m"
RESET = "\033[0m"


def imprimir_color(texto, color):
    codificacion_salida = sys.stdout.encoding or "utf-8"
    texto_seguro = texto.encode(codificacion_salida, errors="replace").decode(
        codificacion_salida,
        errors="replace",
    )
    print(f"{color}{texto_seguro}{RESET}")


def mostrar_resultado(resultado):
    if resultado.stdout:
        imprimir_color(resultado.stdout, VERDE)

    if resultado.stderr:
        imprimir_color(resultado.stderr, ROJO)


def ejecutar_comando(argumentos):
    encoding = "oem" if sys.platform.startswith("win") else None
    resultado = subprocess.run(
        argumentos,
        capture_output=True,
        encoding=encoding,
        errors="replace",
        text=True,
        shell=False,
    )
    mostrar_resultado(resultado)
    return resultado


def dir_carpeta(ruta):
    return ejecutar_comando(["cmd", "/c", "dir", ruta])


def copiar_archivo(ruta_archivo, ruta_carpeta_destino):
    return ejecutar_comando(["cmd", "/c", "copy", "/Y", ruta_archivo, ruta_carpeta_destino])


def eliminar_archivo(ruta_archivo):
    return ejecutar_comando(["cmd", "/c", "del", "/F", "/Q", ruta_archivo])


def crear_carpeta(ruta):
    return ejecutar_comando(["cmd", "/c", "md", ruta])


def eliminar_carpeta(ruta):
    return ejecutar_comando(["cmd", "/c", "rd", ruta])
