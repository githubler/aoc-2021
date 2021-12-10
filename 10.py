#day 10

from bisect import insort


def get_input():
    with open('2021/10 input.txt') as f:
        return [x.strip() for x in f.readlines()]


def build_input():
    input = []
    for line in get_input():
        input.append([x for x in line])
    return input


#
# part 1 & 2
#

def calc_score(c) -> int:
    score = 0
    if c == ')':
        score += 3
    if c == ']':
        score += 57
    if c == '}':
        score += 1197
    if c == '>':
        score += 25137

    return score


input = build_input()
score1 = 0
scores = []
for line in input:
    invalid = False
    stack = []
    for c in line:
        if c == ')' or c == ']' or c == '}' or c == '>':
            last_open = stack.pop()
            if last_open == '(':
                if c != ')':
                    score1 += calc_score(c)
                    invalid = True
                    break
            elif last_open == '[':
                if c != ']':
                    score1 += calc_score(c)
                    invalid = True
                    break
            elif last_open == '{':
                if c != '}':
                    score1 += calc_score(c)
                    invalid = True
                    break
            elif last_open == '<':
                if c != '>':
                    score1 += calc_score(c)
                    invalid = True
                    break
        else:
            stack.append(c)
    
    # score for part 2
    if not invalid:
        score2 = 0
        for i in range(len(stack)):
            c = stack[-(i+1)]
            score2 *= 5
            if c == '(':
                score2 += 1
            if c == '[':
                score2 += 2
            if c == '{':
                score2 += 3
            if c == '<':
                score2 += 4
        insort(scores, score2)

            
print("Score 1: ", score1)
print("Score 2: ", scores[int(len(scores)/2)])