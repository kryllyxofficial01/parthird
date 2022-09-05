def getValues(type, response):
	if type == "level list":
		levels = []
		level = ""
		i = 0
		item_num = 0
		while True:
			if response[i] == "|":
				levels[item_num] = level
				item += 1

			elif response[i] == "#":
				break
			
			else:
				level += response[i]
				i += 1

		print(levels)