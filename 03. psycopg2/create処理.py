import psycopg2
import csv

conn = psycopg2.connect(
    database="curriculum iRup",
    user="postgres",
    password="cricket25",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

try:
    cur.execute("select exists (select 1 from information_schema.tables where\
                table_name = 'employees')")
    table_exists = cur.fetchone()[0]

    cur.execute("""
        insert into employees(
            employee_id,
            first_name,
            last_name,
            department,
            salary
            )
        values(%s, %s, %s, %s, %s)
    """, (3, 'Alice', 'Smith', 'IT', 55000))

    conn.commit()
    with open('create_result.csv', mode='a', newline='')as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Success"])
    print("新しい従業員が追加されました。")

except psycopg2.DatabaseError as error:
    with open('create_result.csv', mode='a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Failure"])
    print("エラーが発生しました:", error)

finally:
    cur.close()
    conn.close()
