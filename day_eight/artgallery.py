


	#print(file)

	

def traffic():
	with open("traffic.txt", "r") as f:
		traffic = [data.strip() for data in f]
		print(traffic)


d = {}
for client, room_number, direction, time in traffic:
	if not room_number in d:
		d[room_number] = [-int(time)]
	else:
		d[room_number].append(-int(time)) if direction == "I" else int(time)
for number in d.items():
	visitor = int(len(number[1]) //2)

traffic()



