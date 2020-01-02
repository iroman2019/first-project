from mysql.connector import connect


class DbOperation:

    def delete_locations(self):
        conn = connect(
            host="localhost",
            user="locations",
            passwd="locations",
            database="locations"
        )

        cursor = conn.cursor()
        cursor.execute("delete from location_tags")
        cursor.execute("delete from locations")
        conn.commit()
        cursor.close()
        conn.close()