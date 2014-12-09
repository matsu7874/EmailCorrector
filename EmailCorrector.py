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
        rules.update({'o':['o', '0']})
        rules.update({'i':['i', 'j', 'l', '1']})
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
        for x in itertools.product(*self.construct_suggestion_array(self.separate_chars(fuzzy))):
            suggestions.append("".join(x))
        return suggestions

def main():
    fuzzyEmail = input()
    corrector = Corrector()
    for x in corrector.suggest(fuzzyEmail):
        print(x)

if __name__ == '__main__':
  main()