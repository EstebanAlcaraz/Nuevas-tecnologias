
Nombre = str(input("Cual es el nombre del empleado "))
Nro_hijos = int(input("¿Cuantos hijos tiene? "))
Valor_hora = 1300000 / 188 #El salario minimo dividido entre las horas laborales mensuales (Legales)
Horas_trabajadas = int(input("Cuantas horas trabajo?"))
Valor47horas = Valor_hora * 47
Horas_extras = Horas_trabajadas - 47
incremento_extras = 35
Valor_hora_extra = (Valor_hora * (incremento_extras/ 100)) + Valor_hora
Total_extras = Valor_hora_extra * Horas_extras

Devengado = Valor47horas + Total_extras

if Nro_hijos >= 3:
    subsidio = (Valor_hora * 10) * Nro_hijos
else:
    subsidio = (Valor_hora * 5) * Nro_hijos

Neto_pagar = Devengado + subsidio
print(f" Nombre: {Nombre}")
print(f" Numero de hijos: {Nro_hijos}")
print(f" Bonificacion por hijos {subsidio}")
print(f" Valor hora: {Valor_hora}")
print(f" Horas trabajadas: {Horas_trabajadas}")
print(f" Valor de las horas(47) semana: {Valor47horas}")
print(f" Horas Extras: {Horas_extras}")
print(f" Valor de las horas hextra: {Total_extras}")
print(f" Devengado.Horas Extras + las 47: {Devengado}")
print(f" Neto a pagar: {Neto_pagar}")

#
#EJERCICIO 2
Nombres = str(input("Ingrese el nombre del estudiante: "))
Valor_matricula = int(input("Cual es el valor de la matrícula? "))
Estrato = int(input("Ingrese el estrato: "))

Descuento1 = 40
Descuento2 = 30
Descuento3 = 10

Recargo1 = 10
Recargo2 = 20
Recargo3 = 40

if Estrato == 1:
    Precio_descuento1 = Valor_matricula - (Descuento1 / 100) * Valor_matricula
    print(f"Nombre Estudiante: {Nombres}")
    print(f"Valor matrícula: {Valor_matricula}")
    print(f"Estrato: {Estrato}")
    print(f"Descuento: {Precio_descuento1}")
    print("Recargo: 0")
    print(f"Neto a pagar: {Precio_descuento1}")

elif Estrato == 2:
    Precio_descuento2 = Valor_matricula - (Descuento2 / 100) * Valor_matricula
    print(f"Nombre Estudiante: {Nombres}")
    print(f"Valor matrícula: {Valor_matricula}")
    print(f"Estrato: {Estrato}")
    print(f"Descuento: {Precio_descuento2}")
    print("Recargo: 0")
    print(f"Neto a pagar: {Precio_descuento2}")

elif Estrato == 3:
    Precio_descuento3 = Valor_matricula - (Descuento3 / 100) * Valor_matricula
    print(f"Nombre Estudiante: {Nombres}")
    print(f"Valor matrícula: {Valor_matricula}")
    print(f"Estrato: {Estrato}")
    print(f"Descuento: {Precio_descuento3}")
    print("Recargo: 0")
    print(f"Neto a pagar: {Precio_descuento3}")

elif Estrato == 4:
    Precio_recargo1 = Valor_matricula + (Recargo1 / 100) * Valor_matricula
    print(f"Nombre Estudiante: {Nombres}")
    print(f"Valor matrícula: {Valor_matricula}")
    print(f"Estrato: {Estrato}")
    print("Descuento: 0")
    print(f"Recargo: {Precio_recargo1}")
    print(f"Neto a pagar: {Precio_recargo1}")

elif Estrato == 5:
    Precio_recargo2 = Valor_matricula + (Recargo2 / 100) * Valor_matricula
    print(f"Nombre Estudiante: {Nombres}")
    print(f"Valor matrícula: {Valor_matricula}")
    print(f"Estrato: {Estrato}")
    print("Descuento: 0")
    print(f"Recargo: {Precio_recargo2}")
    print(f"Neto a pagar: {Precio_recargo2}")

elif Estrato == 6:
    Precio_recargo3 = Valor_matricula + (Recargo3 / 100) * Valor_matricula
    print(f"Nombre Estudiante: {Nombres}")
    print(f"Valor matrícula: {Valor_matricula}")
    print(f"Estrato: {Estrato}")
    print("Descuento: 0")
    print(f"Recargo: {Precio_recargo3}")
    print(f"Neto a pagar: {Precio_recargo3}")

else:
    print("El estrato seleccionado no es correcto")





