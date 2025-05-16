from fastapi import APIRouter
from app.accounts.shemas import Cuentas, ActualizarNombreCuenta, ActualizarContrasenaCuenta, Entradas, Salidas
from app.accounts.crud import create_account, list_account, update_name, update_password, delete_account, create_entry, create_outflows


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
    
    