from fastapi import APIRouter
from db import getConnection


#Listar todos los usuarios
def list_user():
    try:
        conn = getConnection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM usuarios")

        results = cursor.fetchall()

        users = []
        for user in results:
            users.append(
                {
                    "id" : user[0],
                    "nombre" : user[1],
                    "apellido" : user[2],
                    "contrasena" : user[5]
                })
        
        return {"users" : users}
    except Exception as e:
        return {"Message" : "Hubo un error del lado de la consulta" + e}
    finally:
        cursor.close()
        conn.close()
        

#Crear un usuario
def create_user(user):
    try:
        conn = getConnection()
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO usuarios(nombre, apellido, numero_identidad, correo, contrasena, contrasena_cuenta)
                    VALUES(%s, %s, %s, %s, %s, %s)""", (
                        user.nombre,
                        user.apellido,
                        user.numero_identidad,
                        user.correo,
                        user.contrasena,
                        user.contrasena_cuenta
                        ))
        conn.commit()

        if cursor.rowcount == 1:
            return {"message": "Usuario creado correctamente"}
        else:
            return {"message": "Error en la consulta de creacion"}

    except Exception as e:
        return {"message Error" :  str(e)}

    finally:
        cursor.close()
        conn.close()

#Actualizar todos los datos excepto las contraseñas
def update_basic_data(user,  id):
    try:
        conn = getConnection()
        cursor = conn.cursor()
        cursor.execute(""" UPDATE usuarios SET nombre = %s, apellido = %s, numero_identidad = %s, correo = %s WHERE id = %s """,
                    (user.nombre, user.apellido, user.numero_identidad, user.correo, id)
        )
        conn.commit()
        if cursor.rowcount == 1:
            return {"message": "Datos basicos actualizados correctamente"}
        else:
            return {"message": "Error en la consulta de actualizacion"}
    except Exception as e:
        return {"message" : str(e)}
    finally:
        cursor.close()
        conn.close()

def update_password(password, id : int):
    try:
        conn = getConnection()
        cursor = conn.cursor()
        cursor.execute("""UPDATE usuarios SET contrasena = %s WHERE id = %s""", (password, id))
        conn.commit()

        if cursor.rowcount == 1:
            return {"message": "Datos basicos actualizados correctamente"}
        else:
            return {"message": "Error en la consulta de actualizacion"}
        
    except Exception as e:
        return {"message" : str(e)} 
    finally:
        cursor.close()
        conn.close()


def delete_user(id):
    try:
        conn = getConnection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM usuarios WHERE id = %s", (id,))

        conn.commit()

        if cursor.rowcount == 1:
            return {"message": "Usuario eliminado correctamente."}
        else:
            return {"message" : "Error al borrar un usuario."}
        
    except Exception as e:
        return {"message exception" : str(e)}

    finally:
        cursor.close()
        conn.close()