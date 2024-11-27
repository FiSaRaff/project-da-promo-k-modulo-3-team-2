from src import soporte as sp
from src import variables as va
#from src import soporte_queries_creacion_BDD as query
#from src import bdd_soporte as bdd
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
df.columns = ['employee_number','attrition','job_level', 'job_role','department','monthly_income','salary','percent_salary_hike','training_times_last_year','stock_option_level','hourly_rate','daily_rate','monthly_rate','standard_hours','overtime','business_travel','distance_from_home','remote_work','environment_satisfaction','job_involvement','job_satisfaction','satisfaction', 'performance_rating','relationship_satisfaction','work_life_balance','date_birth','age','gender','marital_status','education', 'education_field','num_companies_worked','total_working_years','years_at_company','years_in_current_role','years_since_last_promotion','years_with_curr_manager']


print("guardar csv con cambios hechos")
df.to_csv("data/hr_raw_data_definitivo.csv")
