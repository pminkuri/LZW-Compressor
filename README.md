## LZW-Compressor

  
- Name :- Prashanth Minkuri
- ID :- 801166901
- Programming language :- Python 3.7

Modules in Project

encode.py for compression and decode.py for decompression




### Encoding :

encode.py file is used to encode the input data using dictionary data structure
where the key and values are characters and ASCII values.
The input file is compressed and stored as input.lzw file with each input data
is of 2 bytes(16 bits)

pseudo code for encoding:

  MAX_TABLE_SIZE=2(bit_length) //bit_length is number of encoding bits
  initialize TABLE[0 to 255] = code for individual characters
  STRING = null
  while there are still input symbols:
  SYMBOL = get input symbol
  if STRING + SYMBOL is in TABLE:
  STRING = STRING + SYMBOL
  else:
  output the code for STRING
  If TABLE.size < MAX_TABLE_SIZE: // if table is not full
  add STRING + SYMBOL to TABLE // STRING + SYMBOL now has a code
  STRING = SYMBOL
  output the code for STRING


### Decoding :
 
Decode.py file is used for decoding  and the result is stored in input_decoded.txt




pseudo code for decoding:

  MAX_TABLE_SIZE=2(bit_length)
  initialize TABLE[0 to 255] = code for individual characters
  CODE = read next code from encoder
  STRING = TABLE[CODE]
  output STRING
  while there are still codes to receive:
  CODE = read next code from encoder
  if TABLE[CODE] is not defined: // needed because sometimes the
  NEW_STRING = STRING + STRING[0] // decoder may not yet have code!
  else:
  NEW_STRING = TABLE[CODE]
  output NEW_STRING
  if TABLE.size < MAX_TABLE_SIZE:
  add STRING + NEW_STRING[0] to TABLE
  STRING = NEW_STRING


### Instructions to run the program:

Open the program directory  using command prompt execute the program with below format

  "python encode.py <input.txt> <bit-length> "
  The output is stored in input.lzw in 16 bit format.

  Similarly for decoding execute as below
  "python decoded.py  <input.lzw> <bit-length>

  The decoded file is stored as input_decoded.txt file.


