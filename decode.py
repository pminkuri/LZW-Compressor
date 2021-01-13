#Prashanth Minkuri
import sys
import os


def is_in_dictionary(code, symbol_dict): # checks if the code is  in dictionary
    if code >= 0 and code <=255:
        return True

    return code in symbol_dict

def get_symbol_dictionary_length(symbol_dict):
    return len(symbol_dict) + 256

def get_string(code, symbol_dict):
    if code >= 0 and code <=255:
        return chr(code)
    return symbol_dict[code]

n = int(sys.argv[2])
# n= 12
max_table_size = 2 ** n
input_file = sys.argv[1]
# input_file = 'input.lzw'
output_file = os.path.splitext(input_file)[0] + '_decoded.txt'
string = ''
symbol_dictionary = {}
current_symbol_value = 255
decoded_str = ''
new_string = ''
encoded_data = []

with open(input_file) as f:
    data = f.read()
    bin = data.split(' ')
    for i in range(0, len(bin),2):
        encoded_data.append(int(bin[i]+''+bin[i+1],2))

    code = encoded_data[0]
    string = get_string(code, symbol_dictionary)
    i = 1
    print(string)
    decoded_str = decoded_str + string
    while i < len(encoded_data):
        code = encoded_data[i]
        i = i + 1
        if not is_in_dictionary(code, symbol_dictionary):
            new_string = string + string[0]
        else:
            new_string = get_string(code, symbol_dictionary)
        decoded_str = decoded_str + new_string
        print(new_string)
        if get_symbol_dictionary_length(symbol_dictionary) < max_table_size:
            symbol_dictionary[current_symbol_value + 1] = string + new_string[0]
            current_symbol_value = current_symbol_value + 1
        string = new_string

with open(output_file, "w") as file:
    file.write(decoded_str)
