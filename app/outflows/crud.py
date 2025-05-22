from db import getConnection

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