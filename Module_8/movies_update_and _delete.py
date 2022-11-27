"""
Name: Oscar boateng Acheampong
Date:November 26th, 2022
Assignment No.:Movies: Update & Delete
Github Repo: https://github.com/dboat10/csd-310.git
"""


import mysql.connector


def show_films(cursor, title):
    # This is the method to execute an inner join on all tables, iterate over the dataset and output the results
    # to the terminal window.

    # This block of code initializes the Inner join query to a variable named sql.
    sql = "SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' " \
          "FROM film " \
          "INNER JOIN genre " \
          "ON film.genre_id = genre.genre_id " \
          "INNER JOIN studio " \
          "ON film.studio_id = studio.studio_id "

    cursor.execute(sql)

    # This line of code gets the results from the cursor object
    films = cursor.fetchall()

    print("\n -- {} --".format(title))

    # This loop statement iterates over the film data set and displays the results.
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2],
                                                                                         film[3]))


# This is the entry point of the program, we establish our database connection and do all the manipulations we want to
# do to our database tables in this block of code.
def main():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="@Dadaboat1",
        database="movies"
    )

    cursor = mydb.cursor()

    show_films(cursor, "DISPLAYING FILMS")

    # INSERT STATEMENT
    insert_sql = "INSERT INTO film(film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) " \
                 "VALUES ('Black Panther', '2022', '160', 'Oscar Acheampong', " \
                 "(SELECT studio_id FROM studio WHERE studio_name = 'Universal Pictures')," \
                 "(SELECT genre_id FROM genre WHERE genre_name = 'SciFi') );"
    mydb.commit()
    cursor.execute(insert_sql)
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    # UPDATE STATEMENT
    update_sql = "UPDATE film " \
                 "SET genre_id = (select genre_id from genre where genre_name = 'Horror') " \
                 "WHERE film_name = 'Alien';"
    mydb.commit()
    cursor.execute(update_sql)
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")

    # DELETE STATEMENT
    delete_sql = " DELETE FROM film WHERE film_name = 'Gladiator';"
    mydb.commit()
    cursor.execute(delete_sql)
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")


main()
