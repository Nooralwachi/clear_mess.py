import re
def clear_mess(filename):
	lines={} 
	name = r'[a-zA-Z]+'
	date = r'\d{2}/\d{2}/\d{4}'
	phone = r'\d{3}-\d{3}-\d{4}'
	with open(filename) as f:
		
		for line in f:
			line = line.strip()
			names= re.search(name, line)
			dates= re.search(date, line)
			phones= re.search(phone, line)
			# print(names.group(0), phones.group(0), dates.group(0))
			lines[names.group(0)] = [names.group(0), phones.group(0), dates.group(0), '\n']
	lines_sorted= sorted(lines.items(), key = lambda item:item[0])
	with open('fixed.txt', 'w') as fw:
		fw.write('Username Phone_num Start_date\n')
		for line in lines_sorted:
			fw.write((' ').join(line[1]))
	
clear_mess('contact_list.txt')
