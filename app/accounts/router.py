from fastapi import APIRouter
from app.accounts.shemas import Cuentas, ActualizarNombreCuenta, ActualizarContrasenaCuenta, Entradas, ActualizarEntrada, Salidas
from app.accounts.crud import create_account, list_account, update_name, update_password, delete_account, create_entry, list_entry, list_one_entry, update_entry, create_outflows, delete_entry

from typing import Optional
router = APIRouter(prefix = "/accounts", tags = ["Cuentas"])

@router.post("/create")
def createAccount(account : Cuentas):
    data = create_account(account)
    if data:
        return data
    else:
        return "no se devolvieron datos al crear la cuenta."

@router.get("/list")
def listAccount():
    data = list_account()
    
    if data: 
        return data
    else:
        return "no se devolvieron datos para listar cuentas."


@router.patch("/updateNameAccount")
def updateNameAccount(id : int, cuenta : ActualizarNombreCuenta):
    if id and cuenta:
        data = update_name(id, cuenta.nombre)
        if data:
            return data
        else:
            return {"message" : "no se devolvieron datos para listar cuentas."}
    else:
        return {"faltan datos para poder actualizar."}
    
@router.patch("/updatePasswordAccount")
def updatePasswordAccount(id : int, cuenta : ActualizarContrasenaCuenta):
    if id and cuenta:
        data = update_password(id, cuenta.contrasena)
        if data:
            return data
        else:
            return {"message" : "No se devolvieron datos"}
    else:
        return {"message": "Faltan datos para actualizar"}
    
@router.delete("/deleteAccount")
def deleteAccount(id : int):
    id_account = id
    if id_account:
        data = delete_account(id)
        if data:
            return data
        else:
            {"message": "No se devolvieron datos."}




####            ENTRANCES 
@router.post("/newEntry")
def addEntry(entrance : Entradas):
    if entrance:
        data = create_entry(entrance)
        if data:
            return data
        else: 
            {"message" : "No se devolvieron datos."}
    else:
        return {"Message" : "Informacion de entrada incorrecta."}
    
@router.get("/entryList")
def listEntry(id : Optional[int] = None):
    if id is not None:
        data = list_one_entry(id)
    elif id is None:
        data = list_entry()
    
    if data:
        return data
    else:
        return {"message": "No se devolvieron datos."}


@router.put("/updateEntry/")
def updateEntry(id: int, entrance: ActualizarEntrada):
    if id:
        entrance_EXIST = list_one_entry(id)
        if entrance_EXIST is None:
            return {"message": "Registro no encontrado"}

        # Actualizar solo los campos proporcionados
        update_data = entrance.dict()
        print(update_data)
        if update_data:
            result = update_entry(id, update_data)
            return result
        else:
            return {"message": "No se proporcionaron datos para actualizar."}
    else:
        return {"message": "Falta la ID o los datos son incorrectos."}
        
@router.delete("/deleteEntry")
def deleteEntry(id):
    if id:
        data = delete_entry(id)
        if data:
            return data
        else:
            return {"message" : "no se devolvieron datos"}
    else:
        return {"message" : "Falta la id para poder realizar la consulta"}


@router.post("/newExit")
def addExit( outflows: Salidas):
    if outflows:
        data = create_outflows(outflows)
        if data:
            return data
        else: 
            {"message" : "No se devolvieron datos."}
    else:
        return {"Message" : "Informacion de entrada incorrecta."}
    
    