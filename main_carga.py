#%%
from src import soporte_queries_creacion_BDD as query
from src import bdd_soporte as bdd
import pandas as pd
#%%
# Creación de base de datos y tablas
bdd.creacion_bbdd_tablas(query.query_creacion_bdd, 'Mysql.2440')
#%%
bdd.creacion_bbdd_tablas(query.query_creacion_tabla_education_employee_level, 'Mysql.2440', 'human_resources_ABC_corporation')
#%%
bdd.creacion_bbdd_tablas(query.query_creacion_tabla_marital_status, 'Mysql.2440', 'human_resources_ABC_corporation')

#%%
bdd.creacion_bbdd_tablas(query.query_creacion_tabla_gender, 'Mysql.2440', 'human_resources_ABC_corporation')
#%%
bdd.creacion_bbdd_tablas(query.query_creacion_tabla_personal_information, 'Mysql.2440', 'human_resources_ABC_corporation')
#%%
bdd.creacion_bbdd_tablas(query.query_creacion_tabla_work_experience, 'Mysql.2440', 'human_resources_ABC_corporation')
#%%
bdd.creacion_bbdd_tablas(query.query_creacion_tabla_working_conditions, 'Mysql.2440', 'human_resources_ABC_corporation')
#%%
bdd.creacion_bbdd_tablas(query.query_creacion_tabla_employee_satisfaction, 'Mysql.2440', 'human_resources_ABC_corporation')
#%%
bdd.creacion_bbdd_tablas(query.query_creacion_tabla_jobrole_information, 'Mysql.2440', 'human_resources_ABC_corporation')
#%%
bdd.creacion_bbdd_tablas(query.query_creacion_tabla_salary_information, 'Mysql.2440', 'human_resources_ABC_corporation')
#%%
# Lectura del csv para la carga de datos en la BDD
dfcarga = pd.read_csv("data/hr_raw_data_definitivo.csv", index_col=0)

#%%
# Cambiamos Married por 1, Divorced por 2, Single por 3 y convertivos el dato en float
dict_mstatus = {'married':'1', 'divorced':'2', 'single':'3'}
dfcarga['marital_status'] = dfcarga['marital_status'].map(dict_mstatus).astype(float)


#añadimos las columnas nuevas y las que borramos y ahora necesitamos
dfcarga['first_name'] = "unknown"
dfcarga['last_name'] = "unknown"
dfcarga['number_children'] = None
#%%
# Crear las listas de tuplas con la información 

# TABLA education_employee_level
datos_tabla_education_employee_level = [(1,'Basic Education'),(2,'Secondary Education'),(3,'Technical or Vocational Education'),(4,'University Education'),(5,'Graduate Education')]
#%%
# TABLA gender
datos_tabla_gender = [('F','Female'),('M','Male')]
#%%
# TABLA marital_status
datos_tabla_marital_status = [(1,'Married'),(2,'Divorced'),(3,'Single')]
#%%
# TABLA personal_information

datos_tabla_personal_information = list(set(zip(dfcarga['employee_number'].values, dfcarga['first_name'].values, dfcarga['last_name'].values, dfcarga['date_birth'].values, dfcarga['gender'].values, dfcarga['marital_status'].values,dfcarga['number_children'].values, dfcarga['education'].values, dfcarga['education_field'].values, dfcarga['attrition'].values))) 
print(datos_tabla_personal_information)
#%%
nueva_lista_personal_information=[]
for t in datos_tabla_personal_information:
    tupla_consumible= []
    for dato in t:
        try:
            tupla_consumible.append(int(dato))
        except:
            tupla_consumible.append(dato)
    nueva_lista_personal_information.append(tuple(tupla_consumible))
#%%
nueva_lista_personal_information=[]
for t in datos_tabla_personal_information:
    tupla_consumible= []
    for dato in t:
        try:
            tupla_consumible.append(float(dato))
        except:
            tupla_consumible.append(dato)
    nueva_lista_personal_information.append(tuple(tupla_consumible))
nueva_lista_personal_information
#%%
bdd.convertir_float(datos_tabla_personal_information)

#%%
# TABLA work_experience
datos_tabla_work_experience = list(set(zip(dfcarga['employee_number'].values, dfcarga['num_companies_worked'].values, dfcarga['total_working_years'].values, dfcarga['years_at_company'].values, dfcarga['years_since_last_promotion'].values, dfcarga['years_in_current_role'].values,dfcarga['years_with_curr_manager'].values))) 
#%%
datos_tabla_work_experience
#%%
nueva_lista_workexperience=[]
for t in datos_tabla_work_experience:
    tupla_consumible= []
    for dato in t:
        try:
            tupla_consumible.append(int(dato))
        except:
            tupla_consumible.append(dato)
    nueva_lista_workexperience.append(tuple(tupla_consumible))
#%%
nueva_lista_workexperience=[]
for t in datos_tabla_work_experience:
    tupla_consumible= []
    for dato in t:
        try:
            tupla_consumible.append(float(dato))
        except:
            tupla_consumible.append(dato)
    nueva_lista_workexperience.append(tuple(tupla_consumible))
#%%

#%%
# TABLA working_conditions
datos_tabla_working_conditions = list(set(zip(dfcarga['employee_number'].values, dfcarga['standard_hours'].values, dfcarga['overtime'].values, dfcarga['business_travel'].values, dfcarga['distance_from_home'].values, dfcarga['remote_work'].values))) 
#%%
nueva_lista_workconditions=[]
for t in datos_tabla_working_conditions:
    tupla_consumible= []
    for dato in t:
        try:
            tupla_consumible.append(int(dato))
        except:
            tupla_consumible.append(dato)
    nueva_lista_workconditions.append(tuple(tupla_consumible))
#%%
print(nueva_lista_workconditions)
#%%
# TABLA employee_satisfaction
datos_tabla_employee_satisfaction = list(set(zip(dfcarga['employee_number'].values, dfcarga['environment_satisfaction'].values, dfcarga['job_satisfaction'].values, dfcarga['performance_rating'].values, dfcarga['relationship_satisfaction'].values, dfcarga['work_life_balance'].values, dfcarga['job_involvement']))) 
#%%
nueva_lista_satisfaction=[]
for t in datos_tabla_employee_satisfaction:
    tupla_consumible= []
    for dato in t:
        try:
            tupla_consumible.append(int(dato))
        except:
            tupla_consumible.append(dato)
    nueva_lista_satisfaction.append(tuple(tupla_consumible))
#%%
nueva_lista_satisfaction=[]
for t in datos_tabla_employee_satisfaction:
    tupla_consumible= []
    for dato in t:
        try:
            tupla_consumible.append(float(dato))
        except:
            tupla_consumible.append(dato)
    nueva_lista_satisfaction.append(tuple(tupla_consumible))
#%%
# TABLA jobrole_information
datos_tabla_jobrole_information = list(set(zip(dfcarga['employee_number'].values, dfcarga['job_level'].values, dfcarga['job_role'].values, dfcarga['department'].values))) 
#%%
nueva_lista_jobrole=[]
for t in datos_tabla_jobrole_information:
    tupla_consumible= []
    for dato in t:
        try:
            tupla_consumible.append(int(dato))
        except:
            tupla_consumible.append(dato)
    nueva_lista_jobrole.append(tuple(tupla_consumible))
#%%
nueva_lista_jobrole=[]
for t in datos_tabla_jobrole_information:
    tupla_consumible= []
    for dato in t:
        try:
            tupla_consumible.append(float(dato))
        except:
            tupla_consumible.append(dato)
    nueva_lista_jobrole.append(tuple(tupla_consumible))
#%%
# TABLA salary_information
datos_tabla_salary_information = list(set(zip(dfcarga['employee_number'].values, dfcarga['monthly_income'].values, dfcarga['percent_salary_hike'].values, dfcarga['training_times_last_year'].values, dfcarga['stock_option_level'].values, dfcarga['monthly_rate'].values))) 
#%%
nueva_lista_salary=[]
for t in datos_tabla_salary_information:
    tupla_consumible= []
    for dato in t:
        try:
            tupla_consumible.append(float(dato))
        except:
            tupla_consumible.append(dato)
    nueva_lista_salary.append(tuple(tupla_consumible))

# Insertar los datos
#%%
# Insertar datos en TABLA education_employee_level
bdd.insertar_datos(query.query_insertar_education_employee_level, "Mysql.2440", 'human_resources_ABC_corporation', datos_tabla_education_employee_level)

#%%
# Insertar datos en TABLA gender
bdd.insertar_datos(query.query_insertar_gender, "Mysql.2440", 'human_resources_ABC_corporation', datos_tabla_gender)
#%%
# Insertar datos en TABLA marital_status
bdd.insertar_datos(query.query_insertar_marital_status, "Mysql.2440", 'human_resources_ABC_corporation', datos_tabla_marital_status)
#%%
# Insertar datos en TABLA personal_information
bdd.insertar_datos(query.query_insertar_personal_information, "Mysql.2440", 'human_resources_ABC_corporation', nueva_lista_personal_information)
#%%
# Insertar datos en TABLA work_experience
bdd.insertar_datos(query.query_insertar_work_experience, "Mysql.2440", 'human_resources_ABC_corporation', nueva_lista_workexperience)
#%%
# Insertar datos en TABLA working_conditions
bdd.insertar_datos(query.query_insertar_working_conditions, "Mysql.2440", 'human_resources_ABC_corporation', nueva_lista_workconditions)
#%%
# Insertar datos en TABLA employee_satisfaction
bdd.insertar_datos(query.query_insertar_employee_satisfaction, "Mysql.2440", 'human_resources_ABC_corporation', nueva_lista_satisfaction)
#%%
# Insertar datos en TABLA jobrole_information
bdd.insertar_datos(query.query_insertar_jobrole_information, "Mysql.2440", 'human_resources_ABC_corporation', nueva_lista_jobrole)
#%%
# Insertar datos en TABLA salary_information
bdd.insertar_datos(query.query_insertar_salary_information, "Mysql.2440",'human_resources_ABC_corporation', nueva_lista_salary)


# %%
