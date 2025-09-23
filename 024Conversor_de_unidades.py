#hacer de metros pedidos al usuario a las demas unidades
num1 = float(input("Dame la cantidad que quieres en metros : "))
unidad = input("Dame la unidad (km, hm, dam, dm, cm, mm: ")

match unidad:
    case "km" :
        print(f"Los metros {num1} son {num1 * 1000} km")
    case "hm" :
        print(f"Los metros {num1} son {num1 * 100} hm")
    case "dam":
        print(f"Los metros {num1} son {num1 * 10} dam")
    case "dm":
        print(f"Los metros {num1} son {num1 / 10} dm")
    case "cm" :
        print(f"Los metros {num1} son {num1 / 100} cm")
    case "mm" :
        print(f"Los metros {num1} son {num1 / 1000} mm")