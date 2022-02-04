https://prod.liveshare.vsengsaas.visualstudio.com/join?A88E288BE6D7B2FEB45DA35E5A7C4849E47C

from logging import raiseExceptions


class exa:
    def __init__(self):
        self.x = 0
        self.t = 0
    
    
    
    def read_lines(self, lines):
        # ignore empty lines
        if lines == '': # None? 
            pass
        else:
            reading = list(lines.strip().split())
            arg_new = []
            instruction_list = list('COPY ADDI SUBI MULI DIVI MODI'.split())
            if reading[0] not in instruction_list:
                print('Invalide instruction.  CRASH  !!!')
                pass
            else:
                for item in reading[1:]:
                    #print('item is: ', item)
                    if item not in ['X', 'T'] and not str(item).isdigit():
                        print('Invalid code! CRASH!!!')
                        break
                    if str(item).isdigit() is True:
                        item = int(item)
                    arg_new.append(item)
                    #print('new list is: ', arg_new)
                exp = reading[0], arg_new
                return exp

    def func_copy(self, value, reg):
        if reg == 'X':
            self.x = value
            return self.x 
        elif reg == 'T':
            self.t = value
            return self.t 
        else:
            raiseExceptions
    
    def func_addi(self, value1, value2, reg):
        pass



