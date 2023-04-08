"""Скрипт для заполнения данными таблиц в БД Postgres."""

import psycopg2
import csv


with psycopg2.connect(
        host='localhost',
        database='north',
        user='postgres',
        password='Ane4ka18230'
) as conn:
    with conn.cursor() as cur:
        with open("north_data/employees_data.csv") as file:
            i = 1
            reader = csv.reader(file)
            for row in reader:
                if '_' not in row[0]:
                    cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)",
                                (i, row[0], row[1], row[2], row[3], row[4]))
                    i += 1
        with open("north_data/customers_data.csv") as file:
            reader = csv.reader(file)
            for row in reader:
                if '_' not in row[0]:
                    cur.execute("INSERT INTO customers VALUES (%s, %s, %s)",
                                (row[0], row[1], row[2]))
        with open("north_data/orders_data.csv") as file:
            reader = csv.reader(file)
            for row in reader:
                if '_' not in row[0]:
                    cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)",
                                (row[0], row[1], row[2], row[3], row[4]))

conn.close()

