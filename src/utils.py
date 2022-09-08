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

		return values