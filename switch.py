#!/usr/bin/python3
print("Loading...")
import RPi.GPIO as GPIO
import time
import subprocess
import obd_display
import music_player
obd_display.print_green("Loading complete")
def main():
	GPIO.setmode(GPIO.BCM)

	GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)

	flag_clock = flag_music = 1
	helper()

	while True:
		s1 = GPIO.input(16)
		s2 = GPIO.input(12)
		s3 = GPIO.input(13)
		s4 = GPIO.input(20)
		s5 = GPIO.input(6)
		s6 = GPIO.input(21)
		s7 = GPIO.input(26)
		s8 = GPIO.input(19)

		if s1 == False:
			time.sleep(0.2)
			print('Button 1 pressed')
			obd_display.main()
		if s2 == False:
			time.sleep(0.2)
			print("Button 2 pressed")
			if flag_clock == 1:
				flag_clock = 0
				clock = subprocess.Popen(['tty-clock','-sSc'])
			elif flag_clock == 0:
				clock.terminate()
				subprocess.call(['clear'])
				flag_clock = 1
		if s3 == False:
			time.sleep(0.2)
			obd_display.print_green('Attempting to connect to OBDII...')
			subprocess.call(['/home/pi/connect_obd.sh'])
		if s4 == False:
			time.sleep(0.2)
			music_player.main()

		if s5 == False:
			time.sleep(0.2)
			print('Button 5 pressed')
		if s6 == False:
			time.sleep(0.2)
			print('Button 6 pressed')
		if s7 == False:
			time.sleep(0.2)
			obd_display.print_red('Exiting...')
			return
		if s8 == False:
			time.sleep(0.2)
			print('Button 8 pressed')
			issue_shutdown()


def helper():
	text = "Switches:\n1) Start obd_display\n2) Show clock\n3) Connect to OBDII\n4) Play music\n7) Exit\n8) Power off"
	obd_display.print_red(text)

def issue_shutdown():
	obd_display.print_red('System will power off!\nContinue?:\n1) Yes\n8) No')
	GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	
	while True:
		s1 = GPIO.input(16)
		s8 = GPIO.input(19)

		if s8 == False:
			obd_display.print_green('Aborting...\n')
			time.sleep(1)
			return
		elif s1 == False:
			obd_display.print_red('Shutting down...\n')
			subprocess.call(["sudo", "shutdown", "now"])	


if __name__ == "__main__":
    main() 
