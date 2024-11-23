from src import soporte as sp
from src import variables as va
import pandas as pd

df = pd.read_csv("../pr_raw_data_prueba.csv", index_col=0)

print("se procede a hacer exploración del dataframe")
sp.exploracion(df)

print("eliminar los 64 duplicados")
df = df.drop_duplicates()

print("se corrige la columna de age")
df["age"] = sp.age(df["datebirth"])

print("se corrigen las columnas cuyos valores tienen ',' en vez de '.' y terminan en $")

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
df['maritalstatus'] = df['maritalstatus'].apply(sp.marital_status)

print("después de preguntar y confirmar los nulos de 2 columnas lo cambiamos por el dato correcto")
sp.fill_null(df, "businesstravel", "non-travel")
sp.fill_null(df, "standardhours", "Full Time")
sp.fill_null(df, "performancerating", "not rated")
sp.fill_null(df, "maritalstatus", "unknown")

print("redondeamos el contenido de las columnas con valores económicos")
for column in va.list_round:
    df[column] = round(df[column], 2)

print("corregimos los departamentos")
sp.assign_departament(df, "jobrole", va.dict_department, "roledepartament")

print("eliminamos las columnas que no dan información, están repetidas o no se necesitan")
for column in va.list_drop:
    sp.drop_column(df,column)

print("renombramos la columna nueva de departamentos")
df.rename(columns={'correct_department': 'department'}, inplace=True)

print("reemplazamos los no data por otro concepto")
sp.replace_nodata(df,"educationfield", "other")
sp.replace_nodata(df,"department", "general")

print("cambiamos el orden de las columnas y el nombre")
df=df[va.new_order]
df.columns = ['employee_number','attrition','job_level', 'job_role','department','monthly_income','salary','percent_salary_hike','training_times_last_year','stock_option_level','hourly_rate','daily_rate','monthly_rate','standard_hours','overtime','business_travel','distance_from_home','remote_work','environment_satisfaction','job_involvement','job_satisfaction','performance_rating','relationship_satisfaction','work_life_balance','date_birth','age','gender','marital_status','education', 'education_field','num_companies_worked','total_working_years','years_at_company','years_since_last_promotion','years_with_curr_manager']

df.to_csv("../pr_raw_data_comprobado.csv")

