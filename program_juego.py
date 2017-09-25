try:
	def jugamos():
		contador = 0
		suma_Valores = 0
		media = 0
		
		while True:
			valor_entreda = raw_input('Engresa un dato>>> ')
			if valor_entreda == 'fin':
				break
			contador = contador + 1
			suma_Valores = int(valor_entreda) + suma_Valores
			media = suma_Valores / contador
		print 'Numero de intentos',contador,'/ Suma de valores introducidos',suma_Valores,'/ media de valores',media
	jugamos()
except:
	print'introduce datos validos'