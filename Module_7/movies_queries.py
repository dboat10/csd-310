import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@Dadaboat1",
    database="movies"
)

mycursor = mydb.cursor()
query = "select studio_id, studio_name from studio"
mycursor.execute(query)
print('-- DISPLAYING Studio RECORDS --')

myresult = mycursor.fetchall()

for studio in myresult:
    print("Studio ID: {} \nStudio Name: {}\n".format(studio[0], studio[1]))


query = "select genre_id, genre_name from genre"
mycursor.execute(query)
print('-- DISPLAYING Genre RECORDS --')

myresult = mycursor.fetchall()

for genre in myresult:
    print("Genre ID: {} \nGenre Name: {}\n".format(genre[0], genre[1]))


query = "select film_name, film_runtime from film where film_runtime < 160"
mycursor.execute(query)
print('-- DISPLAYING Short Film RECORDS --')

myresult = mycursor.fetchall()

for film in myresult:
    print("Film Name: {} \nRuntime: {}\n".format(film[0], film[1]))


query = "select film_name, film_director from film Order by film_director"
mycursor.execute(query)
print('-- DISPLAYING Director RECORDS IN ORDER --')

myresult = mycursor.fetchall()

for film in myresult:
    print("Film Name: {} \nDirector: {}\n".format(film[0], film[1]))

mydb.commit()
mydb.close()