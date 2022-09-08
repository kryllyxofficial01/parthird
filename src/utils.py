def getValues(response, type):
	if type == "user":
		info = response.split("#")
		values = info[0].split(":")

		user_info = {}
		headers = values[::2]
		data = values[1::2]
		
		for i in range(len(headers)):
			user_info[headers[i]] = data[i]

		return user_info

	elif type == "levels":
		info = response.split("#")
		levels = info[0].split("|")

		values = []
		level_values = {}

		for level in levels:
			level = level.split(":")
			headers = level[::2]
			data = level[1::2]

			for i in range(len(headers)):
				level_values[headers[i]] = data[i]

			values.append(level_values)
			level_values = {}
		
		creator_info = info[1].split("|")
		song_info = info[2].split("~:~")

		creators = []
		for creator in creator_info:
			creators.append(creator.split(":")[1])
		
		songs = []
		song_values = {}

		for song in song_info:
			song = song.split("~|~")
			headers = song[::2]
			data = song[1::2]

			for i in range(len(headers)):
				song_values[headers[i]] = data[i]
			
			songs.append(song_values)
			song_values = {}

		return values, creators, songs