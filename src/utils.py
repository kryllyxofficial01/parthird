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

	elif type == "level":
		info = response.split("#")
		values = info[0].split(":")

		level_info = {}
		headers = values[::2]
		data = values[1::2]
		
		for i in range(len(headers)):
			level_info[headers[i]] = data[i]

		song_info = info[2]
		song_info = song_info.split("~|~")

		song = {}
		headers = song_info[::2]
		data = song_info[1::2]

		for i in range(len(headers)):
			song[headers[i]] = data[i]
		
		return level_info, song

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
		creators = []

		for creator in creator_info:
			creators.append(creator.split(":")[1])

		return values, creators