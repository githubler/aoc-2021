#day 16


from os import curdir


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
    #print(message)
    value = 0
    literal_value = ''
    i = 0
    for _ in range(len(message)):
        print(i, message[i], message[i+1:i+5])
        if message[i] == '1':
            for bit in message[i+1:i+5]:
                literal_value += bit
            i += 5
        elif message[i] == '0':
            for bit in message[i+1:i+5]:
                literal_value += bit
            consume_message(message, i+5)
            break
    #print(literal_value)
    value = (int(literal_value, 2))
    return value #, consumed_bits


def decode_operator(message, type_id):
    result = 0
    length_type_id = message[0]
    if length_type_id == '0':
        sub_packets_length = to_num(message[1:16])
        consume_message(message, 16)
        message_length = len(message)
        #while sub_packets_length >= message_length-len(message):
        while len(message) > message_length - sub_packets_length:
            result = decode_sub_packets(message) #, length=sub_packets_length)
    else:
        num_sub_packets = to_num(message[1:12])
        consume_message(message, 12)
        for i in range(num_sub_packets):
            result = decode_sub_packets(message) #, num_sub=num_sub_packets)

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

    print("value: ", result)

    return result


def decode_message(message):
    num_of_bits = 4
    bin_message = []

    for c in message:
        binary = bin(int(c, 16))[2:].zfill(num_of_bits)
        for bit in binary:
            bin_message.append(bit)

    print(message, " -> ", bin_message)

    _ = decode_sub_packets(bin_message) #, length=len(bin_message))



#
# part 1
#
sum_version_numbers = 0

lines = get_input()
decode_message(lines[0])
print("Submit: ", sum_version_numbers)

