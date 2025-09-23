dia = int(input("dia de cumpleaños: "))
mes = input("Dime el mes: ")
signo = ""
match mes:
    case "enero": 
      if dia <= 19: 
          signo = "Capricornio" 
      else: 
          "Acuario"
    case "febrero":
            if dia <= 18:
                signo = "Acuario"  
            else:
                "Piscis"
    case "marzo":
            if dia <= 20:
                signo = "Piscis" 
            else:
                "Aries"
    case "abril":
            signo = "Aries" 
            if dia <= 19:
                signo = "Aries" 
            else:
                "Tauro"
    case "mayo":
            if dia <= 20:
                signo = "Tauro"
            else:
                "Géminis"
    case "junio":
            if dia <= 20:
                 signo = "Géminis"
            else:
                "Cáncer"
    case "julio":
            if dia <= 22:
                signo = "Cáncer" 
            else:
                "Leo"
    case "agosto":
             if dia <= 22:
                 signo = "Leo"
             else:
                 "Virgo"
    case "septiembre":
             if dia <= 22:
                 signo = "Virgo"
             else:
                 "Libra"
    case "octubre":
             if dia <= 22:
                 signo = "Libra"
             else:
                 "Escorpio"
    case "noviembre":
             if dia <= 21:
                signo = "Escorpio"
             else: 
                 "Sagitario"
    case "diciembre":
             if dia <= 21:
                 signo = "Sagitario"
             else:
                 "Capricornio"
    case _:
        exit()

print(f"Tu signo del zodiaco {signo}")

 
        




# Aries: 21 de marzo – 20 de abril
# Tauro: 21 de abril – 20 de mayo
# Géminis: 21 de mayo – 21 de junio
# Cáncer: 22 de junio – 22 de julio
# Leo: 23 de julio – 23 de agosto
# Virgo: 24 de agosto – 22 de septiembre
# Libra: 23 de septiembre – 23 de octubre
# Escorpio: 24 de octubre – 22 de noviembre
# Sagitario: 23 de noviembre – 21 de diciembre
# Capricornio: 22 de diciembre – 20 de enero
# Acuario: 21 de enero – 19 de febrero
# Piscis: 20 de febrero – 20 de marzo