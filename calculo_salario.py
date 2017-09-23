# Reescribe el programa del calculo del salario para darle al empleado
# 1.5 veces la tarifa horaria para todas las horas trabajadas que excedan de 40.



try:
	num_horas = float(raw_input('Ingrese las horas trabajas>>> '))
	tarifa_horas = float(raw_input('Ingrese el costo de la hora trabajada>>> '))
	if num_horas > 40:
		horas_extra = num_horas - 40
		tarifa_horas_extra = (tarifa_horas * 1.5) * horas_extra
		salario = 40 * tarifa_horas
		salario_neto = salario + tarifa_horas_extra
		print 'El salario a cobrar es>>>', salario_neto
	else:
		salario_neto = num_horas * tarifa_horas
		print 'El salario neto a cobrar es:',salario_neto
except:
	print '<<< Solo Puedes Ingresar valores numericos>>>'
