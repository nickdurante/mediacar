import sys
import time
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format
init(strip=not sys.stdout.isatty())

#pip3 install termcolor
#pip3 install colorama
#pip3 install git+https://github.com/pwaller/pyfiglet
#text = 'HOLA'
# fonts: doh, colossal, banner3

def print_fancy(text):
	cprint(figlet_format(str(text), font = 'banner3'), 'red', 'on_blue', attrs=['bold'])

def print_carriage_ret():
	i = 1
	while i < 50:
		print("\033c")		#probably better than call(['clear'])
		n = 'I => ' + str(i)
		text = figlet_format(n, font = 'banner3')
		cprint(text, 'red', attrs=['bold'])
		time.sleep(0.5)
		i += 1


def main():
	
	#print_carriage_ret()
	while True:
		text = str(input("Enter text:\n"))
		if text == 'exit':
			return
		print_fancy(text)

if __name__ == '__main__':
		main()	
	