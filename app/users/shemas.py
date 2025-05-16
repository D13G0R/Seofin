from datetime import datetime, date
import uuid
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List
from decimal import Decimal

class Usuarios(BaseModel):
    nombre : str
    apellido : str
    numero_identidad : str
    correo : str
    contrasena : str
    contrasena_cuenta : str

class actualizarUsuario(BaseModel):
    nombre : Optional[str]
    apellido : Optional[str]
    numero_identidad : Optional[str]
    correo : Optional[str]
    
class ActualizarContrasenaUsuario(BaseModel):
    contrasena : str


class Deudas (BaseModel):
    id : int
    fk_usuario_id : int
    fecha_prestamo : datetime
    fecha_pago : datetime
    detalle : Optional[str]

