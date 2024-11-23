import pandas as pd
import numpy as np
from datetime import datetime
from IPython.display import display

def exploracion(dataframe):
    '''
    Realiza una exploración inicial de un DataFrame de pandas proporcionando información 
    sobre los datos nulos, duplicados, tipos de datos, valores únicos y estadísticas descriptivas.

    Esta función imprime un resumen con:
    - El número de filas y columnas del DataFrame.
    - El porcentaje de valores nulos y no nulos por columna.
    - El tipo de dato de cada columna.
    - El número de valores únicos en cada columna.
    - El número total de registros duplicados y su porcentaje respecto al total de filas.
    - Las columnas que contienen datos nulos y las que no contienen datos nulos.
    - Estadísticas descriptivas para las columnas numéricas y categóricas (de tipo 'object').

    Parámetros:
    ----------
    df : pandas.DataFrame
        El DataFrame que se desea explorar.

    Retorna:
    --------
    df_info : pandas.DataFrame
        Un DataFrame con la siguiente información para cada columna:
        - '% nulos': Porcentaje de valores nulos.
        - '% no_nulos': Porcentaje de valores no nulos.
        - 'tipo_dato': Tipo de dato de la columna.
        - 'num_valores_unicos': Número de valores únicos en la columna.'''
    
    df_info = pd.DataFrame()

    df_info["% nulos"] = round(dataframe.isna().sum()/dataframe.shape[0]*100, 2).astype(str)+"%" # type: ignore
    df_info["% no_nulos"] = round(dataframe.notna().sum()/dataframe.shape[0]*100, 2).astype(str)+"%" # type: ignore
    df_info["tipo_dato"] = dataframe.dtypes # type: ignore
    df_info["num_valores_unicos"] = dataframe.nunique() # type: ignore

    print(f"""El DataFrame tiene {dataframe.shape[0]} filas y {dataframe.shape[1]} columnas. # type: ignore # type: ignore # type: ignore # type: ignore # type: ignore # type: ignore # type: ignore # type: ignore # type: ignore # type: ignore
    Tiene {dataframe.duplicated().sum()} datos duplicados, lo que supone un porcentaje de {round(dataframe.duplicated().sum()/dataframe.shape[0], 2)}% de los datos.

    Hay {len(list(df_info[(df_info["% nulos"] != "0.0%")].index))} columnas con datos nulos, y son: 
    {list(df_info[(df_info["% nulos"] != "0.0%")].index)}

    y sin nulos hay {len(list(df_info[(df_info["% nulos"] == "0.0%")].index))} columnas y son: 
    {list(df_info[(df_info["% nulos"] == "0.0%")].index)}


    A continuación tienes un detalle sobre los datos nulos y los tipos y número de datos:""")

    display(df_info.head())

    print("Principales estadísticos de las columnas categóricas:")

    display(dataframe.describe(include="O").T)

    print("Principales estadísticos de las columnas numéricas:")

    display(dataframe.describe(exclude="O").T)

    return df_info

def age(column_birth_year):
    '''
    Calculates the current age based on the year of birth.

    This function takes a year of birth and calculates 
    the age by subtracting the birth year from the current year.

    Parameters:
    -----------
    column_year : int or pandas.Series
        The year of birth, or a column of birth years. It can be a single integer 
        value for a single birth year, or a pandas Series for applying the calculation 
        to multiple values.

    Returns:
    --------
    int or pandas.Series
        The calculated age(s), by subtracting the birth year from the current year. 
        If a single value is passed, the function will return a single age. If a pandas 
        Series is passed, it will return a series of ages corresponding to the birth years.

    Example:
    --------
    # For a single value:
    >>> age(1990)
    34  # If the current year is 2024'''


    column_birth_year = pd.to_numeric(column_birth_year, errors='coerce')
    return column_birth_year.apply(lambda x: datetime.now().year - x)

def replace_dot(column):
    '''
    Converts a string representing a monetary value with commas and a dollar sign into a float.

    This function is intended to process columns of type 'object' where the values are monetary 
    amounts formatted with commas as decimal separators, and a dollar sign ('$') at the end. 
    It performs the following transformations:
    
    - Replaces commas (',') with periods ('.') for correct decimal notation.
    - Removes the dollar sign ('$').
    - Converts the resulting string into a float.

    If the input is not a valid monetary string or cannot be converted, the function returns `np.nan`.

    Args:
        cadena (str): A string representing a monetary value, with commas as decimal separators 
                      and a dollar sign ('$') at the end, e.g., "$1,234.56".

    Returns:
        float: The monetary value as a float, or `np.nan` if the conversion fails or the input is invalid.

    Example:
        >>> replace_dot("$1,234.56")
        1234.56

        >>> replace_dot("Invalid value")
        nan'''
    try:
        # Reemplazar las comas por puntos en la cadena
        return float(column.replace(",", ".").replace("$",""))
    
    except:
        # Si ocurre algún error (por ejemplo, si el argumento no es una cadena)
        return np.nan
    
def clean_satisfaction(valoration):
    '''
    Cleans and standardizes a satisfaction score.

    This function processes a satisfaction score by performing the following:
    - If the value of `valoration` is greater than or equal to 10, it divides it by 10, 
      converts the result to an integer, and returns the integer part of the quotient.
    - If the value of `valoration` is less than 10, it returns the value unchanged.
    
    If the input cannot be processed (for example, due to non-numeric data), the function 
    returns `np.nan` to indicate an invalid or missing value.

    Args:
        valoration (int or float): The satisfaction score. It can be a numeric value 
                                   (either integer or float). The function expects values 
                                   that can be compared with 10.

    Returns:
        int or float or np.nan: 
            - An integer representing the processed satisfaction score if the value is >= 10.
            - The original value if it's less than 10.
            - `np.nan` if the input cannot be processed or is invalid.'''
    try: 
        if valoration >= 10:
            return int(str(valoration/10).split('.')[0])
        else: 
            return valoration
    except:
            return np.nan

def convert_negatives_in_absolute(df, columns):
    '''Converts negative values to their absolute values in specified columns of a DataFrame.

    This function applies the `abs()` method to the specified columns in the DataFrame, 
    which converts any negative values to their corresponding positive values. It does 
    not modify other columns of the DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame containing the data.
        columns (list or str): A list or a string of column names in the DataFrame 
                               whose negative values will be converted to absolute values. 
                               If a single column is provided, it should be a string; 
                               if multiple columns are provided, they should be in a list.

    Returns:
        pandas.DataFrame: The original DataFrame with the specified columns updated 
                           to contain only the absolute values.'''
 
    df[columns] = df[columns].abs()  # Aplica abs() solo a las columnas seleccionadas 
    return df # Llamar a la función, por ejemplo, para convertir las columnas 'A' y 'B'

def lower(column):
    """
    Converts a string to lowercase.

    This function takes a string and converts it to lowercase. 
    If the value is not a string (e.g., if it's `None` or another data type),
    the function returns the string `"no data"` as the default value.

    Parameters:
    -----------
    column : str
        The string to be converted to lowercase.

    Returns:
    --------
    str
        The string in lowercase if the conversion is successful.
        If an error occurs (e.g., if the value is not a string), `"no data"` is returned.
    """
    try:
        return column.lower()
    except:
        return "no data"

def fill_null(df,column, concept): 
    '''
    Fills missing (null) values in a specified column of a DataFrame with a given concept.

    Parameters:
    df (pandas.DataFrame): The DataFrame containing the column to be modified.
    column (str): The name of the column in which null values will be filled.
    concept (scalar): The value to replace the null values with.
    '''
    df[column] = df[column].fillna(concept)
    return 

def marital_status(value):
    
    '''Corrects and standardizes marital status values.

    This function checks if the input marital status value is incorrectly spelled as 'Marreid'.
    If so, it renames it to 'married'. For other values, it converts the input to lowercase.
    If an error occurs during processing, the function returns NaN.

    Parameters:
    value (str or any): The marital status value to be processed. It can be a string or any other data type.

    Returns:
    str or np.nan: Returns the corrected marital status as a string, or NaN if an error occurs.'''

    try:
        if value == 'Marreid':
            return value.rename(columns= {'Marreid': 'married'})
        else:
            return str(value).lower()
    except:
        return np.nan 

def assign_departament(dataframe, rolejob, dict_department, column_roledepartment):
    # Limpiamos la columna 'jobrole' de espacios y le hacemos un lower, ya que no estaba reconociendo las claves y es posible que hubiera algún espacio
    dataframe[rolejob] = dataframe[rolejob].str.strip().str.lower()
    dataframe['correct_department'] = dataframe.apply(lambda fila: dict_department.get(fila[rolejob], fila[column_roledepartment]), axis=1)
    #corregimos departamentos
    dataframe["correct_department"].str.strip("-")
    dataframe['correct_department'] = dataframe['correct_department'].str.replace('manager  -', '').str.strip()
    return

def drop_column (dataframe,column):
    '''Drops a specified column from a pandas DataFrame.

    This function removes a given column from the DataFrame using the `drop()` method, 
    modifying the DataFrame in place. The column to be dropped is passed as an argument.

    Parameters:
    dataframe (pandas.DataFrame): The DataFrame from which the column will be removed.
    column (str): The name of the column to be dropped.

    Returns:
    None: The function modifies the DataFrame in place and does not return anything.'''

    return dataframe.drop([column],axis=1, inplace= True)

def replace_nodata(dataframe,column, value):
    '''
    Replaces occurrences of 'no data' in a specified column of a pandas DataFrame with a given value.

    This function modifies the DataFrame by replacing any instances of the string 'no data' 
    in the specified column with the provided `value`. The operation is performed in place.

    Parameters:
    dataframe (pandas.DataFrame): The DataFrame in which the column will be modified.
    column (str): The name of the column where 'no data' will be replaced.
    value (str, int, float, etc.): The value to replace 'no data' with. This can be any valid value 
                                   depending on the column's data type.

    Returns:
    None: The function modifies the DataFrame in place and does not return anything.'''

    dataframe[column] = dataframe[column].replace("no data", value)
    return