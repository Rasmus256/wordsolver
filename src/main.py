import os

inputs = os.getenv("INPUTS").replace("[", "").replace("]", "").split(" ")

print(f"was given these ínputs: {inputs}")
operands = inputs[:len(inputs)-1]
result = inputs[len(inputs)-1:]

print(f"started with these operands: {operands}, result: {result}")

def calculateSum(name, translations):
    sum = 0
    for idx, l in enumerate(name[::-1]):
      sum = sum + translations[l]*pow(10, idx)
    return sum
def determineWhetherMatch(translations):
    global operands, result
    sum_of_operands = []
    for op in operands:
        sum_of_operands.append(calculateSum(op, translations))
    return sum(sum_of_operands) == calculateSum(result, translations)
def iterateoverLetters(letters, translations, level):
    if len(letters) == 0:
        if determineWhetherMatch(translations):
            print(translations)
    if len(letters) >0:
        for i in range(10):
            tr = translations.copy()
            tr[letters[0]] = i
            iterateoverLetters(letters[1::], tr, level+1)

letters = list(set(''.join(inputs)))
letters.sort()

print(f"These are the unique letters that we will look at for your input: {letters}")
translations = {}
for i in letters:
    translations[i] = 0

iterateoverLetters(letters, translations, 0)
