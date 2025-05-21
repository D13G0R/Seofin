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

class Entradas(BaseModel):
    origen : str
    fecha : datetime
    cantidad : float
    detalle : Optional[str]
    fk_cuenta_id : int
    
class ActualizarEntrada(BaseModel):
    origen : Optional[str] = None
    fecha : Optional[datetime] = None
    cantidad : Optional[float] = None
    detalle : Optional[str] = None
    fk_cuenta_id : Optional[int] = None

class Salidas(BaseModel):
    categoria : str
    descripcion : str
    cantidad : float
    fecha : datetime
    detalle : Optional[str]
    fk_cuenta_id : int