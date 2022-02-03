from logging import raiseExceptions


class exa:
    def __init__(self):
        self.x = 0
        self.t = 0
    


    def read_lines(lines):
        # ignore empty lines
        if lines == None:
            pass
        else:
            exp = list(lines.strip().split())[0], list(lines.strip().split())[1:]
            #b = list(lines.strip().split())
            #exp = b[0], b[1:]
            for item in exp[1:]:
                if item not in ['X, T'] or not str(item).isdigit():
                    print('Invalid code')
                    break
                if str(item).isdigit() == True:
                    item = int(item)
                    print(item)
                    print(type(item))
            return exp

    def func_copy(self, value, reg):
        if reg == 'X':
            self.x = value
            return self.x 
        if reg == 'T':
            self.t = value
            return self.t 
        else:
            raiseExceptions
    
    def func_addi(self, value1, value2, reg):
        pass



