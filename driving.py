country = input('country?')
age = input('age?')
age = int(age)
if country == 'TW':
	if age >= 18:
		print('apply license')
	else:
		print('no')