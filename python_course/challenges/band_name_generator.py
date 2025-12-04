print("Welcome to the Band Name Generator.")
city = input("What's the name of the city you grow up in? \n")
print(city)
pet_name = input("What's the name of your pet? \n")
print(pet_name)
print(
    "Your pet name could be "
    + city[0].upper()
    + city[1:]
    + " "
    + pet_name[0].upper()
    + pet_name[1:]
)
