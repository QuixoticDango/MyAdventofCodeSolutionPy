file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2021 Day 16 Advent of Code Input.txt"

def decode_message(encrypted_msg: str, version_numbers: list = None,
                   literals: list = None, packet_len: int = None, packet_num: int = None):
    if version_numbers is None:
        version_numbers = []
    
    if literals is None:
        literals = []

    code = encrypted_msg[:]
    print(f"{len(code) = }")
    if not code:
        return code, version_numbers, literals
    # print(f'{code = }')

    version = int(code[:3], 2)
    version_numbers.append(version)
    
    type_id = int(code[3:6], 2)
    code = code[6:]
    
    # Literal value
    if type_id == 4:
        print("TYPE 4")
        if packet_len:
            lst = []
            bits_used = 0
            while True:
                if code[0] == '0':
                    lst.append(code[:5])
                    code = code[5:]
                    bits_used += 5
                    break
                lst.append(code[:5])
                code = code[5:]
                bits_used += 5
            literals.append(int(''.join(lst), 2))

            if bits_used < packet_len:
                code = code[packet_len - bits_used:]
            if bits_used > packet_len:
                print('OOPSIE')
            
            return (code, version_numbers, literals)
        if packet_num:
            count = 0
            # bits_used = 0
            lst = []
            while count < packet_num:
                while True:
                    if code[0] == '0':
                        lst.append(code[:5])
                        code = code[5:]
                        # bits_used += 5
                        count += 1
                        break
                    lst.append(code[:5])
                    code = code[5:]
                    # bits_used += 5
                literals.append(int(''.join(lst), 2))

                # if bits_used < packet_len:
                #     code = code[packet_len - bits_used:]
                # if bits_used > packet_len:
                #     print('OOPSIE')
            return (code, version_numbers, literals)
        if not packet_num and not packet_len:
            lst = []
            bits_used = 0
            while True:
                if code[0] == '0':
                    lst.append(code[:5])
                    code = code[5:]
                    bits_used += 5
                    break
                lst.append(code[:5])
                code = code[5:]
                bits_used += 5
            literals.append(int(''.join(lst), 2))

            # if bits_used < packet_len:
            #     code = code[packet_len - bits_used:]
            # if bits_used > packet_len:
            #     print('OOPSIE')
            code = code[code.index('1'):]
            
            return (code, version_numbers, literals)
    else:
        print("TYPE ELSE")
        if code[0] == '0':
            print("LENGTH TYPE 0")
            bit_len = int(code[1:16], 2)
            code = code[16:]
            # sub_packets = code[:bit_len]=
            code, version_numbers, literals = decode_message(code, version_numbers, literals, packet_len = bit_len)
        if code[0] == '1':
            print("LENGTH TYPE 1")
            num_sub_packets = int(code[1:12], 2)
            code = code[12:]
            for _ in range(num_sub_packets):
                # Process one sub-packet and capture the updated code and results
                code, version_numbers, literals = decode_message(code, version_numbers, literals)
            # return decode_message(code, version_numbers, literals, None, num_sub_packets)
    print('MISSED EVERYTHING')
    print(f"{type_id = }")
    print(f"{packet_len = }")
    print(f"{packet_num = }")
    
with open(file) as f:
    msg = f.readline().strip()

hex_digits = [str(i) for i in range(10)] + [ch for ch in 'ABCDEF']
hex_vals = [0 for i in range(4)]
hex_bits = []
for i in range(16):
    if i > 0:
        hex_vals[-1] += 1
    for idx in range(len(hex_vals) - 1, -1, -1):
        if hex_vals[idx] > 1:
            hex_vals[idx] = 0
            hex_vals[idx-1] += 1
    hex_bits.append(''.join(map(str, hex_vals.copy())))
hex_dict = dict(zip(hex_digits, hex_bits))

new_msg = ''
for ch in msg:
    new_msg += hex_dict[ch]

a = sum(decode_message(new_msg))
print(f"{a = }")