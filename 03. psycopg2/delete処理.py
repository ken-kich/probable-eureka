import psycopg2
import csv

conn_params = {
    "database": "curriculum iRup",
    "user": "postgres",
    "password": "cricket25",
    "host": "localhost",
    "port": "5432"
}

output_file_path = "delete_result.csv"

try:
    conn = psycopg2.connect(**conn_params)
    cur = conn.cursor()

    cur.execute("""
        delete from employees
        where employee_id = %s
    """, (2,))

    with open(output_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Success"])
    print("従業員のデータを削除しました。")

except psycopg2.Error as e:
    with open(output_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Failure"])
    print("エラーが発生しました:", e)

finally:
    cur.close()
    conn.close()
