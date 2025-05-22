from pydantic import BaseModel
from datetime import datetime
from typing import Optional

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