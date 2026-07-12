import os
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from dotenv import load_dotenv
from dataclasses import dataclass


def validate_and_fix_date(series: pd.Series, default_date='1900-01-01') -> pd.Series:
    try:
        dates = pd.to_datetime(series, errors='coerce', dayfirst=False)
    except Exception:
        dates = pd.to_datetime(series, errors='coerce', dayfirst=True)

    dates = dates.fillna(pd.Timestamp(default_date))
    return dates


def fix_sales_timestamp(df: pd.DataFrame, col='sales_timestamp') -> pd.DataFrame:
    df = df.copy()
    df[col] = pd.to_datetime(df[col], errors='coerce')
    df = df.dropna(subset=[col])
    df[col] = df[col].dt.strftime('%Y-%m-%d %H:%M:%S')
    return df

@dataclass
class DBConfig:
    host: str
    port: int
    dbname: str
    user: str
    password: str

    @property
    def url(self) -> str:
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.dbname}"

load_dotenv()
config = DBConfig(
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

try:
    engine = create_engine(config.url, echo=True)
    with engine.connect() as conn:
        conn.execute("SELECT 1")
except OperationalError as e:
    print(f"Не удалось подключиться к БД: {e}")
except Exception as e:
    print(f"Неизвестная ошибка при создании engine: {e}")

Session = sessionmaker(bind=engine)
session = Session()

df_countries = pd.read_csv('countries.csv', delimiter=';')
df_cities = pd.read_csv('cities.csv', delimiter=';')
df_categories = pd.read_csv('categories.csv', delimiter=';')
df_products = pd.read_csv('products.csv', delimiter=';')
df_shops = pd.read_csv('shops.csv', delimiter=';')
df_employees = pd.read_csv('employees.csv', delimiter=';')
df_employees['hire_date'] = validate_and_fix_date(df_employees['hire_date'])
df_employees['birth_date'] = validate_and_fix_date(df_employees['birth_date'])
df_customers = pd.read_csv('customers.csv', delimiter=';')

df_countries.to_sql('silver_countries', engine, if_exists='append', schema='silver', index=False)
df_cities.to_sql('silver_cities', engine, if_exists='append', schema='silver', index=False)
df_categories.to_sql('silver_categories', engine, if_exists='append', schema='silver', index=False)
df_products.to_sql('silver_products', engine, if_exists='append', schema='silver', index=False)
df_shops.to_sql('silver_shops', engine, if_exists='append', schema='silver', index=False)
df_employees.to_sql('silver_employees', engine, if_exists='append', schema = 'silver', index=False)
df_customers.to_sql('silver_customers', engine, if_exists='append', schema='silver', index=False)

df_sales = pd.read_csv('sales.csv', delimiter=';')
df_sales = fix_sales_timestamp(df_sales)
df_sales.to_sql('silver_sales', engine, if_exists='append', index=False, chunksize=1000, schema = 'silver')


"""
WITH ranked AS (
    SELECT 
        *,
        ROW_NUMBER() OVER (
            PARTITION BY employee_id 
            ORDER BY hire_date DESC, birth_date DESC
        ) AS rn
    FROM silver.silver_employees
)
DELETE FROM silver.silver_employees
WHERE (employee_id, first_name, middle_initial, last_name, birth_date, gender, city_id, shop_id, hire_date) IN (
    SELECT employee_id, first_name, middle_initial, last_name, birth_date, gender, city_id, shop_id, hire_date
    FROM ranked
    WHERE rn > 1
);"""

"""
DELETE FROM silver.silver_employees
WHERE employee_id = NULL;
"""

"""
DELETE FROM silver.silver_employees as e
WHERE NOT EXISTS (
	SELECT *
	FROM silver.silver_sales
	WHERE e.employee_id = silver.silver_sales.employee_id
)
"""

"""
UPDATE silver.silver_sales
SET shop_id = shops.shop_id,
	city_id = cities.city_id
FROM silver.silver_employees
JOIN silver.silver_shops AS shops ON silver.silver_employees.shop_id = shops.shop_id
JOIN silver.silver_cities AS cities ON silver.silver_employees.city_id = cities.city_id
WHERE silver.silver_sales.employee_id = silver.silver_employees.employee_id
"""




