import sys
import re

from pdfminer.high_level import extract_text

def main():
	
	fileName = None
	startPage = None
	endPage = None

	try:
		fileName = sys.argv[1]
	except:
		print("Specify File Name")
		return

	all_pages_text = extract_text(fileName)
	#print(all_pages_text)

	lines = all_pages_text.split('\n')
	lines = list(filter(lambda a: a != "",lines))
	#print(lines)

	patterns = {
	'question': r'\d\..',
	'option1': r'\(1\).',
	'option2': r'\(2\).',
	'option3': r'\(3\).',
	'option4': r'\(4\).',
	}

	questions = []
	no_of_lines = len(lines)
	for i in range(no_of_lines):
		res = re.search(patterns['question'],lines[i])
		if(res):
			questions.append(lines[i])
	print(questions)

	option1 = []
	for i in range(no_of_lines):
		res = re.search(patterns['option1'],lines[i])
		if(len(lines[i])<=3 and i+1<no_of_lines):
			lines[i] += ' '+lines[i+1]
		if(res):
			option1.append(lines[i])
	print(option1)

	option2 = []
	for i in range(no_of_lines):
		res = re.search(patterns['option2'],lines[i])
		if(len(lines[i])<=3 and i+1<no_of_lines):
			lines[i] += ' '+lines[i+1]		
		if(res):
			option2.append(lines[i])
	print(option2)

	option3 = []
	for i in range(no_of_lines):
		res = re.search(patterns['option3'],lines[i])
		if(len(lines[i])<=3 and i+1<no_of_lines):
			lines[i] += ' '+lines[i+1]		
		if(res):
			option3.append(lines[i])
	print(option3)

	option4 = []
	for i in range(no_of_lines):
		res = re.search(patterns['option4'],lines[i])
		if(len(lines[i])<=3 and i+1<no_of_lines):
			lines[i] += ' '+lines[i+1]
		if(res):
			option4.append(lines[i])
	print(option4)



if __name__=="__main__":
    main()