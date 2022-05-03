lines = []
b = True
while b:
    try :
        lines.append(input())
    except:
        b = False


syntax_error_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
resMap = {')':0, ']':0, '}':0, '>':0}
openers = '({[<'
closers = ')}]>'

closing_brackets = {cl:op for op,cl in zip(openers, closers)}
opening_brackets = {op:cl for op,cl in zip (openers, closers)}



def find_mismatch(text:str) -> str:
    stack = []

    for char in text:
        if char in openers:
            stack.append(char)
        elif char in closers:
            popped = stack.pop()
            if closing_brackets[char] != popped:
                return char

scores = []
for line in lines:
    incorrect_char = find_mismatch(line)
    if incorrect_char is not None:
        scores.append(syntax_error_scores[incorrect_char])

print(sum(scores))