from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Cuentas(BaseModel):
    nombre : str
    entrada_total : float
    salida_total : float
    saldo_total : float
    fk_usuario_id : int
    contrasena : str

class ActualizarNombreCuenta(BaseModel):
    nombre: str

class ActualizarContrasenaCuenta(BaseModel):
    contrasena : str



