import itertools

class Corrector(object):
    def __init__(self, rules=None):
        if rules is None:
            self.rules = self.make_default_rules()
        else:
            self.rules = rules

    def make_default_rules(self):
        rules = {}
        rules.update({'a':['a', 'u']})
        rules.update({'b':['b']})
        rules.update({'c':['c']})
        rules.update({'d':['d']})
        rules.update({'e':['e', 'c']})
        rules.update({'f':['f']})
        rules.update({'g':['g']})
        rules.update({'h':['h']})
        rules.update({'i':['i', 'j', 'l', '1']})
        rules.update({'j':['j', 'i']})
        rules.update({'k':['k']})
        rules.update({'l':['l', '1', 'i']})
        rules.update({'m':['m', 'nn', 'rn']})
        rules.update({'n':['n', 'r']})
        rules.update({'o':['o', '0']})
        rules.update({'p':['p']})
        rules.update({'q':['q', '9']})
        rules.update({'r':['r', 'n']})
        rules.update({'s':['s', '5']})
        rules.update({'t':['t']})
        rules.update({'u':['u', 'v']})
        rules.update({'v':['v', 'u']})
        rules.update({'w':['w', 'vv']})
        rules.update({'x':['x']})
        rules.update({'y':['y']})
        rules.update({'z':['z', '2']})

        rules.update({'0':['0', 'u']})
        rules.update({'1':['1', '7', 'l']})
        rules.update({'2':['2', 'z']})
        rules.update({'3':['3']})
        rules.update({'4':['4']})
        rules.update({'5':['5', 's']})
        rules.update({'6':['6']})
        rules.update({'7':['7', '1']})
        rules.update({'8':['8']})
        rules.update({'9':['9', 'g', 'q']})

        rules.update({'-':['-', '_']})
        rules.update({'_':['_', '-']})
        rules.update({'.':['.', '']})
        return rules

    def separate_chars(self, string):
        chars = []
        for c in string:
            chars.append(c)
        return chars

    def construct_suggestion_array(self, chars):
        suggestion_array = []
        for c in chars:
            if c in self.rules:
                suggestion_array.append(self.rules[c])
            else:
                suggestion_array.append([c])
        return suggestion_array

    def suggest(self, fuzzy):
        suggestions = []
        (fuzzylocal, fuzzydomain) = fuzzy.split('@')
        for x in itertools.product(*self.construct_suggestion_array(self.separate_chars(fuzzylocal))):
            suggestions.append("".join(x) + '@' + fuzzydomain)
        return suggestions

def main():
    fuzzyEmail = input()
    corrector = Corrector()
    for x in corrector.suggest(fuzzyEmail):
        print(x)

if __name__ == '__main__':
  main()