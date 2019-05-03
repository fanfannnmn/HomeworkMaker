import LaTexProblemGenerator
import subprocess
import os
import tempfile
import shutil
import time

# Generate Problems
numberOfQuestions = input('Please Enter Number of Questions: ')
fileName = time.strftime("%Y%m%d%H%M%S")

f = open('output/ProblemSet' + fileName + '.tex', 'w')
fa = open('output/ProblemSet' + fileName + 'Ans.tex', 'w')

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

proc = subprocess.Popen(['pdflatex', current + '/output/ProblemSet' + fileName + '.tex'])
subprocess.Popen(['pdflatex', current + '/output/ProblemSet' + fileName + '.tex'])
proc.communicate()

shutil.copy('ProblemSet' + fileName + '.pdf', current + '/output')

proc = subprocess.Popen(['pdflatex', current + '/output/ProblemSet' + fileName + 'Ans.tex'])
subprocess.Popen(['pdflatex', current + '/output/ProblemSet' + fileName + 'Ans.tex'])
proc.communicate()

shutil.copy('ProblemSet' + fileName + 'Ans.pdf', current + '/output')

shutil.rmtree(temp)
