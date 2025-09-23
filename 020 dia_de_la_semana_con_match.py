dia = input("Dame un dia de la semana: lunes,martes,miercoles,jueves,viernes,sabado,domingo: ")

match dia:
    case "sabado" | "domingo":
        print("Es dia festivo")
         
    case  "lunes" | "martes" | "miercoles" | "jueves" | "viernes" | "sabado" | "domingo":
          print("Es dia raboral")  
       # _ es como el resto   
    case _:
        print("No es lo que tienes que poner cabezon")