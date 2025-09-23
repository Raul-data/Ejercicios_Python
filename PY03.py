pi = 3.1416

# ---------------- CUADRADO ----------------
print("Ahora el CUADRADO")
Lado_cuadrado = int(input("Dime el lado del cuadrado: "))
area_cuadrado = Lado_cuadrado * Lado_cuadrado
perimetro_cuadrado = 4 * Lado_cuadrado

print(f"cuadrado: area = {area_cuadrado} perimetro = {perimetro_cuadrado}")

# ---------------- RECTÁNGULO ----------------
print("Ahora el RECTÁNGULO")
base = int(input("Dime la base: "))
altura = int(input("Dime la altura: "))
area_rect = base * altura
perimetro_rect = 2 * (base + altura)

print(f"Rectángulo: Área = {area_rect} Perímetro = {perimetro_rect}")

# ---------------- TRIÁNGULO ----------------
print("Ahora el TRIÁNGULO")
base = int(input("Dime la base: "))
altura = int(input("Dime la altura: "))
l1 = l2 = l3 = int(input("Dime el lado: "))
area_tri = (base * altura) / 2
perimetro_tri = l1 + l2 + l3

print(f"Triángulo: Área = {area_tri} Perímetro = {perimetro_tri}")
# ---------------- ROMBO ----------------
print("Ahora el ROMBO")
D = int(input("Dime la dioganal mayor: "))
d = int(input("Dime la dioganal menor: "))
lado = 5
area_rombo = (D * d) / 2
perimetro_rombo = 4 * lado

print(f"Rombo: Área = {area_rombo} Perímetro = {perimetro_rombo}")
# ---------------- PENTÁGONO ----------------
print("Ahora el PENTÁGONO")
lado = int(input("Dime la lado: "))
apotema = int(input("Dime la apotema: "))
area_pent = (5 * lado * apotema) / 2
perimetro_pent = 5 * lado

print(f"Pentágono: Área = {area_pent} Perímetro = {perimetro_pent}")

# ---------------- HEXÁGONO ----------------
print("Ahora el HEXÁGONO")
lado = int(input("Dime la lado: "))
apotema = int(input("Dime la apotema: "))
area_hex = (6 * lado * apotema) / 2
perimetro_hex = 6 * lado

print(f"Hexágono: Área = {area_hex} Perímetro = {perimetro_hex}")
