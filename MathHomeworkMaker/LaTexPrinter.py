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
    parser.add_argument('--number-of-questions', '-n', action="store", required=False, type=str, help='Number of questions you want to generate')
    parser.add_argument('--output-file-name', '-o', action="store", required=False, type=str,help='Output file name with timestamp')

    return parser.parse_args()


def main():
    # Generate Problems
    args = parse_args()

    print(args)

    if args.number_of_questions is not None:
        number_of_questions = args.number_of_questions
    else:
        number_of_questions = input('Please Enter Number of Questions (Default 100): ')

    if args.output_file_name is not None:
        file_name = args.output_file_name + ' ' + time.strftime("%Y%m%d%H%M%S")
    else:
        file_name = 'ProblemSet ' + time.strftime("%Y%m%d%H%M%S")

    f = open('output/' + file_name + '.tex', 'w')
    fa = open('output/' + file_name + '_Answer.tex', 'w')

    temp = open('template/head', 'r')
    for line in temp:
        f.write(line)
        fa.write(line)

    if int(number_of_questions) < 1:
        number_of_questions = 100

    LaTexProblemGenerator.generateQuestions(int(number_of_questions), f, fa, file_name)

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
    printout = [file_name, file_name + '_Answer']

    for x in printout:
        proc = subprocess.Popen(['pdflatex', current + '/output/' + x + '.tex'])
        subprocess.Popen(['pdflatex', current + '/output/' + x + '.tex'])
        proc.communicate()

        shutil.copy(x + '.pdf', current + '/output')

    shutil.rmtree(temp)


if __name__ == "__main__":
    main()
