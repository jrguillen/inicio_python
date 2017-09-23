# Programa basico de claificaciones

try:
	cal_alum = float(raw_input('Igrese la calificacion de alumno>>> '))
	if cal_alum >= 0.9 and cal_alum <= 1:
		print cal_alum,'claificacion Sobresaliente'
	elif cal_alum >= 0.8 and cal_alum < 0.9:
		print cal_alum,'calificacion Notable'
	elif cal_alum >= 0.7 and cal_alum < 0.8:
		print cal_alum,'claificacion Buena'
	elif cal_alum >= 0.6 and cal_alum < 0.7:
		print cal_alum,'claificacion Suficiente'
	elif cal_alum < 0.6:
		print cal_alum,'calificacion Insufisiente'
	else:
		print '<<<la calificacion esta fuera de rango establecido (0.0 y 1.0)>>>'
except:
	print'<<<Solo puede ingrasar valores numericos entre 0.0 y 1.0>>>'