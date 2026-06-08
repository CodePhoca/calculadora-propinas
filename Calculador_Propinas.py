"""
Nombre del programa: Calculadora de Propinas Pro
Objetivo: Calcular el pago por persona en una mesa incluyendo propinas e impuestos.
Fecha: 08/06/2026
Programado por: PhocaDev
Modificado por: PhocaDev

"""

print("==========================================================")
print("========¡Bienvenido a la Calculadora de Propinas!========")
print("==========================================================")

calcular_todo = input("Deseas calcular Cuanto tendrian que pagar cada uno? (Si/No) ").lower()

while calcular_todo == "si":
    #Se usan las exepciones try-except por si el usuario coloca letras en vez de numeros.
    try:
        total_cuenta = float(input("¿Cuál fue el total de la cuenta? "))
        Porcentaje_propina = int(input("¿Qué porcentaje de propina desean dejar? (Ej. 10, 12, 15 o 20). "))
        personas_total = int(input("¿Entre cuántas personas se va a dividir la cuenta? "))
    except:
        print("Error, Debes introducir numeros.Intente de nuevo")
        continue
    
    agregar_impuesto = input("Quieres agregar el impuesto a la cuenta? (Si/No)").lower()
    
    if agregar_impuesto == "si":
        total_cuenta = total_cuenta * 1.18 #En Rep.Dom el impuesto es del 18%
    
    #Se calcula cuanto tendra que dar cada persona.
    monto_propina = total_cuenta * (Porcentaje_propina / 100)
    gran_total = total_cuenta + monto_propina
    reparticion_propina = gran_total / personas_total
    
    print(f"Cada persona debe pagar {reparticion_propina} pesos")
    
    calcular_todo = input("Deseas calcular otra vez? (si/no) ").lower()
    
print("¡Gracias por usar la calculadora! Hasta la próxima.")

