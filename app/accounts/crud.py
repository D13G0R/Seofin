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

def create_entry(entrance):
    try:
        conn = getConnection()
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO entradas(origen, fk_cuenta_id, fecha, cantidad, detalle) 
                    VALUES(%s, %s, %s, %s, %s)""", (entrance.origen, entrance.fk_cuenta_id, entrance.fecha, entrance.cantidad, entrance.detalle))
        conn.commit()
        
        if cursor.rowcount == 1:
                return {"message" : "Entrada registrada correctamente."}
        else:
            return {"message" : "Hubo un error en la consulta."}
    except Exception as e:
        return {"message" : str(e)}
    finally:
        cursor.close()
        conn.close()

def list_entry():

    try:
        conn = getConnection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM entradas")

        data = cursor.fetchall()  # Llamada correcta al método fetchall

        if data:
            # Convertir tuplas a diccionarios para facilitar la serialización
            columns = [desc[0] for desc in cursor.description]
            entrances = [dict(zip(columns, row)) for row in data]
            return entrances
        else:
            return {"message": "No se encontraron datos"}

    except Exception as e:
        return {"message": str(e)}

    finally:
        cursor.close()
        conn.close()

def list_one_entry(id):
    try:
        conn = getConnection()
        cursor = conn.cursor()
        if id:
            cursor.execute("SELECT * FROM entradas WHERE id_ingreso = %s", (id,))

        data = cursor.fetchall()  # Llamada correcta al método fetchall

        if data:
            # Convertir tuplas a diccionarios para facilitar la serialización
            columns = [desc[0] for desc in cursor.description]
            entrances = [dict(zip(columns, row)) for row in data]
            return entrances
        else:
            return {"message": "No se encontraron datos"}

    except Exception as e:
        return {"message": str(e)}

    finally:
        cursor.close()
        conn.close()

def update_entry(id, entrance):
    try:
        print("Llegó aca")
        conn = getConnection()
        cursor = conn.cursor()
        datos_a_enviar = []
        params_list = []

        for key, value in entrance.items():
            if value is not None:
                datos_a_enviar.append(f"{key}=%s")
                params_list.append(value)
                

        params_list.append(id)
        
        print("\nDATOS A ENVIAR: \n" + ", ".join(datos_a_enviar))
        print("\nPARAMETROS: \n" + str(params_list))


        consulta = f"UPDATE entradas SET {str(", ".join(datos_a_enviar))} WHERE id_ingreso = %s"
        print(consulta)
        cursor.execute(consulta, params_list)
        conn.commit()

        if cursor.rowcount == 1:
            return {"message": "Registro actualizado correctamente."}
        else:
            return {"message": "Hubo un error en la consulta."}
    except Exception as e:
        return {"message": str(e)}
    finally:
        cursor.close()
        conn.close()
    

def delete_entry(id):
    try:
        conn = getConnection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM entradas WHERE id_ingreso=%s", (id,))
        conn.commit()

        if cursor.rowcount == 1:
            return {"message" : "Registro eliminado correctamente."}
        else:
            return {"message" : "Hubo un error en la consulta."}
    except Exception as e:
        return {"message" : str(e)}
    finally:
        cursor.close()
        conn.close()



def create_outflows(outflows):
    try:
        conn = getConnection()
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO salidas(categoria, descripcion, cantidad, fecha, detalle, fk_cuenta_id) 
                    VALUES(%s, %s, %s, %s, %s, %s)""", (outflows.categoria, outflows.descripcion, outflows.cantidad, outflows.fecha, outflows.detalle, outflows.fk_cuenta_id))
        conn.commit()
        if cursor.rowcount == 1:
                return {"message" : "Salida de dinero registrada correctamente."}
        else:
            return {"message" : "Hubo un error en la consulta."}
    except Exception as e:
        return {"message" : str(e)}
    finally:
        cursor.close()
        conn.close()