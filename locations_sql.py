from mysql.connector import connect

conn = connect(
    host="localhost",
    user="locations",
    passwd="locations",
    database="locations"
)

#cursor = conn.cursor()
#letter = input("Add meg az első betűt: ")
#cursor.execute("select name, lat, lon from locations where name like %s", (letter +"%",))
#for (name, lat, lon) in cursor:
    #print(f"{name} ({lat}, {lon})")
#cursor.close()

cursor = conn.cursor()
cursor.execute("update locations set name = concat(name, 'XXX'), lat = lat + 3 where name='Budapest'")
conn.commit()


def delete_locations():
    cursor = conn.cursor()
    cursor.execute("delete from location_tags")
    cursor.execute("delete from locations")
    conn.commit()
    cursor.close()


def count_locations():
    cursor = conn.cursor()
    cursor.execute("select count('id') from locations")
    count_found = 0
    for (count,) in cursor:
        count_found =count
    cursor.close()
    return count_found


def insert_location(name, coords):
    parts_of_coords = coords.split(",")
    lat = float(parts_of_coords[0])
    lon = float(parts_of_coords[1])
    cursor =conn.cursor()
    cursor.execute("INSERT INTO locations(name, lat, lon) VALUES (%s, %s, %s);", (name, lat, lon))
    conn.commit()
    cursor.close()

def find_location_by_name(name):
    location_found = None
    #location_found = []
    cursor = conn.cursor()
    cursor.execute("select name, lat, lon from locations where name = %s", (name, ))
    for (name, lat, lon) in cursor:
        location_found = (name, lat, lon)
        #location_found = {""
        #location_found.append((name, lat, lon))
    return location_found

def assert_location_exists(name, coords):
    parts = coords.split(",")
    lat = float(parts[0])
    lon = float(parts[1])
    location_found = find_location_by_name(name)
    assert location_found is not None
    print(location_found[1])
    assert lat == location_found[1]
    assert lon == location_found[2]


#delete_locations()
#insert_location('Pécs', "11,13.02")
#print(count_locations())
print(find_location_by_name("Piripócs"))
print(find_location_by_name("Paks"))
print(find_location_by_name("Pécs"))
assert_location_exists("Pécs", "11,13.02")
