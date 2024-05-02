import psycopg2
import csv

try:
    conn = psycopg2.connect(
        database="curriculum iRup",
        user="postgres",
        password="cricket25",
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()

    cur.execute("""
        select *
        from employees
        """)

    with open('read_result.csv', 'w', newline='')as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            ['employee_id, first_name, last_name, department, salary']
            )

        for row in cur:
            writer.writerow(row)

    print('Success')

except psycopg2.DatabaseError as error:
    print('Failure:', error)

finally:
    cur.close()
    conn.close()
