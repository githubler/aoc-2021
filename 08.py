#day 08


def get_input():
    with open('2021/08 input.txt') as f:
        return [x.strip() for x in f.readlines()]


#
#part 1
#
sum = 0
for line in get_input():
    input, output = line.split('|')
    signal_patterns = [str(x) for x in output.split()]
    for signal_pattern in signal_patterns:
        if len(signal_pattern) == 2 or len(signal_pattern) == 3 or len(signal_pattern) == 4 or len(signal_pattern) == 7:
            sum += 1

print("Submit part 1:", sum)



#
#part 2
#
def contains(str, pattern) -> bool:
    text = [s for s in str if s in pattern]
    return len(text) == len(str)

def is_remapping(str, pattern) -> bool:
    text = [s for s in str if s in pattern]
    return len(text) == len(str) == len(pattern)


sum = 0
for line in get_input():
    mapping = ['', '', '', '', '', '', '', '', 'abcdefg', '']

    input, output = line.split('|')

    input_patterns = [str(x) for x in input.split()]
    for pattern in input_patterns:
        if len(pattern) == 2:
            mapping[1] = pattern
        elif len(pattern) == 3:
            mapping[7] = pattern
        elif len(pattern) == 4:
            mapping[4] = pattern
        elif len(pattern) == 7:
            mapping[8] = pattern

    # create pattern to distinguish existing patterns
    left_mid = ''.join( x for x in mapping[4] if x not in mapping[1])

    for pattern in input_patterns:
        if len(pattern) == 5:
            if contains(mapping[1], pattern):
                mapping[3] = pattern
            elif contains(left_mid, pattern):
                mapping[5] = pattern
            else:
                mapping[2] = pattern
        elif len(pattern) == 6:
            if contains(mapping[4], pattern):
                mapping[9] = pattern
            elif contains(mapping[1], pattern):
                mapping[0] = pattern
            else:
                mapping[6] = pattern

    output_patterns = [str(x) for x in output.split()]
    output_value = ''
    for pattern in output_patterns:
        for n in range(10):
            if is_remapping(mapping[n], pattern):
                output_value += str(n)

    if len(output_value) < 4:
        print("ERROR: ", output_value)
        
    sum += int(output_value)

print("Submit part 2:", sum)