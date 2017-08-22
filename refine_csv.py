import re

def find_matches(text):
	matches=re.findall(r'\"(.+?)\"',text)
	return matches

def replace(file, file2, f1):
	r = []
	l = len(file2) 
	lcount = 2
	count = 0
	for line in file:
		if count % 7 == 2:
			line2 = file2[l-lcount]
			lcount += 1
			line = find_matches(line)
			if len(line) > 0:
				date = line[0].split(',')
				[month, day] = date[0].split()
				year = date[1].strip()[2:]
				price = line[1].replace(',', '')
				new_line = day + '-' + month + '-' + year + ',' + price + ',' + line2.split(',')[1]
				f1.write(new_line + '\n')
		count += 1
	return r

f = open('bitcoin_price.csv', 'r').read().split('\n')
f2 = open('bitcoin_search.csv', 'r').read().split('\n')
f1 = open('new_file.csv', 'w')
f1.write('date,price,search\n')
res = replace(f, f2, f1)
