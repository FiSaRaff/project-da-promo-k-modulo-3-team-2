query_creacion_bdd = "CREATE SCHEMA IF NOT EXISTS `human_resources_ABC_corporation`;"

query_creacion_tabla_education_employee_level = """CREATE TABLE IF NOT EXISTS `human_resources_ABC_corporation`.`education_employee_level` (
                                                        education_level INT AUTO_INCREMENT NOT NULL UNIQUE COMMENT 'nivel de estudios',
                                                        education VARCHAR (50) COMMENT 'Level 1 - Basic Education\nLevel 2 - Secondary Education\nLevel 3 - Technical or Vocational Education\nLevel 4 - University Education\nLevel 5 - Graduate Education',
                                                        PRIMARY KEY (education_level));"""

query_creacion_tabla_gender = """CREATE TABLE IF NOT EXISTS `human_resources_ABC_corporation`.`gender`(
                                    id_gender VARCHAR (5) NOT NULL UNIQUE COMMENT 'género',
                                    gender_description VARCHAR (50) COMMENT 'F : Female , M : Male',
                                    PRIMARY KEY (id_gender));"""

query_creacion_tabla_marital_status = """CREATE TABLE IF NOT EXISTS `human_resources_ABC_corporation`.`marital_status` (
                                            id_marital_status INT AUTO_INCREMENT NOT NULL UNIQUE COMMENT 'Estado civil',
                                            marital_status_description VARCHAR (50) COMMENT 'Married, Divorced, Single',
                                            PRIMARY KEY (id_marital_status));"""

query_creacion_tabla_personal_information = """CREATE TABLE IF NOT EXISTS `human_resources_ABC_corporation`.`personal_information` (
                                                id_employee_number INT NOT NULL UNIQUE,
                                                first_name VARCHAR (50),
                                                last_name VARCHAR (50),
                                                birth_date INT,
                                                id_gender VARCHAR (5),
                                                id_marital_status INT,
                                                number_children INT COMMENT 'número de hijos',
                                                education_level INT COMMENT 'nivel de estudios',
                                                education_field VARCHAR (80) COMMENT 'rama educativa',
                                                attrition VARCHAR(45) COMMENT 'Indica si el empleado ha dejado la empresa: Yes, No',
                                                PRIMARY KEY (id_employee_number),
                                                CONSTRAINT fk_personal_information_gender
                                                        FOREIGN KEY (id_gender)
                                                        REFERENCES gender (id_gender)
                                                        ON DELETE CASCADE 
                                                        ON UPDATE CASCADE,
                                                CONSTRAINT fk_personal_information_education_employee_level
                                                        FOREIGN KEY (education_level)
                                                        REFERENCES education_employee_level (education_level)
                                                        ON DELETE CASCADE 
                                                        ON UPDATE CASCADE,
                                                CONSTRAINT fk_personal_information_marital_status
                                                        FOREIGN KEY (id_marital_status)
                                                        REFERENCES marital_status (id_marital_status)
                                                        ON DELETE CASCADE 
                                                        ON UPDATE CASCADE);"""

query_creacion_tabla_work_experience = """CREATE TABLE IF NOT EXISTS `human_resources_ABC_corporation`.`work_experience` (
                                            id_employee_number INT NOT NULL UNIQUE,
                                            num_companies_worked INT COMMENT 'número de empresas en las que ha trabajado',
                                            total_working_years INT COMMENT 'Años de experiencia',
                                            years_at_company INT COMMENT 'Años en la empresa actual',
                                            years_since_las_promotion INT COMMENT 'Años desde la última promocion',
                                            years_in_current_role INT COMMENT 'Años en el puesto actual',
                                            years_with_currmanager INT COMMENT 'Años bajo la supervisión del mismo gerente',
                                            PRIMARY KEY (id_employee_number),
                                            CONSTRAINT fk_work_experience_personal_information
                                                    FOREIGN KEY (id_employee_number)
                                                    REFERENCES personal_information (id_employee_number)
                                                    ON DELETE CASCADE 
                                                    ON UPDATE CASCADE);""" 

query_creacion_tabla_working_conditions = """CREATE TABLE IF NOT EXISTS `human_resources_ABC_corporation`.`working_conditions` (
                                                id_employee_number INT NOT NULL UNIQUE,
                                                standard_hours VARCHAR(45) COMMENT 'jornada de trabajo : Full Time, Part Time',
                                                overtime VARCHAR(45) COMMENT 'Indica si el trabajo hace horas extras: Yes, No',
                                                business_travel VARCHAR(45) COMMENT 'frecuencia de viajes: travel rarely, travel frequently, non travel',
                                                distance_from_home FLOAT COMMENT 'distancia al trabajo ',
                                                remote_work VARCHAR(45) COMMENT 'Posibilidad de trabajar en remoto: Yes, No',
                                                PRIMARY KEY (id_employee_number),
                                                CONSTRAINT fk_working_conditions_personal_information
                                                        FOREIGN KEY (id_employee_number)
                                                        REFERENCES personal_information (id_employee_number)
                                                        ON DELETE CASCADE 
                                                        ON UPDATE CASCADE);"""

query_creacion_tabla_employee_satisfaction = """CREATE TABLE IF NOT EXISTS `human_resources_ABC_corporation`.`employee_satisfaction` (
                                                    id_employee_number INT NOT NULL UNIQUE,
                                                    environment_satisfaction INT COMMENT 'Nivel de satisfacción del empleado: 1-2-3-4',
                                                    job_satisfaction INT COMMENT 'Nivel de satisfacción en el trabajo: 1-2-3-4',
                                                    performance_rating FLOAT COMMENT 'calificación de rendimiento: 3-4',
                                                    relationship_satisfaction INT COMMENT 'Nivel de satisfaccion en las relaciones interpersonales: 1-2-3-4',
                                                    work_life_balance FLOAT COMMENT 'Equilibrio en trabajo y vida personal: 1-2-3-4',
                                                    job_involvement INT COMMENT 'Nivel implicación del empleado con la empresa: 1-2-3-4',
                                                    PRIMARY KEY (id_employee_number),
                                                    CONSTRAINT fk_employee_satisfaction_personal_information
                                                        FOREIGN KEY (id_employee_number)
                                                        REFERENCES personal_information (id_employee_number)
                                                        ON DELETE CASCADE 
                                                        ON UPDATE CASCADE);"""

query_creacion_tabla_jobrole_information = """CREATE TABLE IF NOT EXISTS `human_resources_ABC_corporation`.`jobrole_information` (
                                                id_employee_number INT NOT NULL UNIQUE,
                                                job_level INT COMMENT 'Nivel jerárquico : 1, 2, 3, 4, 5',
                                                job_role VARCHAR(100) COMMENT 'Puesto que ocupa',
                                                department VARCHAR(100) COMMENT 'Departamento',
                                                PRIMARY KEY (id_employee_number),
                                                CONSTRAINT fk_jobrole_information_personal_information
                                                    FOREIGN KEY (id_employee_number)
                                                    REFERENCES personal_information (id_employee_number)
                                                    ON DELETE CASCADE 
                                                    ON UPDATE CASCADE);"""

query_creacion_tabla_salary_information = """CREATE TABLE IF NOT EXISTS `human_resources_ABC_corporation`.`salary_information` (
                                                id_employee_number INT NOT NULL UNIQUE,
                                                monthly_income FLOAT COMMENT 'Ingresos mensuales',
                                                percent_salary_hike INT COMMENT '% de aumento de salario\n',
                                                training_times_last_year INT COMMENT 'nº de veces que recibió captación el año pasado',
                                                stock_option_level INT COMMENT 'nivel de opciones de compra de acciones',
                                                monthly_rate FLOAT COMMENT 'Coste empresarial mensual',
                                                PRIMARY KEY (id_employee_number),
                                                CONSTRAINT fk_salary_information_personal_information
                                                    FOREIGN KEY (id_employee_number)
                                                    REFERENCES personal_information (id_employee_number)
                                                    ON DELETE CASCADE 
                                                    ON UPDATE CASCADE);"""


query_insertar_education_employee_level = "INSERT INTO education_employee_level (education_level, education ) VALUES (%s, %s)"

query_insertar_gender = "INSERT INTO gender (id_gender, gender_description ) VALUES (%s, %s)"

query_insertar_marital_status = "INSERT INTO marital_status (id_marital_status, marital_status_description ) VALUES (%s, %s)"

query_insertar_personal_information = "INSERT INTO personal_information (id_employee_number, first_name, last_name, birth_date, id_gender, id_marital_status, number_children, education_level, education_field, attrition) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

query_insertar_work_experience = "INSERT INTO work_experience (id_employee_number, num_companies_worked, total_working_years, years_at_company, years_since_las_promotion, years_in_current_role, years_with_currmanager) VALUES (%s, %s, %s, %s, %s, %s, %s)"

query_insertar_working_conditions = "INSERT INTO working_conditions (id_employee_number, standard_hours, overtime, business_travel, distance_from_home , remote_work) VALUES (%s, %s, %s, %s, %s, %s)"

query_insertar_employee_satisfaction = "INSERT INTO employee_satisfaction (id_employee_number, environment_satisfaction, job_satisfaction, performance_rating, relationship_satisfaction, work_life_balance, job_involvement) VALUES (%s, %s, %s, %s, %s, %s, %s)"

query_insertar_jobrole_information = "INSERT INTO jobrole_information (id_employee_number, job_level, job_role, department) VALUES (%s, %s, %s, %s)"

query_insertar_salary_information = "INSERT INTO salary_information (id_employee_number,monthly_income, percent_salary_hike, training_times_last_year, stock_option_level, monthly_rate) VALUES (%s, %s, %s, %s, %s, %s)"



