# Escribe un programa para pedirle al usuario el numero de horas y
# la tarifa por hora para calcular el salario bruto.

num_horas = float(raw_input('Ingrese las horas trabajas>>> '))
tarifa_horas = float(raw_input('Ingrese el costo de la hora trabajada>>> '))

salario_neto = num_horas * tarifa_horas

print 'El salario neto a cobrar es:',salario_neto