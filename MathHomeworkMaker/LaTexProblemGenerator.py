from random import randint


class Formula:
    num1 = 0
    num2 = 0
    ans = 0.0
    operation = ["+", "-", "\\times", "\\div"]
    oCode = 0

    def swap(self):
        x = self.num1
        self.num1 = self.num2
        self.num2 = x

    def getAnswer(self):
        if self.oCode == 0:
            self.ans = self.num1 + self.num2
        if self.oCode == 1:
            self.ans = self.num1 - self.num2
        if self.oCode == 2:
            self.ans = self.num1 * self.num2
        if self.oCode == 3:
            self.ans = self.num1 / self.num2

    def printFormula(self):
        return "{} {} {} =".format(self.num1, self.operation[self.oCode], self.num2)


def generateQuestions(x, problemSet, problemSetAns, file_name):
    i = 0
    j = 0
    while i < x:
        problem = Formula()
        problem.num1 = randint(0, 100)
        problem.num2 = randint(0, 100)
        problem.oCode = randint(0, 3)

        while problem.oCode < 2 and problem.num2 < 10:
            problem.num2 = randint(10, 100)

        if problem.num2 > problem.num1:
            problem.swap()

        while 1 < problem.oCode < 4 and (problem.num2 < 2 or problem.num2 > 10):
            problem.num2 = randint(2, 10)

        problem.getAnswer()
        ans = "{:.2f}".format(problem.ans)
        if ans[len(ans) - 3:len(ans)] == ".00":
            ans = ans[:-3]

        if j % 35 == 0:
            problemSet.write("{}\\\\\n".format(file_name))
            problemSetAns.write("{}\\\\\n".format(file_name))

            problemSet.write("\\begin{enumerate}[resume]\n")
            problemSetAns.write("\\begin{enumerate}[resume]\n")

        problemSet.write("  \item ${}$\n".format(problem.printFormula()))
        problemSetAns.write("  \item ${}{}$\n".format(problem.printFormula(), ans))

        i += 1
        j += 1

        if j % 35 == 0 and not x % 35 == 0:
            problemSet.write("\\end{enumerate}\n")
            problemSetAns.write("\\end{enumerate}\n")
