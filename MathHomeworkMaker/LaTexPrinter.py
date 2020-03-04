import LaTexProblemGenerator
import argparse
import subprocess
import os
import tempfile
import shutil
import time

# Create Output Directory (iff not exist)
current = os.getcwd()
if not os.path.exists(current + '/output'):
    os.makedirs(current + '/output')

def parse_args():
	parser = argparse.ArgumentParser()
	#'--input', '-i', dest='input', required=True, type=str,
    #                   help='input CSV file')
	parser.add_argument('--number-of-questions', '-n', dest='', required=False, type=str, help='Number of questions you want to generate')
	parser.add_argument('--output-file-name', '-o', , dest='', required=False, type=str,help='Output filename with timestamp')

	return parser.parse_args()


def main():
	# Generate Problems
	args = parse_args()

	if args.number_of_questions is not None:
	    numberOfQuestions = args.number_of_questions
	else:
	    numberOfQuestions = input('Please Enter Number of Questions (Default 100): ')
	
	if args.output_file_name is not None:
	    fileName = args.output_file_name + ' ' + time.strftime("%Y%m%d%H%M%S")
	else:
	    fileName = 'ProblemSet ' + time.strftime("%Y%m%d%H%M%S")
	
	f = open('output/' + fileName + '.tex', 'w')
	fa = open('output/' + fileName + '_Answer.tex', 'w')
	
	temp = open('template/head', 'r')
	for line in temp:
	    f.write(line)
	    fa.write(line)
	
	if int(numberOfQuestions) < 1:
	    numberOfQuestions = 100
	
	LaTexProblemGenerator.generateQuestions(int(numberOfQuestions), f, fa, fileName)
	
	temp = open('template/tail', 'r')
	for line in temp:
	    f.write(line)
	    fa.write(line)
	
	temp.close()
	f.close()
	fa.close()
	
	# Compile LaTex File
	temp = tempfile.mkdtemp()
	os.chdir(temp)
	printout = [fileName, fileName + '_Answer']
	
	for x in printout:
	    proc = subprocess.Popen(['pdflatex', current + '/output/' + x + '.tex'])
	    subprocess.Popen(['pdflatex', current + '/output/' + x + '.tex'])
	    proc.communicate()
	
	    shutil.copy(x + '.pdf', current + '/output')
	
	shutil.rmtree(temp)


if __name__ == "__main__":
    main()
