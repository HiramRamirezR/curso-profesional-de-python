nombre_completo = input("¿Cual es tu nombre completo?: ")
edad = int(input("¿Cual es tu edad?: "))
estatura = float(input("¿Cual es tu estatura?: "))
autorizacion = input("¿Eres mayor de edad?: (si/no)") == "si"

print(f"Tu nombre es {nombre_completo}, tu edad es {edad}, tu estatura es {estatura} y eres mayor de edad {autorizacion}")