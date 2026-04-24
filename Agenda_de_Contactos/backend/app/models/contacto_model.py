from pydantic import BaseModel, EmailStr


# - La librería Enum me servirá para crear una clase categoría como si fuera una lista, así limito
# a que en este campo solo se pueda elegir cualquiera de estos valores.
# - Me ahorro el tener que hacer verificaciones dentro del modelo o incluso crear un modelo, que
# aún así no verificaría las categorías."""
from enum import Enum


class CategoriaLista(str,Enum):
    """Definición de las categorías disponibles"""
    personal = "personal"
    trabajo = "trabajo"
    familia = "familia"    

class ContactoBase(BaseModel):
    """
    Modelo base de un contacto.

    Este modelo contiene los campos que comparten tanto
    el contacto de entrada como el contacto de salida.

    ¿Por qué usar Pydantic?
    Porque FastAPI lo utiliza para:
    - validar datos automáticamente
    - convertir datos al tipo correcto cuando es posible
    - documentar la API de forma automática
    - detectar errores antes de procesar la solicitud

    Campos:
    - nombre: nombre del contacto
    - telefono: número telefónico
    - correo: correo electrónico validado como email
    """
    nombre: str
    telefono: str
    correo: EmailStr
    categoria: CategoriaLista


# Como ContactoCreate y Contacto ya heredan de ContactoModel no considero necesario tener
# que modificarlos.
class ContactoCreate(ContactoBase):
    """
    Modelo para crear un contacto.

    En este caso hereda directamente de ContactoBase
    porque para crear un contacto se requieren exactamente
    esos tres campos.

    No se incluye el id porque normalmente el id
    lo genera el backend.
    """
    pass


class Contacto(ContactoBase):
    """
    Modelo completo de contacto.

    Este ya incluye el id y representa la versión final
    del contacto dentro del sistema.
    """
    id: int