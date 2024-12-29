import random
import os
os.system("pip install faker")
from faker import Faker
import time
from colorama import init
from colorama import Fore, Back, Style
init()


faker = Faker()

print(Fore.CYAN + "\n█▀▀ █▀▀ █▄░█ █▀▀ █▀█ ▄▀█ ▀█▀ █▀█ █▀█")
print("█▄█ ██▄ █░▀█ ██▄ █▀▄ █▀█ ░█░ █▄█ █▀▄\n")


print(Fore.RESET + "[ 1 ] - Information about the software  [ 6 ] - Personality generator ")
time.sleep(0.1)
print("[ 2 ] - Phone generator numbers   	[ 7 ] - Mail generator ")
time.sleep(0.1)
print("[ 3 ] - Bank card generator 		[ 8 ] - Link generator ")
time.sleep(0.1)
print("[ 4 ] - Randomizer random numbers   	[ 9 ] - English name generator ")
time.sleep(0.1)
print("[ 5 ] - Password generator           	[ 10 ] - Randomizer from 1 to 10 ")
time.sleep(0.1)

print("[ 11 ] - Nickname generator         	[ 12 ] - Last name generation")
time.sleep(0.2)
print("[ 13 ] - Random street generator   	[ 14 ] - Exit the software")
time.sleep(0.2)

#print("\nВнимание! \nВсе что сгенерировано в этой программе вымошленное!")

command = input(Fore.CYAN + "\n[ ? ] -> Enter number: " + Fore.RESET)


if command == "1":
	print(Fore.RESET + "\nPosted by tg: @marjaway / discord: marjaway")
	time.sleep(0.2)
	print("Software version -> 0.1.7\n")
	time.sleep(0.2)
	news = input("\nSee what was added (Write news):")
	time.sleep(0.2)
	print("\n")

	if news == "news":
		time.sleep(0.2)
		print("0.1.0 - Added Phone Generator. numbers / English name generator")
		time.sleep(0.2)
		print("0.1.1 - Many bugs fixed / Link generation added")
		time.sleep(0.2)
		print("0.1.2 - Changed generator names / Added Randomizer for numbers from 1 to 10")
		time.sleep(0.2)
		print("0.1.3 - Bug fixes")
		time.sleep(0.2)
		print("0.1.4 - Added Nickname generator / Password generator / Mail generator\n")
		time.sleep(0.2)
		print("0.1.5 - Added Random Street Generator")
		time.sleep(0.2)
		print("0.1.6 - Bug fixes")
		time.sleep(0.2)
		print("0.1.7 - Name changes")
		time.sleep(0.2)

		input("\nPress Enter to exit..")


if command == "2":
	time.sleep(0.2)

	print(Fore.RESET + "\nGenerating phone numbers...\n")

	phone = input("How many phone numbers do you want to generate:")
	phone = int(phone)
	
	for i in range(phone):
		print(faker.phone_number())
		time.sleep(0.5)

	input("\nPress Enter to exit..")
		

if command == "3":
	time.sleep(0.2)

	print(Fore.RESET + "\nGeneration of bank cards\n")

	m = input("How many bank numbers do you want to generate? cards:")
	m = int(m)
	for i in range(m):
		a = random.randint(0000000000000000, 9999999999999999)
		u = random.randint(000, 999)
		print("\n")
		print(a)
		time.sleep(0.2)
		print(u)
		time.sleep(0.2)

	input("\nPress Enter to exit..")


if command == "6":
	time.sleep(0.2)

	print(Fore.RESET + "\nPersonality generator...")

	profe = input("\nHow much do you want to generate:")
	profe = int(profe)
	
	for a in range(profe):
		print("\n")
		print("Имя: " + faker.name())
		time.sleep(0.2)
		print("Адрес: " + faker.address())
		time.sleep(0.2)
		print("Город: " + faker.city())
		time.sleep(0.2)
		print("Страна: " + faker.country())
		time.sleep(0.2)
		print("Работа: " + faker.job())
		time.sleep(0.2)

	input("\nPress Enter to exit..")
		
		
if command == "7":
	time.sleep(0.2)

	print(Fore.RESET + "\nGeneration of mail...\n")

	numbber = input("Введите количесво почт: ")
	numbber = int(numbber)

	for d in range(numbber):
		print(faker.ascii_free_email())
		time.sleep(0.2)

	input("\nPress Enter to exit..")

		
if command == "8":
	time.sleep(0.2)

	print(Fore.RESET + "\nGenerating links")

	web = input("\nHow many links do you want to generate:")
	web = int(web)
		
	for g in range(web):
		print(faker.uri())
		time.sleep(0.2)

	input("\nPress Enter to exit..")

			
if command == "4":
	time.sleep(0.2)

	print(Fore.RESET + "\nRandom numbers from 0 to 9999999999\n")
	time.sleep(0.1)
	randomm = input("How many numbers do you want to output:")
	randomm = int(randomm) 
		
	for h in range(randomm):
		h = random.randint(0, 9999999999)
		print(h)
		time.sleep(0.2)

	
	input("\nPress Enter to exit..")


if command == "9":
	print(Fore.RESET + "\nGenerating names\n")

	name = input("How many names do you want to generate:")
	name = int(name)
		
	for i in range(name):
		print(faker.name())
		time.sleep(0.2)

	input("\nPress Enter to exit..")
		

if command == "5":
	time.sleep(0.2)
	
	print(Fore.RESET + "Password generation...\n")
	
	chars = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
	number = input("Количество паролей: ")
	length = input("Длинна пароля: ")
	print("\n")
	number = int(number)
	length = int(length)
	for n in range(number):
		password=''
		for i in range(length):
			password += random.choice(chars)
		print(password)
		time.sleep(0.2)
	
	input("\nPress Enter to exit..")
	

if command == "10":
	time.sleep(0.2)
	
	numbers = random.randint(1, 10)
	print(numbers)

	input("\nPress Enter to exit..")
	

if command == "11":
	time.sleep(0.2)

	print(Fore.RESET + "Nickname generator...")

	char = "abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
	nnumber = input("\nNumber of nicknames:")
	llengeth = input("Nickname length:")
	print("\n")
	nnumber = int(nnumber)
	llengeth = int(llengeth)
	for p in range(nnumber):
		nick=''
		for i in range(llengeth):
			nick += random.choice(char)
		print(nick)
		time.sleep(0.2)

	input("\nPress Enter to exit..")


if command == "12":
	time.sleep(0.3)
	print(Fore.RESET + "\nLast name generation")
	
	fam = input("Number of surnames: ")
	fam = int(fam)
	for f in range(fam):
		print(faker.last_name())
		time.sleep(0.2)

	input("\nPress Enter to exit..")
		

if command == "13":
	time.sleep(0.2)
	print(Fore.RESET + "\nStreet randomizer\n")
	
	ul = input("Number of streets:")
	ul = int(ul)
	for h in range(ul):
		print(faker.street_address())
		time.sleep(0.2)

	input("\nPress Enter to exit..")
		
	
if command == "14":
	print(Fore.RESET + "Exiting the software...")
