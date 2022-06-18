import os

output1= None
while output1 != "quitter":
	os.system('cls')
	output1 = input("documents\ntelechargements\nquitter\n\n> ")

	if output1 == "documents":
		output2 = None

		while output2 != "retour":
			os.system('cls')
			output2 = input("ouvrir\nfermer\nexplorer\nretour\n\n> ")
