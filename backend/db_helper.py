import os
from dotenv import load_dotenv

load_dotenv()

host = os.environ.get("DB_HOST")
user = os.environ.get("DB_USER")
password = os.environ.get("DB_PASSWORD")
database = os.environ.get("DB_NAME")





import mysql.connector
from contextlib import contextmanager
import logging

logger = logging.getLogger("db_helper")

logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("server.log")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)





@contextmanager
def get_db_cursor(commit = False):


    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )



    cursor = connection.cursor(dictionary=True)
    yield cursor

    if commit:
        connection.commit()

    cursor.close()
    connection.close()


def fetch_all_records():
    with get_db_cursor() as cursor:
        cursor.execute("SELECT *  FROM expenses;")
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)



def fetch_exp_for_date(expense_date):
    logger.info(f"fetch_exp_for_date called with {expense_date}")
    with get_db_cursor() as cursor:
        query = "SELECT * FROM expenses WHERE expense_date = %s"
        print(f"Executing query : {query} with date : {expense_date}")
        cursor.execute(query,(expense_date,))
        expenses = cursor.fetchall()
        print(f"Query results : {expenses}")
        return expenses




def insert_expenses(expense_date,amount,category,notes):
    logger.info(f"insert_expenses called with {expense_date},amount:{amount},category:{category},notes:{notes}")
    with get_db_cursor(commit = True) as cursor:
        cursor.execute(
            "INSERT INTO expenses (expense_date,amount,category,notes) VALUES (%s,%s,%s,%s)",
            (expense_date, amount, category, notes)

        )

def delete_exp_for_date(expense_date):
    logger.info(f"delete_exp_for_date called with {expense_date}")
    with get_db_cursor(commit = True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s",(expense_date,))

def fetch_expense_summary(start_date,end_date):
    logger.info(f"fetch_exp_summary called with start:{start_date},end:{end_date}")
    with get_db_cursor() as cursor:
        cursor.execute(
            '''SELECT category, SUM(amount) as total
            FROM expenses WHERE expense_date
            BETWEEN %s and %s
            GROUP BY category;''',(start_date,end_date)
        )
        data = cursor.fetchall()
        return data

if __name__ == "__main__":
    expenses = fetch_exp_for_date("2024-08-02")
    print(expenses)
