import sys
import re
import json

from pdfminer.high_level import extract_text

def main():
	
	fileName = None

	try:
		fileName = sys.argv[1]
	except:
		print("Specify File Name")
		return

	all_pages_text = extract_text(fileName)
	#print(all_pages_text)

	lines = all_pages_text.split('\n')
	lines = list(filter(lambda a: a != "",lines))

	#Regular Expressions
	question_pattern = r'\d\.'

	option_patterns = {
	'option1': r'\(1\).',
	'option2': r'\(2\).',
	'option3': r'\(3\).',
	'option4': r'\(4\).',
	}

	answer_pattern = r'Sol\. Answer[\.]*'

	data = []

	#Populate Questions
	no_of_lines = len(lines)
	for i in range(no_of_lines):
		res = re.search(question_pattern,lines[i])
		if(i+1<no_of_lines and len(lines[i])<=3):
			lines[i] += ' '+lines[i+1]
		if(res):
			data.append({'question':lines[i]})

	# Populate Options
	for option,pattern in option_patterns.items():
		ind = 0
		for i in range(no_of_lines):
			res = re.search(pattern,lines[i])
			if(i+1<no_of_lines and len(lines[i])<=3):
				lines[i] += ' '+lines[i+1]
			if(res and ind < len(data)):
				data[ind][option] = lines[i]
				ind += 1

	# Populate Anwers
	ind = 0
	for i in range(no_of_lines):
		res = re.search(answer_pattern,lines[i])
		if(res):
			data[ind]['answer'] = lines[i]
			ind += 1

	data = json.dumps(data, indent=4, sort_keys=True)
	
	print(data)



if __name__=="__main__":
    main()