# Print indica que el programa debe mostrar en la pantalla
print("Hello world")
print("Hola esto es Python")

'''
Comentario varias
lineas

'''

# Data types
#String
my_name = "Chompiras"
my_name = 'Chompiras'
print("My name ->", my_name)
print(type(my_name))

#Integer
my_age = 16
print('My age ->', my_age)
print(type(my_age))

# boolean
is_single = True
print(is_single)
print(type(is_single))

# Input. Every input is a string
place_birth = input("Where did you born: ")
print('I born in ->', place_birth)
print(type(place_birth))

# Practice
# Write your code below
name = input('Hello, what is your name?')
print("Nice to meet you", name, ",now I'll ask you for information about you")
age = input('What is your age?')
city = input('Where do you live?')
college = input('What is your college?')
profession = input('What is your profession?')
pet_name = input("What is your name's pet")

print("There once was a person named" + name + "`\n" +
    "who lived in " + city + ". At the age of" + age + "," + name + 
    "went to college at" + " " + college + "." + name + "graduated and went to work as a" + 
    profession + ".Then," + name + " adopted an animal named" + pet_name + ".They both lived happily ever after!")

template = "There once was a person named {} who lived in {}. At the age of {}, {} went to college at {}.\n {} graduated and went to work as a {}.\nThen, {} adopted an animal named {}.\nThey both lived happily ever after!".format(name,city,age,name,college,name,profession,name,pet_name)
template2 = "There once was a person named {name} who lived in {city}. At the age of {age}, {name} went to college at {college}.\n {name} graduated and went to work as a {profession}.\nThen, {name} adopted an animal named {pet_name}.\nThey both lived happily ever after!".format(name,age,city,college,profession,pet_name)

print(template)