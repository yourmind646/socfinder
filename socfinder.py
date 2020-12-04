#!/usr/bin/env python3
try:
	import requests, json, colorama
	from colorama import Fore, Back, Style

	colorama.init()

	class nicknameIsEmpty(Exception):
		pass

	class nicknameContainsSpace(Exception):
		pass

	def search(nick):
		print('{}\n[=] Выполняется поиск профилей...{}'.format(Fore.YELLOW, Fore.WHITE))
		for site in data:
			r = str(requests.get(site + nick))
			if r.find("200") > -1:
				print('{}[+] {}{}'.format(Fore.GREEN, (site + nick), Fore.WHITE))
			elif r.find("404") > -1:
				print('{}[-] {}{}'.format(Fore.RED, (site + nick), Fore.WHITE))

	print(Fore.CYAN + '''
█████████████████████████████████████████████████████
█───█────█────█───█───█─██─█────██───█────██─███────█
█─███─██─█─██─█─████─██──█─█─██──█─███─██─█──███─██─█
█───█─██─█─████───██─██─█──█─██──█───█────██─███─██─█
███─█─██─█─██─█─████─██─██─█─██──█─███─█─███─███─██─█
█───█────█────█─███───█─██─█────██───█─█─███─█─█────█
█████████████████████████████████████████████████████

Предназначено для систем Linux/Termux
Автор скрипта TG @RubySide\n''' + Fore.WHITE)

	nickname = input('Введите никнейм, по которому нужно найти профиль (пример: rubyside)\n>>> ')

	if nickname == "":
		raise nicknameIsEmpty()
	elif nickname.find(' ') != -1:
		raise nicknameContainsSpace()

	print('{}\n[=] Загрузка списка с сайтами...{}'.format(Fore.YELLOW, Fore.WHITE))
	with open("data_file.json", "r") as read_file:
		data = json.load(read_file)
	print('{}[+] Список загружен! Сайтов для поиска - {}{}'.format(Fore.GREEN, len(data), Fore.WHITE))

	search(nickname)

except EOFError:
	print('\n{}[=] Выход из программы...{}'.format(Fore.YELLOW, Fore.WHITE))
except KeyboardInterrupt:
	print('\n\n{}[=] Выход из программы...{}'.format(Fore.YELLOW, Fore.WHITE))
except nicknameIsEmpty:
	print('\n{}[-] Никнейм не введен.{}'.format(Fore.RED, Fore.WHITE))
except nicknameContainsSpace:
	print('\n{}[-] Никнейм не должен содержать пробелы.{}'.format(Fore.RED, Fore.WHITE))