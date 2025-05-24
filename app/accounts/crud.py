from db import getConnection


def create_account(account):
    try:
        
        conn = getConnection()
        cursor = conn.cursor()

        cursor.execute("""INSERT INTO cuentas(nombre, entrada_total, salida_total, saldo_total, contrasena, fk_usuario_id)
        VALUES(%s,%s,%s,%s,%s,%s)""", (account.nombre, account.entrada_total, account.salida_total, account.saldo_total, account.contrasena, account.fk_usuario_id))
        conn.commit()
        
        if cursor.rowcount == 1:
            return {"message" : "Cuenta creada correctamente"}
        else:
            {"message" : "Error al crear"}
    except Exception as e:
        return {"message": str(e)}
    finally:
        conn.close()
        cursor.close()
    


def list_account():
    try:
        conn = getConnection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cuentas")
        conn.commit()
        data = cursor.fetchall()
        if data: return data
        
    except Exception as e:
        
        return {"message" : str(e)}
    
    finally:
        conn.close()
        cursor.close()

def update_name(id, name):
    try:
        conn = getConnection()
        cursor = conn.cursor()
        cursor.execute("UPDATE cuentas SET nombre = %s WHERE id = %s", (name, id))
        conn.commit()

        if cursor.rowcount == 1:
            return {"message" : "Nombre actualizado correctamente"}
        else:
            {"message" : "Error al actualizar"}
    except Exception as e:
        return {"message": str(e)}
    finally:
        conn.close()
        cursor.close()

def update_password(id, password):
    try:
        conn = getConnection()
        cursor = conn.cursor()
        cursor.execute("UPDATE cuentas SET contrasena = %s WHERE id = %s", (password, id))
        conn.commit()
        if cursor.rowcount == 1:
            return {"message" : "Contraseña actualizada correctamente."}
        else:
            return {"message" : "Hubo un error en la consulta."}
    except Exception as e:
        return {"message": str(e)}
    finally:
        cursor.close()
        conn.close()
    
def delete_account(id):
    try:
        conn = getConnection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM cuentas WHERE id=%s", (id,))
        conn.commit()

        if cursor.rowcount == 1:
            return {"message" : "Cuenta eliminada correctamente."}
        else:
            return {"message" : "Hubo un error en la consulta."}
    except Exception as e:
        return {"message" : str(e)}
    finally:
        cursor.close()
        conn.close()





