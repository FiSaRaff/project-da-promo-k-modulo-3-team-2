from src import soporte_queries_creacion_BDD as query
from src import bdd_soporte as bdd
import pandas as pd

# Creación de base de datos y tablas
bdd.creacion_bbdd_tablas(query.query_creacion_bdd, 'admin')
bdd.creacion_bbdd_tablas(query.query_creacion_tabla_education_employee_level, 'admin', 'human_resources_ABC_corporation')
bdd.creacion_bbdd_tablas(query.query_creacion_tabla_marital_status, 'admin', 'human_resources_ABC_corporation')
bdd.creacion_bbdd_tablas(query.query_creacion_tabla_personal_information, 'admin', 'human_resources_ABC_corporation')
bdd.creacion_bbdd_tablas(query.query_creacion_tabla_work_experience, 'admin', 'human_resources_ABC_corporation')
bdd.creacion_bbdd_tablas(query.query_creacion_tabla_working_conditions, 'admin', 'human_resources_ABC_corporation')
bdd.creacion_bbdd_tablas(query.query_creacion_tabla_employee_satisfaction, 'admin', 'human_resources_ABC_corporation')
bdd.creacion_bbdd_tablas(query.query_creacion_tabla_jobrole_information, 'admin', 'human_resources_ABC_corporation')
bdd.creacion_bbdd_tablas(query.query_creacion_tabla_salary_information, 'admin', 'human_resources_ABC_corporation')

# Lectura del csv para la carga de datos en la BDD
dfcarga = pd.read_csv("data/hr_raw_data_definitivo.csv", index_col=0)
dfcarga.head()

# Cambiamos Married por 1, Divorced por 2, Single por 3 y convertivos el dato en float
dict_mstatus = {'married':'1', 'divorced':'2', 'single':'3'}

#añadimos las columnas nuevas y las que borramos y ahora necesitamos
dfcarga['first_name'] = None
dfcarga['last_name'] = None
dfcarga['number_children'] = None
dfcarga['years_in_current_role'] = None
dfcarga.head(2)

# #%%
# Crear las listas de tuplas con la información 

# TABLA education_employee_level
datos_tabla_education_employee_level = [(1,'Basic Education'),(2,'Secondary Education'),(3,'Technical or Vocational Education'),(4,'University Education'),(5,'Graduate Education')]

# TABLA gender
datos_tabla_gender = [('F','Female'),('M','Male')]

# TABLA marital_status
datos_tabla_marital_status = [(1,'Married'),(2,'Divorced'),(3,'Single')]

# TABLA personal_information
datos_tabla_personal_information = list(set(zip(dfcarga['employee_number'].values, dfcarga['first_name'].values, dfcarga['last_name'].values, dfcarga['date_birth'].values, dfcarga['gender'].values, dfcarga['marital_status'].values,dfcarga['number_children'].values, dfcarga['education'].values, dfcarga['education_field'].values))) 

# TABLA work_experience
datos_tabla_work_experience = list(set(zip(dfcarga['employee_number'].values, dfcarga['num_companies_worked'].values, dfcarga['total_working_years'].values, dfcarga['years_at_company'].values, dfcarga['years_since_last_promotion'].values, dfcarga['years_in_current_role'].values,dfcarga['years_with_curr_manager'].values))) 

# TABLA working_conditions
datos_tabla_working_conditions = list(set(zip(dfcarga['employee_number'].values, dfcarga['standard_hours'].values, dfcarga['overtime'].values, dfcarga['business_travel'].values, dfcarga['distance_from_home'].values, dfcarga['remote_work'].values))) 

# TABLA employee_satisfaction
datos_tabla_employee_satisfaction = list(set(zip(dfcarga['employee_number'].values, dfcarga['environment_satisfaction'].values, dfcarga['job_satisfaction'].values, dfcarga['performance_rating'].values, dfcarga['relationship_satisfaction'].values, dfcarga['work_life_balance'].values, dfcarga['job_involvement'], dfcarga['attrition'].values))) 

# TABLA jobrole_information
datos_tabla_jobrole_information = list(set(zip(dfcarga['employee_number'].values, dfcarga['job_role'].values, dfcarga['department'].values))) 

# TABLA salary_information
datos_tabla_salary_information = list(set(zip(dfcarga['monthly_income'].values, dfcarga['percent_salary_hike'].values, dfcarga['training_times_last_year'].values, dfcarga['stock_option_level'].values, dfcarga['monthly_rate'].values))) 


# Insertar los datos

# Insertar datos en TABLA education_employee_level
bdd.insertar_datos(query.query_insertar_education_employee_level, "admin", "spotify_f", datos_tabla_education_employee_level)

# Insertar datos en TABLA gender
bdd.insertar_datos(query.query_insertar_gender, "admin", "spotify_f", datos_tabla_gender)

# Insertar datos en TABLA marital_status
bdd.insertar_datos(query.query_insertar_marital_status, "admin", "spotify_f", datos_tabla_marital_status)

# Insertar datos en TABLA personal_information
bdd.insertar_datos(query.query_insertar_personal_information, "admin", "spotify_f", datos_tabla_personal_information)

# Insertar datos en TABLA work_experience
bdd.insertar_datos(query.query_insertar_work_experience, "admin", "spotify_f", datos_tabla_work_experience)

# Insertar datos en TABLA working_conditions
bdd.insertar_datos(query.query_insertar_working_conditions, "admin", "spotify_f", datos_tabla_working_conditions)

# Insertar datos en TABLA employee_satisfaction
bdd.insertar_datos(query.query_insertar_employee_satisfaction, "admin", "spotify_f", datos_tabla_employee_satisfaction)

# Insertar datos en TABLA jobrole_information
bdd.insertar_datos(query.query_insertar_jobrole_information, "admin", "spotify_f", datos_tabla_jobrole_information)

# Insertar datos en TABLA salary_information
bdd.insertar_datos(query.query_insertar_salary_information, "admin", "spotify_f", datos_tabla_salary_information)

