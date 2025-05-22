from db import getConnection

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