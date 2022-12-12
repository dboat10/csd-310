import mysql.connector
from mysql.connector import errorcode
from pymysql import err

config = {
    "user": "root",
    "password": "@Dadaboat1",
    "host": "127.0.0.1",
    "database": "outland_adventures",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"],
                                                                                      config["database"]))
    cursor = db.cursor()
    query = "SELECT equipment_id, equipment_name, acquisition_date " \
            "FROM equipment " \
            "WHERE acquisition_date < date_sub(curdate(), interval 5 year);"
    cursor.execute(query)
    results = cursor.fetchall()
    print(" -- DISPLAYING Equipments older than 5 years --")

    for equipment in results:
        print("\nEquipment ID:", equipment[0])
        print("Equipment Name:", equipment[1])
        print("Acquisition Date:", equipment[2])

except mysql.connector as Error:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password is invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The supplied database does not exist")

    else:
        print(err)

finally:
    db.close()
