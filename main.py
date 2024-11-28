from src import soporte as sp
from src import variables as va
from src import soporte_queries_creacion_BDD as query
from src import bdd_soporte as bdd
import pandas as pd
import numpy as np

df = pd.read_csv("data/hr_raw_data_final.csv", index_col=0)

print("se procede a hacer exploración del dataframe")
sp.exploracion(df)

print("eliminar los 64 duplicados")
df = df.drop_duplicates()

print("se corrige la columna de age")
df["age"] = sp.age(df["datebirth"])

print("se corrigen las columnas cuyos valores tienen ',' en vez de '.' y terminan en $")

sp.replace_dot_worklikebalance("worklifebalance")
sp.replace_dot_worklikebalance("yearsincurrentrole")

df["yearsincurrentrole"] = df["yearsincurrentrole"].apply(sp.convertir_a_int)

for columna in va.list_column_dot:
     df[columna] = df[columna].apply(sp.replace_dot)

print("se estandarizan los valores de la columna 'remotework'")
df["remotework"] = df["remotework"].map(va.diccionario_remote)

print("se estandariza la columna de satisfacción")
df["environmentsatisfaction"] = df["environmentsatisfaction"].apply(sp.clean_satisfaction)

print("se estandariza la columna de gender")
df["gender"] = df["gender"].map(va.dict_gender)

for col in va.list_column_lower:
    df[col] = df[col].apply(sp.lower)

print("quitamos los negativos de la columna 'distancefromhome")
sp.convert_negatives_in_absolute(df,"distancefromhome")

print("extraemos los salarios que faltan de la columna 'monthlyincome")
df['salary'] = df.apply(lambda row: row['salary'] if row['salary'] > 0 else row['monthlyincome'] * 12, axis = 1)

print("corregimos los monthlyincome de los employeenumber que están mal")
df.loc[df['employeenumber'].isin([1317,1360,1465]), "monthlyincome"]/100

print("extraemos los monthlyincome que faltan de la columna 'salary'")
df['monthlyincome'] = df.apply(lambda row: row['monthlyincome'] if row['monthlyincome'] > 0 else row['salary'] / 12, axis = 1)

print("extraemos los hourlyrate que faltan de la columna 'dailyrate'")
df['hourlyrate'] = df.apply(lambda row: row['dailyrate'] / 8, axis = 1)

print("estandarizamos valores de la columna 'maritalestatus' y conservamos los nulos que tiene")
df['maritalstatus'] = df['maritalstatus'].apply(sp.limpiar_maritalstatus)

print("después de preguntar y confirmar los nulos de 2 columnas lo cambiamos por el dato correcto")
sp.fill_null(df, "businesstravel", "non-travel")
sp.fill_null(df, "standardhours", "Full Time")
sp.fill_null(df, "maritalstatus", "other")

print("redondeamos el contenido de las columnas con valores económicos")
for column in va.list_round:
    df[column] = round(df[column], 2)

print("corregimos los departamentos")
sp.assign_departament(df, "jobrole", va.dict_department, "roledepartament")

print("eliminamos las columnas que no dan información, están repetidas o no se necesitan")
for column in va.list_drop:
    sp.drop_column(df,column)

mediana_worlifebalance = df["worklifebalance"].median()
df["worklifebalance"] = df["worklifebalance"].fillna(mediana_worlifebalance)

print("renombramos la columna nueva de departamentos")
df.rename(columns={'correct_department': 'department'}, inplace=True)

print("reemplazamos los no data por otro concepto")
sp.replace_nodata(df,"educationfield", "other")
sp.replace_nodata(df,"department", "general")

print("creamos columna con satisfacción")
df["satisfaction"] = np.where(df["jobsatisfaction"] < 3, "not satisfied", "satisfied")

print("cambiamos el orden de las columnas y el nombre")
df=df[va.new_order]
df.columns = ['employee_number','attrition','job_level', 'job_role','department','monthly_income','salary','percent_salary_hike','training_times_last_year','stock_option_level','hourly_rate','daily_rate','monthly_rate','standard_hours','overtime','business_travel','distance_from_home','remote_work','environment_satisfaction','job_involvement','job_satisfaction','satisfaction', 'performance_rating','relationship_satisfaction','work_life_balance','date_birth','age','gender','marital_status','number_children', 'education', 'education_field','num_companies_worked','total_working_years','years_at_company','years_in_current_role','years_since_last_promotion','years_with_curr_manager']


print("guardar csv con cambios hechos")
df.to_csv("data/hr_raw_data_definitivo.csv")

print("CREAMOS LA BASE DE DATOS Y TABLAS")
bdd.creacion_bbdd_tablas(query.query_creacion_bdd, 'AlumnaAdalab')
bdd.creacion_bbdd_tablas(query.query_creacion_tabla_education_employee_level, 'AlumnaAdalab', 'human_resources_ABC_corporation')
bdd.creacion_bbdd_tablas(query.query_creacion_tabla_marital_status, 'AlumnaAdalab', 'human_resources_ABC_corporation')
bdd.creacion_bbdd_tablas(query.query_creacion_tabla_gender, 'AlumnaAdalab', 'human_resources_ABC_corporation')
bdd.creacion_bbdd_tablas(query.query_creacion_tabla_personal_information, 'AlumnaAdalab', 'human_resources_ABC_corporation')
bdd.creacion_bbdd_tablas(query.query_creacion_tabla_work_experience, 'AlumnaAdalab', 'human_resources_ABC_corporation')
bdd.creacion_bbdd_tablas(query.query_creacion_tabla_working_conditions, 'AlumnaAdalab', 'human_resources_ABC_corporation')
bdd.creacion_bbdd_tablas(query.query_creacion_tabla_employee_satisfaction, 'AlumnaAdalab', 'human_resources_ABC_corporation')
bdd.creacion_bbdd_tablas(query.query_creacion_tabla_jobrole_information, 'AlumnaAdalab', 'human_resources_ABC_corporation')
bdd.creacion_bbdd_tablas(query.query_creacion_tabla_salary_information, 'AlumnaAdalab', 'human_resources_ABC_corporation')

# Cambiamos Married por 1, Divorced por 2, Single por 3 y convertivos el dato en float
df['marital_status'] = df['marital_status'].map(va.dict_mstatus).astype(float)

#añadimos las columnas nuevas y las que borramos y ahora necesitamos
df['first_name'] = "unknown"
df['last_name'] = "unknown"

# Crear las listas de tuplas con la información 
# TABLA education_employee_level
datos_tabla_education_employee_level = [(1,'Basic Education'),(2,'Secondary Education'),(3,'Technical or Vocational Education'),(4,'University Education'),(5,'Graduate Education')]
# TABLA gender
datos_tabla_gender = [('F','Female'),('M','Male')]
# TABLA marital_status
datos_tabla_marital_status = [(1,'Married'),(2,'Divorced'),(3,'Single')]
# TABLA personal_information
datos_tabla_personal_information = list(set(zip(df['employee_number'].values, df['first_name'].values, df['last_name'].values, df['date_birth'].values, df['gender'].values, df['marital_status'].values,df['number_children'].values, df['education'].values, df['education_field'].values, df['attrition'].values))) 
# TABLA work_experience
datos_tabla_work_experience = list(set(zip(df['employee_number'].values, df['num_companies_worked'].values, df['total_working_years'].values, df['years_at_company'].values, df['years_since_last_promotion'].values, df['years_in_current_role'].values,df['years_with_curr_manager'].values))) 
# TABLA working_conditions
datos_tabla_working_conditions = list(set(zip(df['employee_number'].values, df['standard_hours'].values, df['overtime'].values, df['business_travel'].values, df['distance_from_home'].values, df['remote_work'].values)))
# TABLA employee_satisfaction
datos_tabla_employee_satisfaction = list(set(zip(df['employee_number'].values, df['environment_satisfaction'].values, df['job_satisfaction'].values, df['performance_rating'].values, df['relationship_satisfaction'].values, df['work_life_balance'].values, df['job_involvement'])))
# TABLA jobrole_information
datos_tabla_jobrole_information = list(set(zip(df['employee_number'].values, df['job_level'].values, df['job_role'].values, df['department'].values))) 
# TABLA salary_information
datos_tabla_salary_information = list(set(zip(df['employee_number'].values, df['monthly_income'].values, df['percent_salary_hike'].values, df['training_times_last_year'].values, df['stock_option_level'].values, df['monthly_rate'].values)))

#cambiar a int y float los int64 y float64 de Personal Information
new_datos_tabla_personal_information=[]
for t in datos_tabla_personal_information:
    tupla_consumible= []
    for dato in t:
        try:
            tupla_consumible.append(int(dato))
        except:
            tupla_consumible.append(dato)
    new_datos_tabla_personal_information.append(tuple(tupla_consumible))
new_datos_tabla_personal_information=[]
for t in datos_tabla_personal_information:
    tupla_consumible= []
    for dato in t:
        try:
            tupla_consumible.append(float(dato))
        except:
            tupla_consumible.append(dato)
    new_datos_tabla_personal_information.append(tuple(tupla_consumible))
#cambiar a int y float los int64 y float64 de Work experience
new_datos_tabla_work_experience=[]
for t in datos_tabla_work_experience:
    tupla_consumible= []
    for dato in t:
        try:
            tupla_consumible.append(int(dato))
        except:
            tupla_consumible.append(dato)
    new_datos_tabla_work_experience.append(tuple(tupla_consumible))
new_datos_tabla_work_experience=[]
for t in datos_tabla_work_experience:
    tupla_consumible= []
    for dato in t:
        try:
            tupla_consumible.append(float(dato))
        except:
            tupla_consumible.append(dato)
    new_datos_tabla_work_experience.append(tuple(tupla_consumible))
#cambiar a int los int64 de Working conditions
new_datos_tabla_working_conditions=[]
for t in datos_tabla_working_conditions:
    tupla_consumible= []
    for dato in t:
        try:
            tupla_consumible.append(int(dato))
        except:
            tupla_consumible.append(dato)
    new_datos_tabla_working_conditions.append(tuple(tupla_consumible))
#cambiar a int y float los int64 y float64 de satisfaction
new_datos_tabla_employee_satisfaction=[]
for t in datos_tabla_employee_satisfaction:
    tupla_consumible= []
    for dato in t:
        try:
            tupla_consumible.append(int(dato))
        except:
            tupla_consumible.append(dato)
    new_datos_tabla_employee_satisfaction.append(tuple(tupla_consumible))
new_datos_tabla_employee_satisfaction=[]
for t in datos_tabla_employee_satisfaction:
    tupla_consumible= []
    for dato in t:
        try:
            tupla_consumible.append(float(dato))
        except:
            tupla_consumible.append(dato)
    new_datos_tabla_employee_satisfaction.append(tuple(tupla_consumible))
#cambiar a int y float los int64 y float64 de jobrole
new_datos_tabla_jobrole_information=[]
for t in datos_tabla_jobrole_information:
    tupla_consumible= []
    for dato in t:
        try:
            tupla_consumible.append(int(dato))
        except:
            tupla_consumible.append(dato)
    new_datos_tabla_jobrole_information.append(tuple(tupla_consumible))
new_datos_tabla_jobrole_information=[]
for t in datos_tabla_jobrole_information:
    tupla_consumible= []
    for dato in t:
        try:
            tupla_consumible.append(float(dato))
        except:
            tupla_consumible.append(dato)
    new_datos_tabla_jobrole_information.append(tuple(tupla_consumible))
#cambiar a float los float64 de salary
new_datos_tabla_salary_information=[]
for t in datos_tabla_salary_information:
    tupla_consumible= []
    for dato in t:
        try:
            tupla_consumible.append(float(dato))
        except:
            tupla_consumible.append(dato)
    new_datos_tabla_salary_information.append(tuple(tupla_consumible))

# Insertar los datos
# Insertar datos en TABLA education_employee_level
bdd.insertar_datos(query.query_insertar_education_employee_level, "AlumnaAdalab", 'human_resources_ABC_corporation', datos_tabla_education_employee_level)
# Insertar datos en TABLA gender
bdd.insertar_datos(query.query_insertar_gender, "AlumnaAdalab", 'human_resources_ABC_corporation', datos_tabla_gender)
# Insertar datos en TABLA marital_status
bdd.insertar_datos(query.query_insertar_marital_status, "AlumnaAdalab", 'human_resources_ABC_corporation', datos_tabla_marital_status)
# Insertar datos en TABLA personal_information
bdd.insertar_datos(query.query_insertar_personal_information, "AlumnaAdalab", 'human_resources_ABC_corporation', new_datos_tabla_personal_information)
# Insertar datos en TABLA work_experience
bdd.insertar_datos(query.query_insertar_work_experience, "AlumnaAdalab", 'human_resources_ABC_corporation', new_datos_tabla_work_experience)
# Insertar datos en TABLA working_conditions
bdd.insertar_datos(query.query_insertar_working_conditions, "AlumnaAdalab", 'human_resources_ABC_corporation',  new_datos_tabla_working_conditions)
# Insertar datos en TABLA employee_satisfaction
bdd.insertar_datos(query.query_insertar_employee_satisfaction, "AlumnaAdalab", 'human_resources_ABC_corporation', new_datos_tabla_employee_satisfaction)
# Insertar datos en TABLA jobrole_information
bdd.insertar_datos(query.query_insertar_jobrole_information, "AlumnaAdalab", 'human_resources_ABC_corporation', new_datos_tabla_jobrole_information)
# Insertar datos en TABLA salary_information
bdd.insertar_datos(query.query_insertar_salary_information, "AlumnaAdalab",'human_resources_ABC_corporation', new_datos_tabla_salary_information)
