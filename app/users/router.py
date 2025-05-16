from fastapi import APIRouter
from app.users.crud import list_user, create_user, update_basic_data, delete_user, update_password
from app.users.shemas import Usuarios, actualizarUsuario, ActualizarContrasenaUsuario

router = APIRouter(prefix="/users", tags = ["Usuarios"])

@router.get("/list")
def allUser():
    data = list_user()
    if data:
        return data
    else:
        return {"Message" : "No se obtuvieron datos o hubo un error al crear."}


@router.post("/create")
def createUser(user : Usuarios):
    data = create_user(user)
    if data:
        return data
    else:
        return {"Message" : "No se obtuvieron datos o hubo un error al crear."}
    
@router.put("/updateBasics")
def updateUser(user : actualizarUsuario, id : int):
    data = update_basic_data(user, id)
    if data:
        return data
    else:
        return {"Message" : "No se obtuvieron datos o hubo un error al crear."}
        
@router.patch("/updatePassword")
def updatePassword(user : ActualizarContrasenaUsuario, id = int):
    if id and user:
        id_user = id
        password = user.contrasena
        data = update_password(password, id_user)
        if data:
            return data
    else:
        return {"message": "faltan datos para actualizar"}


@router.delete("/delete")
def deleteUser(id : int):
    data = delete_user(id)
    if data:
        return data
    else: 
        {"message": "No se obtuvieron datos del servidor"}