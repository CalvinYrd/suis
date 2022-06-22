from tkinter import filedialog
import os, colorama, sys, shutil

class UnknownCharacterError(Exception):
	def __init__(self, character, line, _set, file):
		super().__init__(f"The \"{character}\" character is not allowed to be used in this context at line {str(line)} on set n°{str(_set)} in {file}, you can only use these three characters : {'}'} , ¤ , ~. Except you are writing a comment, in which case you can use any character.")

if os.name == 'nt':
	def clear():
		os.system('cls')

else:
	def clear():
		os.system('clear')

clear()

def menu(choices, title="", previousChoices=[]):
	if title:
		title = f'\n{title}\n{colorama.Fore.GREEN}\nFaites <Entrer> pour naviguer entre les différentes options.\nFaites "ok" pour confirmer votre choix.{colorama.Fore.BLACK}\n'

	if previousChoices:
		choices.append("")
		choices.append(f"Retourner vers : {previousChoices[-1]}")
		choices.append("Quitter")

	else:
		choices.append("")
		choices.append("Quitter")

	output, tallestLength = "", 0

	for choice in choices:
		if (len(choice) > tallestLength):
			tallestLength = len(choice)

	while 'ok' not in output.lower().strip():
		for selection in choices:
			if not selection:
				continue

			print(colorama.Back.LIGHTWHITE_EX + colorama.Fore.BLACK)
			clear()

			if os.name == "nt":
				if previousChoices:
					if selection.startswith("Retourner vers : "):
						os.system(f'title "Suis v0.0.1 ◦ By CalvinYrd : {" > ".join(previousChoices)}"')

					else:
						os.system(f'title "Suis v0.0.1 ◦ By CalvinYrd : {" > ".join(previousChoices)} > {selection}"')

				else:
					os.system(f'title "Suis v0.0.1 ◦ By CalvinYrd : {selection}"')

			for line in title.split("\n"):
				print(f"   {line}")

			if previousChoices:
				if selection.startswith("Retourner vers : "):
					print(f'   {colorama.Fore.BLUE}{" > ".join(previousChoices)}{colorama.Fore.BLACK}\n')

				else:
					print(f'   {colorama.Fore.BLUE}{" > ".join(previousChoices)} > {selection}{colorama.Fore.BLACK}\n')

			else:
				print(f'   {colorama.Fore.BLUE}{selection}{colorama.Fore.BLACK}\n')

			for choice in choices:
				if choice == selection:
					print(f"   {colorama.Back.LIGHTGREEN_EX}* {choice}{int((tallestLength - len(choice))) * ' '} {colorama.Back.LIGHTWHITE_EX}")

				else:
					if choice:
						print(f"   - {choice}")

					else:
						print()

			output = input("\n> ")
			if 'ok' in output.lower().strip() and selection:
				if os.name == "nt":
					os.system('title "Suis 0.0.1 | By CalvinYrd"')

				if selection.lower() == "quitter" or selection.lower() == "quit" or selection.lower() == "exit" or selection.lower() == "q":
					print(colorama.Style.RESET_ALL)
					clear()

				return selection

def convertCode(language, lines):
	newLines = []

	for line in lines:
		if language == "python":
			newLines.append(line.split("~~"))

	return newLines

chars = {
	"lower" : {
		2 : {
			1 : "²", 2 : "&", 3 : "é", 4 : '"', 5 : "'", 6 : "(", 7 : "-", 8 : "è", 9 : "_", 10 : "ç", 11 : "à", 12 : ")", 13 : "="
		},
		3 : {
			1 : "\t", 2 : "a", 3 : "z", 4 : "e", 5 : "r", 6 : "t", 7 : "y", 8 : "u", 9 : "i", 10 : "o", 11 : "p", 12 : "^", 13 : "$"
		},
		4 : {
			2 : "q", 3 : "s", 4 : "d", 5 : "f", 6 : "g", 7 : "h", 8 : "j", 9 : "k", 10 : "l", 11 : "m", 12 : "ù", 13 : "*"
		},
		5 : {
			2 : "<", 3 : "w", 4 : "x", 5 : "c", 6 : "v", 7 : "b", 8 : "n", 9 : ",", 10 : ";", 11 : ":", 12 : "!"
		},
		6 : {4 : " "}
	},
	"upper" : {
		2 : {
			2 : "1", 3 : "2", 4 : '3', 5 : "4", 6 : "5", 7 : "6", 8 : "7", 9 : "8", 10 : "9", 11 : "0", 12 : "°", 13 : "+"
		},
		3 : {
			2 : "A", 3 : "Z", 4 : "E", 5 : "R", 6 : "T", 7 : "Y", 8 : "U", 9 : "I", 10 : "O", 11 : "P", 12 : "¨", 13 : "£"
		},
		4 : {
			2 : "Q", 3 : "S", 4 : "D", 5 : "F", 6 : "G", 7 : "H", 8 : "J", 9 : "K", 10 : "L", 11 : "M", 12 : "%", 13 : "µ"
		},
		5 : {
			2 : ">", 3 : "W", 4 : "X", 5 : "C", 6 : "V", 7 : "B", 8 : "N", 9 : "?", 10 : ".", 11 : "/", 12 : "§"
		}
	},
	"altgr" : {
		2 : {
			3 : "~", 4 : "#", 5 : "{", 6 : "[", 7 : "|", 8 : "`", 9 : "\\", 10 : "^", 11 : "@", 12 : "]", 13 : "}"
		},
		3 : {4 : "€", 13 : "¤"}
	}
}

homeTitle = """ ____ ____ ____ ____ _________ ____ ____ ____ ____ ____ 
||S |||U |||I |||S |||       |||0 |||. |||0 |||. |||1 ||
||__|||__|||__|||__|||_______|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|
------------------------------------------------------
  ___         ___      _     _   __   __      _ 
 | _ }_  _   / __|__ _| |_ _{_}_ \ \ / / _ __| |
 | _ \ || | | {__/ _` | \ V / | ' \ V / '_/ _` |
 |___/\_, |  \___\__,_|_|\_/|_|_||_|_||_| \__,_|
	  |__/                                      
------------------------------------------------------"""

menuAccueil = ""
while menuAccueil.lower() != "quitter":
	menuAccueil = menu(["Interpreter", "Convertir", "Afficher le clavier", "Notice d'utilisation"], homeTitle)

	if menuAccueil.lower() == "interpreter":
		menuInterprete = ""
		while "retour" not in menuInterprete.lower():
			menuInterprete = menu(["Interpreter un fichier", "Interpreter un dossier (seuls les fichiers à l'origine du dossiers seront convertis en langage suis)"], homeTitle, [menuAccueil])

			if menuInterprete.lower() == "quitter":
				sys.exit(0)

			elif "interpreter un fichier" in menuInterprete.lower():
				path = filedialog.askopenfile(filetypes = (("Fichiers suis", "*.suis"), ("Tous les fichiers", "*.*")))

				if path and path.name.endswith(".suis"):
					path = path.name

					with open(path, "r", encoding = "utf-8") as sourceFile:
						with open("__exectempfile__.py", "w", encoding = "utf-8") as targetFile:
							input(convertCode("python", sourceFile.readlines()))

					os.remove("__exectempfile__.py")

					# execution

			elif "interpreter un dossier" in menuInterprete.lower():
				path = filedialog.askdirectory()

				if path:
					files = []

					for file in os.listdir(path):
						if os.path.isfile(os.path.join(path, file)):
							files.append(file)

					if os.path.exists("__exectempdir__") and os.path.isdir("__exectempdir__"):
						shutil.rmtree("__exectempdir__")

					shutil.copytree(path, "__exectempdir__")

					for file in files:
						if file.endswith(".suis"):
							os.rename(f"__exectempdir__/{file}", f"__exectempdir__/{file.replace('.suis', '.py')}")

							with open(f"{path}/{file}", 'r', encoding = "utf-8") as sourceFile:
								with open(f"__exectempdir__/{file.replace('.suis', '.py')}", "w", encoding = "utf-8") as targetFile:
									input(convertCode("python", sourceFile.readlines()))

					# menu pour choisir le fichier (que les .suis)

					shutil.rmtree("__exectempdir__")

					# execution

	elif menuAccueil.lower() == "convertir":
		pass
		# convertir en suis
		# convertir en python
			# convertir un fichier
			# convertir un dossier
			# convertir en direct
				# afficher
				# enregistrer
				# afficher et enregistrer

	elif menuAccueil.lower() == "afficher le clavier":
		menuClavier = ""
		while "retour" not in menuClavier.lower():
			menuClavier = menu(["Afficher les caractères en minuscule", "Afficher les caractères en majuscule", "Afficher les caractères en altgr"], homeTitle, [menuAccueil])

			if menuClavier.lower() == "afficher les caractères en minuscule":
				charsType = 'lower'

			elif menuClavier.lower() == "afficher les caractères en majuscule":
				charsType = 'upper'

			elif menuClavier.lower() == "afficher les caractères en altgr":
				charsType = 'altgr'

			elif menuClavier.lower() == "quitter":
				sys.exit(0)

			if "Afficher les caractères en" in menuClavier:
				menuClavierAffichage = menu([], f"""   ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ 
  ||{[[chars[charsType][2][1] if 1 in chars[charsType][2].keys() else ' '][0] if 2 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][2][2] if 2 in chars[charsType][2].keys() else ' '][0] if 2 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][2][3] if 3 in chars[charsType][2].keys() else ' '][0] if 2 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][2][4] if 4 in chars[charsType][2].keys() else ' '][0] if 2 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][2][5] if 5 in chars[charsType][2].keys() else ' '][0] if 2 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][2][6] if 6 in chars[charsType][2].keys() else ' '][0] if 2 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][2][7] if 7 in chars[charsType][2].keys() else ' '][0] if 2 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][2][8] if 8 in chars[charsType][2].keys() else ' '][0] if 2 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][2][9] if 9 in chars[charsType][2].keys() else ' '][0] if 2 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][2][10] if 10 in chars[charsType][2].keys() else ' '][0] if 2 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][2][11] if 11 in chars[charsType][2].keys() else ' '][0] if 2 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][2][12] if 12 in chars[charsType][2].keys() else ' '][0] if 2 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][2][13] if 13 in chars[charsType][2].keys() else ' '][0] if 2 in chars[charsType].keys() else ' '][0]} ||
2 ||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__||
  |/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|
   _______ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____
  ||{[['tab' if 1 in chars[charsType][3].keys() else '   '][0] if 3 in chars[charsType].keys() else '   '][0]}  |||{[[chars[charsType][3][2] if 2 in chars[charsType][3].keys() else ' '][0] if 3 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][3][3] if 3 in chars[charsType][3].keys() else ' '][0] if 3 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][3][4] if 4 in chars[charsType][3].keys() else ' '][0] if 3 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][3][5] if 5 in chars[charsType][3].keys() else ' '][0] if 3 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][3][6] if 6 in chars[charsType][3].keys() else ' '][0] if 3 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][3][7] if 7 in chars[charsType][3].keys() else ' '][0] if 3 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][3][8] if 8 in chars[charsType][3].keys() else ' '][0] if 3 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][3][9] if 9 in chars[charsType][3].keys() else ' '][0] if 3 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][3][10] if 10 in chars[charsType][3].keys() else ' '][0] if 3 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][3][11] if 11 in chars[charsType][3].keys() else ' '][0] if 3 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][3][12] if 12 in chars[charsType][3].keys() else ' '][0] if 3 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][3][13] if 13 in chars[charsType][3].keys() else ' '][0] if 3 in chars[charsType].keys() else ' '][0]} ||
3 ||_____|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__||
  |/_____\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|
   _________ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____
  ||       |||{[[chars[charsType][4][2] if 2 in chars[charsType][4].keys() else ' '][0] if 4 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][4][3] if 3 in chars[charsType][4].keys() else ' '][0] if 4 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][4][4] if 4 in chars[charsType][4].keys() else ' '][0] if 4 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][4][5] if 5 in chars[charsType][4].keys() else ' '][0] if 4 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][4][6] if 6 in chars[charsType][4].keys() else ' '][0] if 4 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][4][7] if 7 in chars[charsType][4].keys() else ' '][0] if 4 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][4][8] if 8 in chars[charsType][4].keys() else ' '][0] if 4 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][4][9] if 9 in chars[charsType][4].keys() else ' '][0] if 4 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][4][10] if 10 in chars[charsType][4].keys() else ' '][0] if 4 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][4][11] if 11 in chars[charsType][4].keys() else ' '][0] if 4 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][4][12] if 12 in chars[charsType][4].keys() else ' '][0] if 4 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][4][13] if 13 in chars[charsType][4].keys() else ' '][0] if 4 in chars[charsType].keys() else ' '][0]} ||
4 ||_______|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__||
  |/_______\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|
   ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ______________ 
  ||  |||{[[chars[charsType][5][2] if 2 in chars[charsType][5].keys() else ' '][0] if 5 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][5][3] if 3 in chars[charsType][5].keys() else ' '][0] if 5 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][5][4] if 4 in chars[charsType][5].keys() else ' '][0] if 5 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][5][5] if 5 in chars[charsType][5].keys() else ' '][0] if 5 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][5][6] if 6 in chars[charsType][5].keys() else ' '][0] if 5 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][5][7] if 7 in chars[charsType][5].keys() else ' '][0] if 5 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][5][8] if 8 in chars[charsType][5].keys() else ' '][0] if 5 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][5][9] if 9 in chars[charsType][5].keys() else ' '][0] if 5 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][5][10] if 10 in chars[charsType][5].keys() else ' '][0] if 5 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][5][11] if 11 in chars[charsType][5].keys() else ' '][0] if 5 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][5][12] if 12 in chars[charsType][4].keys() else ' '][0] if 5 in chars[charsType].keys() else ' '][0]} |||            ||
5 ||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||____________||
  |/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/____________\|
   ____ ____ ____ _______________________________________ ____ ____ ____
  ||  |||  |||  |||               {[['espace ' if 4 in chars[charsType][6].keys() else '       '][0] if 6 in chars[charsType].keys() else '       '][0]}               |||  |||  |||  ||
6 ||__|||__|||__|||_____________________________________|||__|||__|||__||
  |/__\|/__\|/__\|/_____________________________________\|/__\|/__\|/__\|""", [menuAccueil, menuClavier])

				if menuClavierAffichage.lower() == "quitter":
					sys.exit(0)

	elif menuAccueil.lower() == "notice d'utilisation":
		pass
