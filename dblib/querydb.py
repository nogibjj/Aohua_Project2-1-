from databricks import sql
import os


def querydb(query="SELECT * FROM default.ds_salaries_csv LIMIT 2"):
    with sql.connect(
        server_hostname=os.getenv("DATABRICKS_SERVER_HOSTNAME"),
        http_path=os.getenv("DATABRICKS_HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_TOKEN"),
    ) as connection:

        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()

        for row in result:
            print(row)

    return result

def findsalary(level, number):
    query = "select work_year, experience_level, employment_type, job_title, salary_in_usd FROM default.ds_salaries_csv where experience_level=" + "'" + str(level) + "'" +  " ORDER BY work_year DESC" + " LIMIT " + str(number)
    print("executing-> "+query)
    querydb(query)
