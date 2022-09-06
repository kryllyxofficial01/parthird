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