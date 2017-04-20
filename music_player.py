import RPi.GPIO as GPIO
import subprocess
import time
from obd_display import print_red, print_green
import glob
import vlc_player
#apt-get install python-dbus

songs = glob.glob('/home/pi/music/*.mp3')
index = 0

def switch_init():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def helper():
	text = '1) Play/Pause song\n2) Next song\n3) Previous song\n4) Vol +\n5) Vol -\n8) Exit'
	print_red(text)


def main():
	index = 0
	count = 0
	helper()
	switch_init()
	player, instance = vlc_player.player_init()
	vlc_player.load_file(player, instance, songs[0])

	while True:
		if index >= len(songs):
			index = 0
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
			if count == 1:
				print_green("Pause")
				player.pause()
				count = 0;
			elif count == 0:
				print_green("Play")
				print_red("Playing: " + songs[index].strip('/home/pi/music/'))
				player.play()
				count = 1
		if s2 == False:
			time.sleep(0.2)
			print_green("Next")
			player.pause()
			count = 0
			index += 1
			vlc_player.load_file(player, instance, songs[index])

		if s3 == False:
			time.sleep(0.2)
			print_green("Previous")
			player.pause()
			count = 0
			index -= 1
			vlc_player.load_file(player, instance, songs[index])

		if s4 == False:
			time.sleep(0.2)
			print_red("Vol +")
			player.audio_set_volume(110)
		if s5 == False:
			time.sleep(0.2)
			print_red("Vol -")
			player.audio_set_volume(90)
		if s8 == False:
			time.sleep(0.2)
			print_red("Exiting...")
			player.stop()
			return


if __name__ == '__main__':
	main()



