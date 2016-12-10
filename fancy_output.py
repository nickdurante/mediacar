import sys
import time
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint
from pyfiglet import figlet_format
#pip3 install termcolor
#pip3 install colorama
#pip3 install git+https://github.com/pwaller/pyfiglet
#text = 'HOLA'
# fonts: doh, colossal, banner3

def print_fancy(text):
	cprint(figlet_format(text, font = 'banner3'), 'red', 'on_blue', attrs=['bold'])

def print_carriage_ret():
	i = 1
	while 1 < 50:
		print("\033c")		#probably better than call(['clear'])
		n = 'I => ' + str(i)
		text = figlet_format(n, font = 'banner3')
		cprint(text, 'red', attrs=['bold'])
		time.sleep(0.5)
		i += 1


def main():
	
	print_carriage_ret()
	print('Enter text')
	text = input()
	print_fancy(text)

if __name__ == '__main__':
		main()	
	