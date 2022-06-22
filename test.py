import os, string

class UnauthorizedSymbolError(Exception):
	def __init__(self, character, line, _set, file):
		super().__init__(f"The \"{character}\" character is not allowed to be used in this context at line {str(line)} on set n°{str(_set['iteration'])} containing \"{_set['value']}\" in file : {file}, you can only use these three characters : {'}'} , ¤ , ~. Except you are writing a comment, in which case you can use any character.")

class UnknownCharacterError(Exception):
	def __init__(self, y, x, type, line, _set, file):
		super().__init__(f"There is no character at position {y}:{x} of type \"{type}\" at line {str(line)} on set n°{str(_set['iteration'])} containing \"{_set['value']}\" in file : {file}. Please check the keyboard on the home menu.")

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

os.system('cls')

line = "}}}¤}¤¤}¤}¤¤}}}¤¤¤¤}~}}}¤}}~~}}}¤}¤¤~~~ commentaire"

decomposedLine = {"instruction" : None, "comment" : None}

decomposedLine['instruction'] = line[::-1].replace('~~', 'afl855dh2qlhh12g15dg145d7'[::-1], 1)[::-1].split('afl855dh2qlhh12g15dg145d7')[0]

decomposedLine['comment'] = line[::-1].replace('~~', 'afl855dh2qlhh12g15dg145d7'[::-1], 1)[::-1].split('afl855dh2qlhh12g15dg145d7')[1]

charsVerifier = [i for i in line[::-1].replace('~~', 'afl855dh2qlhh12g15dg145d7'[::-1], 1)[::-1].split('afl855dh2qlhh12g15dg145d7')[0].split('~') if i and i != '¤']
print(charsVerifier)

for char in string.printable.replace('}', '').replace('¤', '').replace('~', ''):
	for charToVerifyIndex in range(len(charsVerifier)):
		if char in charsVerifier[charToVerifyIndex]:
			raise UnauthorizedSymbolError(char, '!!! LINE NUMBER IN FOR LOOP !!!', {'iteration' : charToVerifyIndex + 1, 'value' : charsVerifier[charToVerifyIndex]}, '!!! FILE NAME IN CONTEXT !!!')

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
					print(characterSchema[2] * chars['altgr'][characterSchema[0]][characterSchema[1]])

				except KeyError:
					raise UnknownCharacterError(characterSchema[0], characterSchema[1], 'altgr', '!!! LINE NUMBER IN FOR LOOP !!!', {'iteration' : currentSetIteration, 'value' : characters[characterIndex]}, '!!! FILE NAME IN CONTEXT !!!')

			elif not characters[characterIndex + 1]:
				try:
					print(characterSchema[2] * chars['upper'][characterSchema[0]][characterSchema[1]])

				except KeyError:
					raise UnknownCharacterError(characterSchema[0], characterSchema[1], 'upper', '!!! LINE NUMBER IN FOR LOOP !!!', {'iteration' : currentSetIteration, 'value' : characters[characterIndex]}, '!!! FILE NAME IN CONTEXT !!!')

			else:
				try:
					print(characterSchema[2] * chars['lower'][characterSchema[0]][characterSchema[1]])

				except KeyError:
					raise UnknownCharacterError(characterSchema[0], characterSchema[1], 'lower', '!!! LINE NUMBER IN FOR LOOP !!!', {'iteration' : currentSetIteration, 'value' : characters[characterIndex]}, '!!! FILE NAME IN CONTEXT !!!')

		except IndexError:
			try:
				print(characterSchema[2] * chars['lower'][characterSchema[0]][characterSchema[1]])
			
			except KeyError:
				raise UnknownCharacterError(characterSchema[0], characterSchema[1], 'lower', '!!! LINE NUMBER IN FOR LOOP !!!', {'iteration' : characterIndex + 1, 'value' : characters[characterIndex]}, '!!! FILE NAME IN CONTEXT !!!')

