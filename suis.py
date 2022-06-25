from tkinter import filedialog
import os, colorama, sys, shutil, string, msvcrt, pynput, threading, time

class UnauthorizedSymbolError(Exception):
	def __init__(self, character, line, _set, file):
		super().__init__(f"The \"{character}\" character is not allowed to be used in this context at line {str(line)} on set n°{str(_set['iteration'])} containing \"{_set['value']}\" in file : {file}, you can only use these three characters : {'}'} , ¤ , ~. Except you are writing a comment, in which case you can use any character.")

class UnknownCharacterError(Exception):
	def __init__(self, y, x, type, line, _set, file):
		super().__init__(f"There is no character at position {y}:{x} of type \"{type}\" at line {str(line)} on set n°{str(_set['iteration'])} containing \"{_set['value']}\" in file : {file}. Please check the keyboard on the home menu.")

if os.name == 'nt':
	def clear():
		os.system('cls')

else:
	def clear():
		os.system('clear')

clear()

def menu(choices = [], title="", previousChoices=[]):
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

	for lineIndex in range(len(lines)):
		if language == "python":

			newLine = ''
			if lines[lineIndex].replace('\n', ''):
				decomposedLine = {"instruction" : None, "comment" : None}

				if len(lines[lineIndex][::-1].replace('~~', 'afl855dh2qlhh12g15dg145d7'[::-1], 1)[::-1].split('afl855dh2qlhh12g15dg145d7')) == 2:

					commentExists = lines[lineIndex]
					for c in string.printable.replace('}', '').replace('¤', '').replace('~', ''):
						commentExists = commentExists.replace(c, '')

					if commentExists.endswith('~~~'):
						decomposedLine['instruction'] = lines[lineIndex][::-1].replace('~~', 'afl855dh2qlhh12g15dg145d7'[::-1], 1)[::-1].split('afl855dh2qlhh12g15dg145d7')[0]
						decomposedLine['comment'] = lines[lineIndex][::-1].replace('~~', 'afl855dh2qlhh12g15dg145d7'[::-1], 1)[::-1].split('afl855dh2qlhh12g15dg145d7')[1]

					else:
						decomposedLine['instruction'] = lines[lineIndex]
						decomposedLine['comment'] = None

				else:
					decomposedLine['instruction'] = lines[lineIndex]
					decomposedLine['comment'] = None

				charsVerifier = [i for i in lines[lineIndex][::-1].replace('~~', 'afl855dh2qlhh12g15dg145d7'[::-1], 1)[::-1].split('afl855dh2qlhh12g15dg145d7')[0].split('~') if i and i != '¤']

				for char in string.printable.replace('}', '').replace('¤', '').replace('~', '').replace('\n', ''):
					for charToVerifyIndex in range(len(charsVerifier)):
						if char in charsVerifier[charToVerifyIndex]:
							raise UnauthorizedSymbolError(char, lineIndex + 1, {'iteration' : charToVerifyIndex + 1, 'value' : charsVerifier[charToVerifyIndex]}, '!!! FILE NAME IN CONTEXT !!!')

				characters = decomposedLine['instruction'].split('~')[:-1]
				currentSetIteration = 0

				for characterIndex in range(len(characters)):
					if '}' in characters[characterIndex] and '¤' in characters[characterIndex]:

						currentSetIteration += 1
						characterDecomposition, characterSchema = characters[characterIndex].split('¤'), []
						characterSchema.append(len(characterDecomposition[0]))
						baseIndex = None

						if len(characterDecomposition) > 2 and not characterDecomposition[2]:
							characterSchema.append(len(characterDecomposition[1]) * 10 + len(characterDecomposition[3]))

							if (len(characterDecomposition) > 4):
								baseIndex = 4

						else:
							characterSchema.append(len(characterDecomposition[1]))

							if (len(characterDecomposition) > 2):
								baseIndex = 2

						if baseIndex:
							multiplier = 0

							for i in range(len(characterDecomposition) - baseIndex):

								if characterDecomposition[baseIndex]:
									multiplier += int(str(len(characterDecomposition[baseIndex])) + int((((len(characterDecomposition) - baseIndex) - 1) / 2)) * '0')

									baseIndex += 1

								elif not characterDecomposition[baseIndex] and not characterDecomposition[baseIndex - 1]:
									baseIndex += 1

								else:
									baseIndex += 1
									continue

							characterSchema.append(multiplier)

						else:
							characterSchema.append(1)

						try:
							if characters[characterIndex + 1] == '¤':
								try:
									newLine += characterSchema[2] * chars['altgr'][characterSchema[0]][characterSchema[1]]

								except KeyError:
									raise UnknownCharacterError(characterSchema[0], characterSchema[1], 'altgr', lineIndex + 1, {'iteration' : currentSetIteration, 'value' : characters[characterIndex]}, '!!! FILE NAME IN CONTEXT !!!')

							elif not characters[characterIndex + 1]:
								try:
									newLine += characterSchema[2] * chars['upper'][characterSchema[0]][characterSchema[1]]

								except KeyError:
									raise UnknownCharacterError(characterSchema[0], characterSchema[1], 'upper', lineIndex + 1, {'iteration' : currentSetIteration, 'value' : characters[characterIndex]}, '!!! FILE NAME IN CONTEXT !!!')

							else:
								try:
									newLine += characterSchema[2] * chars['lower'][characterSchema[0]][characterSchema[1]]

								except KeyError:
									raise UnknownCharacterError(characterSchema[0], characterSchema[1], 'lower', lineIndex + 1, {'iteration' : currentSetIteration, 'value' : characters[characterIndex]}, '!!! FILE NAME IN CONTEXT !!!')

						except IndexError:
							try:
								newLine += characterSchema[2] * chars['lower'][characterSchema[0]][characterSchema[1]]
							
							except KeyError:
								raise UnknownCharacterError(characterSchema[0], characterSchema[1], 'lower', lineIndex + 1, {'iteration' : characterIndex + 1, 'value' : characters[characterIndex]}, '!!! FILE NAME IN CONTEXT !!!')

				if decomposedLine['comment']:
					newLine += f" #{decomposedLine['comment']}"

			else:
				newLine += '\n'

			newLines.append(newLine)

	return newLines

def launchPythonInterpreter():
	os.system('py')

def printSuisDetails():
	print("Suis 0.0.1\nWrite an empty line to quit.\n>>> ")

def interpretSuis():
	output = '.'
	pynput.keyboard.Controller().press(pynput.keyboard.Key.enter)
	while output.strip():
		output = input()
		pynput.keyboard.Controller().type("\n" + convertCode('python', [output])[0])
		time.sleep(0.3)
		pynput.keyboard.Controller().press(pynput.keyboard.Key.enter)

	pynput.keyboard.Controller().type("import sys; sys.exit(0)")
	pynput.keyboard.Controller().press(pynput.keyboard.Key.enter)

def exit():
	print(colorama.Style.RESET_ALL)
	clear()
	sys.exit(0)

try:
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
				menuInterprete = menu(["Interpreter un fichier", "Interpreter un dossier (seuls les fichiers à l'origine du dossiers seront convertis en langage suis)", "Interpreter en temps-réel"], homeTitle, [menuAccueil])

				if menuInterprete.lower() == "quitter":
					exit()

				elif "interpreter un fichier" in menuInterprete.lower():
					path = filedialog.askopenfile(filetypes = (("Fichiers suis", "*.suis"), ("Tous les fichiers", "*.*")))

					if path and path.name.endswith(".suis"):
						path = path.name

						with open(path, "r", encoding = "utf-8") as sourceFile:
							with open("__exectempfile__.py", "w", encoding = "utf-8") as targetFile:
								for line in convertCode("python", sourceFile.readlines()):
									targetFile.write(line)

						clear()
						os.system('py __exectempfile__.py')
						os.remove("__exectempfile__.py")
						print(f'\n### Appuyez sur une touche pour continuer ###')
						msvcrt.getch()

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
										targetFile.writelines(convertCode("python", sourceFile.readlines()))

						menuInterpreteDossier = menu([i for i in os.listdir("__exectempdir__") if i.endswith(".py")], homeTitle, [menuAccueil, menuInterprete])

						if menuInterpreteDossier.lower() == 'quitter':
							shutil.rmtree("__exectempdir__")
							exit()

						elif "retourner vers : " not in menuInterpreteDossier.lower():
							clear()
							os.system(f"py __exectempdir__/{menuInterpreteDossier}")
							shutil.rmtree("__exectempdir__")
							print(f'\n### Appuyez sur une touche pour continuer ###')
							msvcrt.getch()

						else:
							shutil.rmtree("__exectempdir__")

				elif "interpreter en temps" in menuInterprete.lower():

					threading.Thread(target = launchPythonInterpreter).start()
					time.sleep(0.2)
					threading.Thread(target = clear).start()
					time.sleep(0.2)
					threading.Thread(target = printSuisDetails).start()
					interpretSuis()

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
					exit()

				if "Afficher les caractères en" in menuClavier:
					menuClavierAffichage = menu([], f"""     ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ 
|   ||{[[chars[charsType][2][1] if 1 in chars[charsType][2].keys() else ' '][0] if 2 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][2][2] if 2 in chars[charsType][2].keys() else ' '][0] if 2 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][2][3] if 3 in chars[charsType][2].keys() else ' '][0] if 2 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][2][4] if 4 in chars[charsType][2].keys() else ' '][0] if 2 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][2][5] if 5 in chars[charsType][2].keys() else ' '][0] if 2 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][2][6] if 6 in chars[charsType][2].keys() else ' '][0] if 2 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][2][7] if 7 in chars[charsType][2].keys() else ' '][0] if 2 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][2][8] if 8 in chars[charsType][2].keys() else ' '][0] if 2 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][2][9] if 9 in chars[charsType][2].keys() else ' '][0] if 2 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][2][10] if 10 in chars[charsType][2].keys() else ' '][0] if 2 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][2][11] if 11 in chars[charsType][2].keys() else ' '][0] if 2 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][2][12] if 12 in chars[charsType][2].keys() else ' '][0] if 2 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][2][13] if 13 in chars[charsType][2].keys() else ' '][0] if 2 in chars[charsType].keys() else ' '][0]} ||
| 2 ||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__||
|   |/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|
|    _______ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____
|   ||{[['tab' if 1 in chars[charsType][3].keys() else '   '][0] if 3 in chars[charsType].keys() else '   '][0]}  |||{[[chars[charsType][3][2] if 2 in chars[charsType][3].keys() else ' '][0] if 3 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][3][3] if 3 in chars[charsType][3].keys() else ' '][0] if 3 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][3][4] if 4 in chars[charsType][3].keys() else ' '][0] if 3 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][3][5] if 5 in chars[charsType][3].keys() else ' '][0] if 3 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][3][6] if 6 in chars[charsType][3].keys() else ' '][0] if 3 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][3][7] if 7 in chars[charsType][3].keys() else ' '][0] if 3 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][3][8] if 8 in chars[charsType][3].keys() else ' '][0] if 3 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][3][9] if 9 in chars[charsType][3].keys() else ' '][0] if 3 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][3][10] if 10 in chars[charsType][3].keys() else ' '][0] if 3 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][3][11] if 11 in chars[charsType][3].keys() else ' '][0] if 3 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][3][12] if 12 in chars[charsType][3].keys() else ' '][0] if 3 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][3][13] if 13 in chars[charsType][3].keys() else ' '][0] if 3 in chars[charsType].keys() else ' '][0]} ||
| 3 ||_____|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__||
|   |/_____\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|
|    _________ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____
|   ||       |||{[[chars[charsType][4][2] if 2 in chars[charsType][4].keys() else ' '][0] if 4 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][4][3] if 3 in chars[charsType][4].keys() else ' '][0] if 4 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][4][4] if 4 in chars[charsType][4].keys() else ' '][0] if 4 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][4][5] if 5 in chars[charsType][4].keys() else ' '][0] if 4 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][4][6] if 6 in chars[charsType][4].keys() else ' '][0] if 4 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][4][7] if 7 in chars[charsType][4].keys() else ' '][0] if 4 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][4][8] if 8 in chars[charsType][4].keys() else ' '][0] if 4 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][4][9] if 9 in chars[charsType][4].keys() else ' '][0] if 4 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][4][10] if 10 in chars[charsType][4].keys() else ' '][0] if 4 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][4][11] if 11 in chars[charsType][4].keys() else ' '][0] if 4 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][4][12] if 12 in chars[charsType][4].keys() else ' '][0] if 4 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][4][13] if 13 in chars[charsType][4].keys() else ' '][0] if 4 in chars[charsType].keys() else ' '][0]} ||
| 4 ||_______|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__||
|   |/_______\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|
|    ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ______________ 
|   ||  |||{[[chars[charsType][5][2] if 2 in chars[charsType][5].keys() else ' '][0] if 5 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][5][3] if 3 in chars[charsType][5].keys() else ' '][0] if 5 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][5][4] if 4 in chars[charsType][5].keys() else ' '][0] if 5 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][5][5] if 5 in chars[charsType][5].keys() else ' '][0] if 5 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][5][6] if 6 in chars[charsType][5].keys() else ' '][0] if 5 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][5][7] if 7 in chars[charsType][5].keys() else ' '][0] if 5 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][5][8] if 8 in chars[charsType][5].keys() else ' '][0] if 5 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][5][9] if 9 in chars[charsType][5].keys() else ' '][0] if 5 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][5][10] if 10 in chars[charsType][5].keys() else ' '][0] if 5 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][5][11] if 11 in chars[charsType][5].keys() else ' '][0] if 5 in chars[charsType].keys() else ' '][0]} |||{[[chars[charsType][5][12] if 12 in chars[charsType][4].keys() else ' '][0] if 5 in chars[charsType].keys() else ' '][0]} |||            ||
| 5 ||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||__|||____________||
|   |/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/____________\|
|    ____ ____ ____ _______________________________________ ____ ____ ____
|   ||  |||  |||  |||               {[['espace ' if 4 in chars[charsType][6].keys() else '       '][0] if 6 in chars[charsType].keys() else '       '][0]}               |||  |||  |||  ||
| 6 ||__|||__|||__|||_____________________________________|||__|||__|||__||
|   |/__\|/__\|/__\|/_____________________________________\|/__\|/__\|/__\|""", [menuAccueil, menuClavier])

					if menuClavierAffichage.lower() == "quitter":
						exit()

		elif menuAccueil.lower() == "notice d'utilisation":
			pass

except (EOFError, KeyboardInterrupt):
	exit()
