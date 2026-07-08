import os
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.exc import OperationalError
from dotenv import load_dotenv
from dataclasses import dataclass


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
df_customers = pd.read_csv('customers.csv', delimiter=';')

df_countries.to_sql('bronze_countries', engine, if_exists='append', schema='bronze')
df_cities.to_sql('bronze_cities', engine, if_exists='append', schema='bronze')
df_categories.to_sql('bronze_categories', engine, if_exists='append', schema='bronze')
df_products.to_sql('bronze_products', engine, if_exists='append', schema='bronze')
df_shops.to_sql('bronze_shops', engine, if_exists='append', schema='bronze')
df_employees.to_sql('bronze_employees', engine, if_exists='append', schema = 'bronze')
df_customers.to_sql('bronze_customers', engine, if_exists='append', schema='bronze')

df_sales = pd.read_csv('sales.csv', delimiter=';')
df_sales.to_sql('bronze_sales', engine, if_exists='append', index=False, chunksize=1000, schema = 'bronze')
