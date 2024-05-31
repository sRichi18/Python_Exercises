import mysql.connector

def Conexion_DB():
    mi_conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="universidad")

    return mi_conexion

def Registrar_Alumno(nombre, apellido, carrera, edad):
    mi_db = Conexion_DB()
    mi_cursor = mi_db.cursor()

    sql = """ INSERT INTO estudiantes
                (nombre, apellido, carrera, edad)
                VALUES (%s, %s, %s, %s) """

    valores = (nombre, apellido, carrera, edad)

    try:
        mi_cursor.execute(sql, valores)
    except:
        mi_db.rollback()
        retorno = 1
    else:
        mi_db.commit()
        retorno = 0
    finally:
        mi_db.close()
        return retorno

#resultado = Registrar_Alumno("Carlos", "Rojas", "Programacion", 23)
#print(resultado)

def Listar_Alumnos():
    mi_db = Conexion_DB()
    mi_cursor = mi_db.cursor()

    sql = """ SELECT nombre, apellido, edad
                FROM estudiantes """

    try:
        mi_cursor.execute(sql)
    except:
        mi_db.rollback()
        retorno = 1
    else:
        retorno = []
        for alumno in mi_cursor:
            retorno.append(alumno)
    finally:
        mi_db.close()
        return retorno

#resultado = Listar_Alumnos()
#print(resultado)

def Obtener_Alumno_Id(id_est):
    mi_db = Conexion_DB()
    mi_cursor = mi_db.cursor()

    sql = """ SELECT nombre, apellido, carrera, edad
                FROM estudiantes
                    WHERE estudiante_id = %s """

    valores = (id_est,)

    try:
        mi_cursor.execute(sql, valores)
    except:
        mi_db.rollback()
        retorno = 1
    else:
        retorno = ()
        for alumno in mi_cursor:
            retorno = alumno
    finally:
        mi_db.close()
        return retorno

#resultado = Obtener_Alumno_Id(2)
#print(resultado)


def Actualizar_Carrera_Alumno(carrera, id_est):
    mi_db = Conexion_DB()
    mi_cursor = mi_db.cursor()

    sql = """ UPDATE estudiantes
                SET carrera = %s
                WHERE estudiante_id = %s """

    valores = (carrera, id_est)

    try:
        mi_cursor.execute(sql, valores)
    except:
        mi_db.rollback()
        retorno = 1
    else:
        mi_db.commit()
        retorno = 0
    finally:
        mi_db.close()
        return retorno

#resultado = Actualizar_Carrera_Alumno("Desarrollo Web", 1)
#print(resultado)

def Eliminar_Alumno(id_est):
    mi_db = Conexion_DB()
    mi_cursor = mi_db.cursor()

    sql = """ DELETE FROM estudiantes
                WHERE estudiante_id = %s """

    valores = (id_est,)

    try:
        mi_cursor.execute(sql, valores)
    except:
        mi_db.rollback()
        retorno = 1
    else:
        mi_db.commit()
        retorno = 0
    finally:
        mi_db.close()
        return retorno

#resultado = Eliminar_Alumno(2)
#print(resultado)
