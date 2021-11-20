import os

class Caractere:
    nb_line: int
    nb_column: int
    carac: list

    def __init__(self,_nb_line,_nb_column,_carac):
        self.nb_column = _nb_column
        self.nb_line = _nb_line
        self.carac = _carac

    def __str__(self):
        caractere = "\n"
        for line in range (self.nb_line):
            for column in range (self.nb_column):
                caractere += self.carac[line][column]
            caractere += "\n"
        return caractere

    def __add__(self,a):
        if (self.nb_line != a.nb_line):
            raise ValueError
        else:
            L = [["" for k in range (self.nb_column + a.nb_column + 2)] for j in range(self.nb_line)]
            for j in range (self.nb_line):
                for k in range (self.nb_column):
                    L[j][k] = self.carac[j][k]
                for k in range (2):
                    L[j][self.nb_column + k] = "  "
                for k in range (a.nb_column):
                    L[j][self.nb_column + 2 + k] = a.carac[j][k]
            new_carac = Caractere(self.nb_line,self.nb_column + 2 + a.nb_column,L)
            return new_carac



def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

manette = [["  ","  ","  ","██","██","██","██","██","  ","  ","  ","  ","  ","  ","  ","██","██","██","██","██","  ","  ","  "],
           ["  ","  ","██","  ","  ","  ","  ","  ","██","██","██","██","██","██","██","  ","  ","  ","  ","  ","██","  ","  "],
           ["  ","██","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","##","██","  "],
           ["██","  ","  ","  ","██","██","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","██","██","  ","  ","##","██"],
           ["██","  ","  ","  ","██","██","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","██","██","  ","  ","##","██"],
           ["██","  ","██","██","██","██","██","██","  ","  ","  ","  ","  ","  ","  ","██","██","  ","  ","██","██","##","██"],
           ["██","  ","██","██","██","██","██","██","  ","  ","██","  ","  ","██","  ","██","██","  ","  ","██","██","##","██"],
           ["██","  ","  ","  ","██","██","  ","  ","  ","██","  ","  ","██","  ","  ","  ","  ","██","██","  ","  ","##","██"],
           ["██","  ","  ","  ","██","██","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","██","██","  ","  ","##","██"],
           ["██","  ","  ","  ","  ","  ","##","##","##","##","##","##","  ","  ","  ","  ","  ","  ","  ","  ","  ","##","██"],
           ["██","  ","  ","  ","  ","##","##","██","██","██","██","██","██","██","██","██","  ","  ","  ","  ","##","##","██"],
           ["  ","██","  ","##","##","##","██","  ","  ","  ","  ","  ","  ","  ","  ","  ","██","  ","##","##","##","██","  "],
           ["  ","  ","██","██","██","██","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","██","██","██","██","  ","  "]]
manette_carac = Caractere(13,23,manette)
#print(manette_carac)

print_M = [["██","  ","  ","  ","██"],
           ["██","██","  ","██","██"],
           ["██","  ","██","  ","██"],
           ["██","  ","██","  ","██"],
           ["██","  ","  ","  ","██"],
           ["██","  ","  ","  ","██"],
           ["██","  ","  ","  ","██"]]
m_carac = Caractere(7,5,print_M)


print_O = [["  ","██","██","██","  "],
           ["██","  ","  ","  ","██"],
           ["██","  ","  ","  ","██"],
           ["██","  ","  ","  ","██"],
           ["██","  ","  ","  ","██"],
           ["██","  ","  ","  ","██"],
           ["  ","██","██","██","  "]]
o_carac = Caractere(7,5,print_O)

print_N = [["██","  ","  ","  ","██"],
           ["██","  ","  ","  ","██"],
           ["██","██","  ","  ","██"],
           ["██","  ","██","  ","██"],
           ["██","  ","  ","██","██"],
           ["██","  ","  ","  ","██"],
           ["██","  ","  ","  ","██"]]
n_carac = Caractere(7,5,print_N)

print_P = [["██","██","██","██","  "],
           ["██","  ","  ","  ","██"],
           ["██","  ","  ","  ","██"],
           ["██","██","██","██","  "],
           ["██","  ","  ","  ","  "],
           ["██","  ","  ","  ","  "],
           ["██","  ","  ","  ","  "]]
p_carac = Caractere(7,5,print_P)

print_L = [["██","  ","  ","  ","  "],
           ["██","  ","  ","  ","  "],
           ["██","  ","  ","  ","  "],
           ["██","  ","  ","  ","  "],
           ["██","  ","  ","  ","  "],
           ["██","  ","  ","  ","  "],
           ["██","██","██","██","██"]]
l_carac = Caractere(7,5,print_L)

print_Y = [["██","  ","  ","  ","██"],
           ["██","  ","  ","  ","██"],
           ["  ","██","  ","██","  "],
           ["  ","  ","██","  ","  "],
           ["  ","  ","██","  ","  "],
           ["  ","  ","██","  ","  "],
           ["  ","  ","██","  ","  "]]
y_carac = Caractere(7,5,print_Y)

monopoly_carac = m_carac + o_carac + n_carac + o_carac + p_carac + o_carac + l_carac + y_carac

if __name__ == '__main__' :
    clearConsole()
    print("\n \n \n")
    print(manette_carac)
    print(monopoly_carac)
