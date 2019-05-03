from random import randint

class Formula():
    num1 = 0
    num2 = 0
    ans = 0.0
    operation = ['+', '-', '\\times', '\\div']
    oCode = 0

    def swap(self):
        x = self.num1
        self.num1 = self.num2
        self.num2 = x

    def getanswer(self):
        if self.oCode == 0:
            self.ans = self.num1 + self.num2
        if self.oCode == 1:
            self.ans = self.num1 - self.num2
        if self.oCode == 2:
            self.ans = self.num1 * self.num2
        if self.oCode == 3:
            self.ans = self.num1 / self.num2

    def printformula(self):
        return '%i %s %i =' % (self.num1, self.operation[self.oCode], self.num2)


def generateQuestions(x, problemSet, problemSetAns):
    i = 0
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

        problem.getanswer()
        ans = ' %.2f' % problem.ans
        if ans[len(ans) - 3:len(ans)] == '.00':
            ans = ans[:-3]

        problemSet.write('  \item $' + problem.printformula() + '$\\\\\n')
        problemSetAns.write('  \item $' + problem.printformula() + ans + '$\\\\\n')
        i += 1
