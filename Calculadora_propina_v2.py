"""
Nombre del programa: Calculadora_de_Propinas_v2.py
Objetivo: Calcular el pago por persona en una mesa incluyendo propinas e impuestos.
Fecha: 22/06/2026
Programado por: CodePhoca
Modificado por: CodePhoca
Modificacion: Se integro el uso de funciones.

"""

print("==========================================================")
print("========¡Bienvenido a la Calculadora de Propinas!========")
print("==========================================================")

calcular_todo = input("Deseas calcular Cuanto tendrian que pagar cada uno? (Si/No) ").lower()

def calcular_division_cuenta(cuenta_total, porc_propina, total_de_personas, agregar_impuesto ):
    if agregar_impuesto == "si":
        cuenta_total = cuenta_total * 1.18 #En Rep.Dom el impuesto es del 18%
    
    #Se calcula cuanto tendra que dar cada persona.
    monto_propina = cuenta_total * (porc_propina / 100)
    gran_total = cuenta_total + monto_propina
    reparticion_propina = gran_total / total_de_personas
    return reparticion_propina

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
    
    #se llama a la funcion para realiazar las operaciones matematicas.
    pago_individual = calcular_division_cuenta(total_cuenta, Porcentaje_propina, personas_total, agregar_impuesto)
    
    print(f"Cada persona debe pagar {pago_individual} pesos")
    
    calcular_todo = input("Deseas calcular otra vez? (si/no) ").lower()
    
print("¡Gracias por usar la calculadora! Hasta la próxima.")

