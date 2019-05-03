import LaTexProblemGenerator
import subprocess
import os
import tempfile
import shutil
import time

# Generate Problems
numberOfQuestions = input('Please Enter Number of Questions: ')
fileName = 'ProblemSet' + time.strftime("%Y%m%d%H%M%S")

f = open('output/' + fileName + '.tex', 'w')
fa = open('output/' + fileName + 'Ans.tex', 'w')

temp = open('template/head', 'r')
for line in temp:
    f.write(line)
    fa.write(line)

LaTexProblemGenerator.generateQuestions(int(numberOfQuestions), f, fa)

temp = open('template/tail', 'r')
for line in temp:
    f.write(line)
    fa.write(line)

temp.close()
f.close()
fa.close()

# Compile LaTex File
current = os.getcwd()
temp = tempfile.mkdtemp()
os.chdir(temp)
printout = [fileName, fileName + 'Ans']

for x in printout:
    proc = subprocess.Popen(['pdflatex', current + '/output/' + x + '.tex'])
    subprocess.Popen(['pdflatex', current + '/output/' + x + '.tex'])
    proc.communicate()

    shutil.copy(x + '.pdf', current + '/output')

shutil.rmtree(temp)
