#Prashanth Minkuri
import sys
import os


def is_in_dictionary(lzw_symbol, symbol_dict):
    if len(lzw_symbol) == 1 and ord(
            lzw_symbol) >= 0 and ord(lzw_symbol) <= 255:
        return True

    return lzw_symbol in symbol_dict


def get_code_for_string(lzw_string, symbol_dict):
    if len(lzw_string) == 1:
        return ord(lzw_string)

    return symbol_dict[lzw_string]


def get_symbol_dictionary_length(symbol_dict):
    return len(symbol_dict) + 256

def int_to_bin(integer):
    binary = "{0:{fill}16b}".format(integer, fill='0')
    print(len(binary))
    return binary[:8]+' '+ binary[8:]

n = int(sys.argv[2])
# n= 12
max_table_size = 2 ** n
input_file = sys.argv[1]
# input_file = 'input.txt'
output_file = os.path.splitext(input_file)[0] + '.lzw'
string = ''
symbol_dictionary = {}
current_symbol_value = 255
lzw_data = []


with open(input_file) as f:
    while True:
        symbol = f.read(1)
        if not symbol:
            break
        else:
            if is_in_dictionary(string + symbol, symbol_dictionary):
                string = string + symbol
            else:
                code = get_code_for_string(string, symbol_dictionary)
                lzw_data.append(code)
                print(code)
                if get_symbol_dictionary_length(
                        symbol_dictionary) < max_table_size:
                    symbol_dictionary[string + symbol] = current_symbol_value + 1
                    current_symbol_value = current_symbol_value + 1
                string = symbol

code = get_code_for_string(string, symbol_dictionary)
lzw_data.append(code)
print(code)

with open(output_file, "w") as file:
    output = ' '.join(map(lambda code: int_to_bin(code),lzw_data))
    file.write(output)
