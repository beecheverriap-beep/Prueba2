medicamentos = 60000
despacho = 8000
edad = int(input("Ingrese la edad del paciente: "))
tramo = input("Ingrese el tramo (A, B, C o D): ").upper()

descuento_medicamento = 0.0
descuento_despacho = 0.0


if edad <= 30:
        if tramo in ["A", "B"]:
            descuento_medicamento = 0.18
elif tramo in ["C", "D"]:
        descuento_medicamento = 0.12
elif 31 <= edad <= 60:
        if tramo in ["A", "B"]:
            descuento_medicamento = 0.12
elif tramo in ["C", "D"]:
        descuento_medicamento = 0.08
else:
        descuento_medicamento = 0.0

if tramo in ["A", "B"]:
        descuento_despacho += 0.10 
if edad >= 55:
        descuento_despacho += 0.05 

valor_finalmedicamento = int(medicamentos * (1 - descuento_medicamento ))
valor_finaldespacho = int(despacho * (1 - descuento_despacho))

print(f"El valor de medicamentos es: {valor_finalmedicamento}")
print(f"El valor del despacho es: {valor_finaldespacho}")
