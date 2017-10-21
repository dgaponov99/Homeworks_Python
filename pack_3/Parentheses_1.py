class Parentheses:
    def __init__(self, stroka):
        self.s = stroka

    def rightParentheses(self):
        while len(self.s) > 0:
            f1 = True
            f2 = True
            f3 = True
            n1 = self.s.find(')')
            if n1 > 0:
                if self.s[n1 - 1] == '(':
                    self.s = self.s[0:n1 - 1] + self.s[n1 + 1:]
            else:
                f1 = False
            n2 = self.s.find(']')
            if n2 > 0:
                if self.s[n2 - 1] == '[':
                    self.s = self.s[0:n2 - 1] + self.s[n2 + 1:]
            else:
                f2 = False
            n3 = self.s.find('}')
            if n3 > 0:
                if self.s[n3 - 1] == '{':
                    self.s = self.s[0:n3 - 1] + self.s[n3 + 1:]
            else:
                f3 = False
            if not(f1 and f2 and f3):
                break
        if len(self.s) != 0:
            print("String isn't validity")
        else:
            print("String is validity")


s = input("Введите строку: ")
a = Parentheses(s)
a.rightParentheses()