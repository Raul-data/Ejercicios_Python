# Diseñe un programa que pida una letra al usuario y utilice match para determinar si la letra es una vocal, una consonante o un carácter especial.

letra = input("Dime una letra para decirte si es un vocal, un consonante o un caracter especial: ")

match letra:
    case ("a"|"e"|"i"|"o"|"u"):
        print("Es vocal")
    case ("."|"-"|"/"|"*"|"+"):
        print("Es un caracter especial")
    case _:
        print("Es una consonante")      
            