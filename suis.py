from os import name as os_name
from os import system as os_system
from os import remove as os_remove
from os import listdir as os_listdir
from os import rename as os_rename

from os.path import isfile as os_path_isfile
from os.path import join as os_path_join
from os.path import exists as os_path_exists
from os.path import isdir as os_path_isdir

from colorama import Fore as colorama_Fore
from colorama import Back as colorama_Back
from colorama import Style as colorama_Style

from shutil import rmtree as shutil_rmtree
from shutil import copytree as shutil_copytree

from pynput.keyboard import Controller as pynput_keyboard_Controller
from pynput.keyboard import Key as pynput_keyboard_Key

from sys import exit as sys_exit
from string import printable as string_printable
from msvcrt import getch as msvcrt_getch
from threading import Thread as threading_Thread
from time import sleep as time_sleep
from tkinter import filedialog as tkinter_filedialog

if os_name == 'nt':
	def clear():
		os_system('cls')

else:
	def clear():
		os_system('clear')

clear()

def menu(choices = [], title="", previousChoices=[]):
	if title:
		title = f'\n{title}\n{colorama_Fore.GREEN}\nFaites <Entrer> pour naviguer entre les différentes options.\nFaites "ok" pour confirmer votre choix.{colorama_Fore.BLACK}\n'

	if previousChoices:
		choices.append("")
		choices.append(f"Retourner vers : {previousChoices[-1]}")
		choices.append("Quitter")

	else:
		choices.append("")
		choices.append("Quitter")

	output, tallestLength = "", 0

	for choiceIndex in range(len(choices)):
		if (len(choices[choiceIndex]) > tallestLength):
			tallestLength = len(choices[choiceIndex])

		if choices[choiceIndex]:
			choices[choiceIndex] = choices[choiceIndex][0].upper() + choices[choiceIndex][1:]

	while 'ok' not in output.lower().strip():
		for selection in choices:
			if not selection:
				continue

			print(colorama_Back.LIGHTWHITE_EX + colorama_Fore.BLACK)
			clear()

			if os_name == "nt":
				if previousChoices:
					if selection.startswith("Retourner vers : "):
						os_system(f'title "Suis v0.0.1 ◦ By CalvinYrd : {" > ".join(previousChoices)}"')

					else:
						os_system(f'title "Suis v0.0.1 ◦ By CalvinYrd : {" > ".join(previousChoices)} > {selection}"')

				else:
					os_system(f'title "Suis v0.0.1 ◦ By CalvinYrd : {selection}"')

			for line in title.split("\n"):
				print(f"   {line}")

			if previousChoices:
				if selection.startswith("Retourner vers : "):
					print(f'   {colorama_Fore.BLUE}{" > ".join(previousChoices)}{colorama_Fore.BLACK}\n')

				else:
					print(f'   {colorama_Fore.BLUE}{" > ".join(previousChoices)} > {selection}{colorama_Fore.BLACK}\n')

			else:
				print(f'   {colorama_Fore.BLUE}{selection}{colorama_Fore.BLACK}\n')

			for choice in choices:
				if choice == selection:
					print(f"   {colorama_Back.LIGHTGREEN_EX}* {choice}{int((tallestLength - len(choice))) * ' '} {colorama_Back.LIGHTWHITE_EX}")

				else:
					if choice:
						print(f"   - {choice}")

					else:
						print()

			output = input("\n> ")
			if 'ok' in output.lower().strip() and selection:
				if os_name == "nt":
					os_system('title "Suis 0.0.1 | By CalvinYrd"')

				if selection.lower() == "quitter" or selection.lower() == "quit" or selection.lower() == "exit" or selection.lower() == "q":
					print(colorama_Style.RESET_ALL)
					clear()

				return selection

def convertCode(language, lines, fileName = None):
	newLines = []
	currentLineIteration = 0

	for lineIndex in range(len(lines)):
		if language == "python":

			newLine = ''

			if lines[lineIndex].replace('\n', ''):
				decomposedLine = {"instruction" : None, "comment" : None}
				currentLineIteration += 1

				if len(lines[lineIndex][::-1].replace('~~', 'afl855dh2qlhh12g15dg145d7'[::-1], 1)[::-1].split('afl855dh2qlhh12g15dg145d7')) == 2:

					commentExists = lines[lineIndex]
					for c in string_printable.replace('}', '').replace('¤', '').replace('~', ''):
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

				for char in string_printable.replace('}', '').replace('¤', '').replace('~', '').replace('\n', ''):
					for charToVerifyIndex in range(len(charsVerifier)):
						if char in charsVerifier[charToVerifyIndex]:

							if fileName:
								print(f"The {colorama_Fore.RED}\"{char}\"{colorama_Fore.BLACK} character is not allowed to be used in this context at line {colorama_Fore.GREEN}{str(currentLineIteration)}{colorama_Fore.BLACK} on set n°{colorama_Fore.GREEN}{str(charToVerifyIndex + 1)}{colorama_Fore.BLACK} containing \"{charsVerifier[charToVerifyIndex].replace(char, f'{colorama_Fore.RED}{char}{colorama_Fore.BLACK}', 1)}\" in file : {colorama_Fore.BLUE}{fileName}{colorama_Fore.BLACK}.\nyou can only use these three characters : {'}'} , ¤ , ~. Except you are writing a comment.\nin which case you can use any character.")

							else:
								print(f"The {colorama_Fore.RED}\"{char}\"{colorama_Fore.BLACK} character is not allowed to be used in this context at line {colorama_Fore.GREEN}{str(currentLineIteration)}{colorama_Fore.BLACK} on set n°{colorama_Fore.GREEN}{str(charToVerifyIndex + 1)}{colorama_Fore.BLACK} containing \"{charsVerifier[charToVerifyIndex].replace(char, f'{colorama_Fore.RED}{char}{colorama_Fore.BLACK}', 1)}\".\nyou can only use these three characters : {'}'} , ¤ , ~. Except you are writing a comment.\nin which case you can use any character.")

							return

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

						if fileName:
							unAllowedCharacterErrorMessage = f"There is no character at position {colorama_Fore.RED}{characterSchema[0]}:{characterSchema[1]}{colorama_Fore.BLACK} in this context at line {colorama_Fore.GREEN}{str(currentLineIteration)}{colorama_Fore.BLACK} on set n°{colorama_Fore.GREEN}{str(currentSetIteration)}{colorama_Fore.BLACK} containing {colorama_Fore.RED}\"{characters[characterIndex]}\"{colorama_Fore.BLACK} in file : {colorama_Fore.BLUE}{fileName}{colorama_Fore.BLACK}.\nTake a look at the keyboard at home for more."

						else:
							unAllowedCharacterErrorMessage = f"There is no character at position {colorama_Fore.RED}{characterSchema[0]}:{characterSchema[1]}{colorama_Fore.BLACK} in this context at line {colorama_Fore.GREEN}{str(currentLineIteration)}{colorama_Fore.BLACK} on set n°{colorama_Fore.GREEN}{str(currentSetIteration)}{colorama_Fore.BLACK} containing {colorama_Fore.RED}\"{characters[characterIndex]}\"{colorama_Fore.BLACK}.\nTake a look at the keyboard at home for more."

						try:
							if characters[characterIndex + 1] == '¤':
								try:
									newLine += characterSchema[2] * chars['altgr'][characterSchema[0]][characterSchema[1]]

								except KeyError:
									print(unAllowedCharacterErrorMessage)
									return

							elif not characters[characterIndex + 1]:
								try:
									newLine += characterSchema[2] * chars['upper'][characterSchema[0]][characterSchema[1]]

								except KeyError:
									print(unAllowedCharacterErrorMessage)
									return


							else:
								try:
									newLine += characterSchema[2] * chars['lower'][characterSchema[0]][characterSchema[1]]

								except KeyError:
									print(unAllowedCharacterErrorMessage)
									return

						except IndexError:
							try:
								newLine += characterSchema[2] * chars['lower'][characterSchema[0]][characterSchema[1]]
							
							except KeyError:
								print(unAllowedCharacterErrorMessage)
								return

				if decomposedLine['comment']:
					newLine += f" #{decomposedLine['comment']}"

			else:
				newLine += '\n'

			newLines.append(newLine)

		elif language == "suis":
			newLine = ""

			for char in lines[lineIndex]:
				for charType in ("lower", "upper", "altgr"):

					for charsListIndex in chars[charType]:				
						for _char in chars[charType][charsListIndex]:

							if chars[charType][charsListIndex][_char] == char:
								char = {"line" : charsListIndex, "column" : _char, "type" : None}

								if charType == "lower":
									char["type"] = "~"

								elif charType == "upper":
									char["type"] = "~~"

								elif charType == "altgr":
									char["type"] = "~¤~"

								if char["column"] >= 10:
									newLine += f"{char['line'] * '}'}¤{int(str(char['column'])[0]) * '}'}¤¤{int(str(char['column'])[1]) * '}'}{char['type']}"

								else:
									newLine += f"{char['line'] * '}'}¤{char['column'] * '}'}{char['type']}"

			newLines.append(newLine)

	return newLines

def launchPythonInterpreter():
	os_system('py')

def printSuisDetails():
	print("Suis 0.0.1\nWrite an empty line to quit.\n>>> ")

def interpretSuis():
	output = '.'
	pynput_keyboard_Controller().press(pynput_keyboard_Key.enter)
	while output.strip():
		output = input()

		code = convertCode('python', [output])

		if code:
			pynput_keyboard_Controller().type("\n" + code[0])

		else:
			pynput_keyboard_Controller().type("\n")

		time_sleep(0.3)
		pynput_keyboard_Controller().press(pynput_keyboard_Key.enter)

	pynput_keyboard_Controller().type("import sys; sys.exit(0)")
	pynput_keyboard_Controller().press(pynput_keyboard_Key.enter)

def exit():
	print(colorama_Style.RESET_ALL)
	clear()
	sys_exit(0)

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
					path = tkinter_filedialog.askopenfile(filetypes = (("Fichiers suis", "*.suis"), ("Tous les fichiers", "*.*")))

					if path and path.name.endswith(".suis"):
						path = path.name

						with open(path, "r", encoding = "utf-8") as sourceFile:
							clear()
							code = convertCode("python", sourceFile.readlines(), path)

							if code:
								with open("__exectempfile__.py", "w", encoding = "utf-8") as targetFile:
									for line in code:
										if line.strip('\n'):
											targetFile.write(line + "\n")

										else:
											targetFile.write("\n")

							else:
								print('\n### Appuyez sur une touche pour continuer ###')
								msvcrt_getch()

						clear()
						if code:
							os_system('py __exectempfile__.py')
							os_remove("__exectempfile__.py")
							print(f'\n### Appuyez sur une touche pour continuer ###')
							msvcrt_getch()

				elif "interpreter un dossier" in menuInterprete.lower():
					path = tkinter_filedialog.askdirectory()

					if path:
						files = []

						for file in os_listdir(path):
							if os_path_isfile(os_path_join(path, file)):
								files.append(file)

						if os_path_exists("__exectempdir__") and os_path_isdir("__exectempdir__"):
							shutil_rmtree("__exectempdir__")

						shutil_copytree(path, "__exectempdir__")

						for file in files:
							if file.endswith(".suis"):
								os_rename(f"__exectempdir__/{file}", f"__exectempdir__/{file.replace('.suis', '.py')}")

								with open(f"{path}/{file}", 'r', encoding = "utf-8") as sourceFile:
									print()
									code = convertCode("python", sourceFile.readlines(), f"{path}/{file}")

									if code:
										with open(f"__exectempdir__/{file.replace('.suis', '.py')}", "w", encoding = "utf-8") as targetFile:
											targetFile.writelines(code)

									else:
										with open(f"__exectempdir__/{file.replace('.suis', '.py')}", "w", encoding = "utf-8") as targetFile:
											targetFile.writelines("print('Fichier inexecutable, ce dernier contient une erreur.')")

										print(f'\n### Appuyez sur une touche pour continuer ###')
										msvcrt_getch()

						menuInterpreteDossier = menu([i for i in os_listdir("__exectempdir__") if i.endswith(".py")], homeTitle, [menuAccueil, menuInterprete])

						if menuInterpreteDossier.lower() == 'quitter':
							shutil_rmtree("__exectempdir__")
							exit()

						elif "retourner vers : " not in menuInterpreteDossier.lower():
							clear()
							os_system(f"py __exectempdir__/{menuInterpreteDossier}")
							shutil_rmtree("__exectempdir__")
							print(f'\n### Appuyez sur une touche pour continuer ###')
							msvcrt_getch()

						else:
							shutil_rmtree("__exectempdir__")	

				elif "interpreter en temps" in menuInterprete.lower():

					threading_Thread(target = launchPythonInterpreter).start()
					time_sleep(0.2)
					threading_Thread(target = clear).start()
					time_sleep(0.2)
					threading_Thread(target = printSuisDetails).start()
					interpretSuis()

		elif menuAccueil.lower() == "convertir":
			menuConvertir = ""

			while "retour" not in menuConvertir.lower():
				menuConvertir = menu(["Convertir en suis", "Convertir en python / littéraire"], homeTitle, [menuAccueil])

				if "quitter" in menuConvertir.lower():
					exit()

				elif "convertir" in menuConvertir.lower() and ("python" in menuConvertir.lower() or "suis" in menuConvertir.lower()):

					if "python" in menuConvertir.lower():
						langageConversion = "suis"

					elif "suis" in menuConvertir.lower():
						langageConversion = "python"

					menuConvertir2 = ""

					while "retour" not in menuConvertir2.lower():
						menuConvertir2 = menu(["Convertir un fichier", "Convertir du texte"], homeTitle, [menuAccueil, menuConvertir])

						if "quitter" in menuConvertir2.lower():
							exit()

						elif "fichier" in menuConvertir2.lower() or "texte" in menuConvertir2.lower():
							result = None

							if langageConversion == "suis":
									langageConversionExt, langageConversionResultat, langageConversionResultatExt = "suis", "python", "py"

							elif langageConversion == "python":
								langageConversionExt, langageConversionResultat, langageConversionResultatExt = "py", "suis", "suis"

							if "fichier" in menuConvertir2.lower():

								path = tkinter_filedialog.askopenfile(filetypes = (("Fichiers python", f"*.{langageConversionExt}"), ("Tous les fichiers", "*.*")))

								if path and path.name.endswith(f".{langageConversionExt}"):
									path = path.name

									with open(path, 'r', encoding = "utf-8") as file:
										result = convertCode(langageConversionResultat, file.readlines(), path)

							elif "texte" in menuConvertir2.lower():
								clear()
								result = convertCode(langageConversionResultat, [input("Saisissez le contenu à convertir :\n> ")])

							if result:
								menuConvertir3 = ""

								while "retour" not in menuConvertir3.lower():
									menuConvertir3 = menu(["afficher", "enregistrer", [i if 'fichier' in menuConvertir2.lower() else '' for i in ['écraser']][0]], homeTitle, [menuAccueil, menuConvertir, menuConvertir2])

									if "quitter" in menuConvertir3.lower():
										exit()

									elif "afficher" in menuConvertir3.lower():
										clear()
										
										for line in result:
											if line.strip('\n'):
												print(line)

											else:
												print()

										print(f'\n### Appuyez sur une touche pour continuer ###')
										msvcrt_getch()

									elif "enregistrer" in menuConvertir3.lower():
										savePath = tkinter_filedialog.asksaveasfile(defaultextension = f".{langageConversionResultatExt}")

										if savePath:
											with open(savePath.name, "w", encoding = "utf-8") as file:
												for line in result:
													if line.strip('\n'):
														file.write(line + "\n")

													else:
														file.write("\n")

											clear()
											print(f'\n### Fichier créé. Appuyez sur une touche pour continuer ###')
											msvcrt_getch()

										else:
											clear()
											print(f'\n### Echec de création du fichier. Appuyez sur une touche pour continuer ###')
											msvcrt_getch()

									elif "écraser" in menuConvertir3.lower():
										os_remove(path)

										with open(path[::-1].replace(f'.{path[::-1].split(".", 1)[0][::-1]}'[::-1], f".{langageConversionResultatExt}"[::-1], 1)[::-1], "w", encoding = "utf-8") as file:
											for line in result:
												if line.strip('\n'):
													file.write(line + "\n")

												else:
													file.write("\n")

										clear()
										print(f'\n### Fichier écrasé. Appuyez sur une ouche pour continuer ###')
										msvcrt_getch()

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
			clear()
			print("\n### En raison de la fainéantise du développeur ayant conçu ce programme, la section suivante n'as pas encore été conçue. Appuyez sur une touche pour continuer ###")
			msvcrt_getch()

except (EOFError, KeyboardInterrupt):
	exit()
