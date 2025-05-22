from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Salidas(BaseModel):
    categoria : str
    descripcion : str
    cantidad : float
    fecha : datetime
    detalle : Optional[str]
    fk_cuenta_id : int