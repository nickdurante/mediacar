import vlc


def player_init():
	instance = vlc.Instance()
	player = instance.media_player_new()
	return player, instance

def load_file(player, instance, path):
	media = instance.media_new(path)
	player.set_media(media)

#player.play()