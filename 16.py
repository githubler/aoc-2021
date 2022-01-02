#day 16

from functools import reduce


def get_input():
    with open('2021/16 input.txt') as f:
        return [x.strip() for x in f.readlines()]


def to_num(message):
    num = 0
    bit_string = ''
    for bit in message:
        bit_string += bit
    num = int(bit_string, 2)
    return num


def consume_message(message, count):
    for _ in range(count):
        message.pop(0)


def decode_literal_value(message):
    value = 0
    literal_value = ''
    i = 0
    for _ in range(len(message)):
        if message[i] == '1':
            for bit in message[i+1:i+5]:
                literal_value += bit
            i += 5
        elif message[i] == '0':
            for bit in message[i+1:i+5]:
                literal_value += bit
            consume_message(message, i+5)
            break
    value = (int(literal_value, 2))
    return value


def decode_operator(message, type_id):
    length_type_id = message[0]
    sub_packets = []
    if length_type_id == '0':
        sub_packets_length = to_num(message[1:16])
        consume_message(message, 16)
        message_length = len(message)
        while len(message) > message_length - sub_packets_length:
            sub_packets.append(decode_sub_packets(message))
    else:
        num_sub_packets = to_num(message[1:12])
        consume_message(message, 12)
        for _ in range(num_sub_packets):
            sub_packets.append(decode_sub_packets(message))

    result = 0
    if type_id == 0:
        result = sum(sub_packets)
    elif type_id == 1:
        result = reduce((lambda x, y: x * y), sub_packets)
    elif type_id == 2:
        result = min(sub_packets)
    elif type_id == 3:
        result = max(sub_packets)
    elif type_id == 5:
        result = int(sub_packets[0] > sub_packets[1])
    elif type_id == 6:
        result = int(sub_packets[0] < sub_packets[1])
    elif type_id == 7:
        result = int(sub_packets[0] == sub_packets[1])

    return result


def decode_sub_packets(message):
    global sum_version_numbers
    result = 0
    packet_version = to_num(message[:3])
    sum_version_numbers += packet_version
    type_id = to_num(message[3:6])
    consume_message(message, 6)

    if type_id == 4:
        result = decode_literal_value(message)
    else:
        result = decode_operator(message, type_id)

    return result


def decode_message(message):
    num_of_bits = 4
    bin_message = []

    for c in message:
        binary = bin(int(c, 16))[2:].zfill(num_of_bits)
        for bit in binary:
            bin_message.append(bit)

    #print(message, " -> ", bin_message)
    result = decode_sub_packets(bin_message)
    return result


#
# part 1 & 2
#
sum_version_numbers = 0

lines = get_input()
result = decode_message(lines[0])
print("Submit - sum version numbers: ", sum_version_numbers)
print("Submit - calculation: ", result)
