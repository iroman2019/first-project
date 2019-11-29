even_number = 12
even_numbers = [1, 2, 4, 6, 8, 10]
print(even_numbers[2])

name = "John Doe Smith"
print(name[2])

print(even_numbers[2:4])

for number in even_numbers:
    print("Következő szám")
    print(number)

name_parts = name.split(" ")
print(name_parts)
print(name_parts[1])

for name_part in name_parts:
    print(name_part)

for i in range(1,6):
    print("Román Ildikó" + str(i))

animals = ['dog', 'cat']
print(animals)
animals[0] = 'bagoly'
print(animals)
animals_tuple = ('dog', 'cat')
print(animals_tuple)
#animals_tuple[0] = 'bagoly'
print(animals_tuple)
city = ['Budapest', 23.0, 56.5, False]
print(city)
for part in city:
    print(part)
