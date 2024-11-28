# Importar librería para la conexión con MySQL
# -----------------------------------------------------------------------
# Importar librerías para manipulación y análisis de datos
# -----------------------------------------------------------------------
from ast import literal_eval
import pandas as pd

import mysql.connector

def creacion_bbdd_tablas(query, contraseña, nombre_bdd=None):
    """
    Crea tablas en una base de datos MySQL utilizando una consulta SQL proporcionada.

    Esta función se conecta a un servidor MySQL y ejecuta una consulta SQL para crear tablas.
    Si se proporciona un nombre de base de datos, la conexión se realizará a esa base de datos específica.
    De lo contrario, se conectará al servidor sin seleccionar una base de datos.

    Args:
        query (str): La consulta SQL que se ejecutará para crear las tablas.
        contraseña (str): La contraseña del usuario 'root' para autenticar la conexión con el servidor MySQL.
        nombre_bdd (str, opcional): El nombre de la base de datos en la que se ejecutará la consulta. 
                                     Si es None, se conectará al servidor sin seleccionar una base de datos.

    Raises:
        mysql.connector.Error: Si ocurre un error durante la conexión o la ejecución de la consulta,
                               se imprimirá el error junto con su código y estado SQL.

    Returns:
        None: La función no devuelve ningún valor. Imprime el cursor después de ejecutar la consulta
              y cierra la conexión a la base de datos.
    """
    if nombre_bdd is not None:
        cnx = mysql.connector.connect(
            user="root", 
            password=contraseña, 
            host="127.0.0.1"
        )

        mycursor = cnx.cursor()

        try:
            mycursor.execute(query)
            print(mycursor)

        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)
    else:
        cnx = mysql.connector.connect(
            user="root", 
            password=contraseña,
            host="127.0.0.1", 
            database=nombre_bdd
        )

        mycursor = cnx.cursor()

        try:
            mycursor.execute(query)
            print(mycursor)
            cnx.close()

        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)
            cnx.close()

def insertar_datos(query, contraseña, nombre_bdd, lista_tuplas):
    """
    Inserta múltiples registros en una tabla de una base de datos MySQL utilizando una consulta SQL proporcionada.

    Esta función se conecta a un servidor MySQL y ejecuta una consulta SQL para insertar datos en una tabla.
    Utiliza el método `executemany` para insertar múltiples filas a la vez, lo que mejora la eficiencia
    en comparación con la inserción de registros uno por uno.

    Args:
        query (str): La consulta SQL que se utilizará para insertar los datos. Debe contener marcadores de posición
                     para los valores que se insertarán.
        contraseña (str): La contraseña del usuario 'root' para autenticar la conexión con el servidor MySQL.
        nombre_bdd (str): El nombre de la base de datos en la que se ejecutará la consulta.
        lista_tuplas (list of tuple): Una lista de tuplas, donde cada tupla contiene los valores a insertar
                                       en la tabla correspondiente.

    Raises:
        mysql.connector.Error: Si ocurre un error durante la conexión o la ejecución de la consulta,
                               se imprimirá el error junto con su código y estado SQL.

    Returns:
        None: La función no devuelve ningún valor. Imprime el número de registros insertados y cierra
              la conexión a la base de datos.
    """
    cnx = mysql.connector.connect(
        user="root", 
        password=contraseña, 
        host="127.0.0.1", database=nombre_bdd
    )

    mycursor = cnx.cursor()

    try:
        mycursor.executemany(query, lista_tuplas)
        cnx.commit()
        print(mycursor.rowcount, "registro/s insertado/s.")
        cnx.close()

    except mysql.connector.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)
        cnx.close()

def convertir_float(lista_tuplas):
    """
    Convierte los elementos de una lista de tuplas a float cuando sea posible.

    Args:
    - lista_tuplas (list): Una lista que contiene tuplas con elementos que pueden ser convertidos a float.

    Returns:
    - list: Una nueva lista con las mismas tuplas de entrada, pero con los elementos convertidos a float si es posible.
    """
    datos_tabla_caract_def = []
    
    for tupla in lista_tuplas:
        lista_intermedia = []
        for elemento in tupla:
            try:
                lista_intermedia.append(float(elemento))
            except (ValueError, TypeError):  # Si no puede convertir, deja el valor original
                lista_intermedia.append(elemento)
            
        datos_tabla_caract_def.append(tuple(lista_intermedia))
    
    return datos_tabla_caract_def

def convertir_int(lista_tuplas):
    """
    Convierte los elementos de una lista de tuplas a int cuando sea posible.

    Args:
    - lista_tuplas (list): Una lista que contiene tuplas con elementos que pueden ser convertidos a int.

    Returns:
    - list: Una nueva lista con las mismas tuplas de entrada, pero con los elementos convertidos a int si es posible.
    """
    datos_tabla_caract_def = []

    for tupla in lista_tuplas:
        lista_intermedia = []
        for elemento in tupla:
            try:
                lista_intermedia.append(int(elemento))
            except (ValueError, TypeError):  # Si no puede convertir, deja el valor original
                lista_intermedia.append(elemento)
            
        datos_tabla_caract_def.append(tuple(lista_intermedia))
    
    return datos_tabla_caract_def

def int_sql (datos):
    nueva_lista=[]
    for t in datos:
        tupla_consumible= []
        for dato in t:
            try:
                tupla_consumible.append(int(dato))
            except:
                tupla_consumible.append(dato)
        nueva_lista.append(tuple(tupla_consumible))
    return nueva_lista

def float_sql (datos):
    nueva_lista=[]
    for t in datos:
        tupla_consumible= []
        for dato in t:
            try:
                tupla_consumible.append(float(dato))
            except:
                tupla_consumible.append(dato)
        nueva_lista.append(tuple(tupla_consumible))
    return nueva_lista