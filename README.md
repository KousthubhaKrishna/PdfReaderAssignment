# PdfReaderAssignment
<b>task.py</b> file contains a python program which extracts questions, multi choice options and answers from the given pdf.<br/>
The dependencies for the program are specified in <b>requirements.txt</b> file.<br/>
I used 3 inbuilt python modules and one additional python package(PdfMiner) that helps in reading pdf files.<br/>
The final output is a json array of questions along with options and answers.

### Instructions to run the file
1. Install PdfMiner with below command or use requirements.txt
```bash
pip3 install pdfminer.six
```
2. Run the task.py file and specify pdf file name as a cmd line argument.
```bash
python3 task.py The_Living_World.pdf
```

