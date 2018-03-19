###########################
### Abruzzese Alexandre ###
###    19 March 2018    ###
###########################

import cryptocompare as cc

while (1) :
	print('\nAppuyer sur q pour quitter\n')
	print('De quelle cryptomonnaie souhaitez-vous connaître la valeur ?\n')
	print('saisir \'list\' afin de connaître la liste des cryptomonnaies\n')
	prix = input('ou alors merci de saisir la cryptomonnaie souhaité\n\n')

	if (prix == 'list') :
		page = cc.get_coin_list()
		for key in page :
			print(key)

	elif (prix == 'q') :
		print('Au revoir et bonne journée !')
		break

	else :
		val = cc.get_price(prix).get(prix).get('EUR')
		print('\nLa valeur du ' + prix + ' est de : ' + str(val) + ' €')