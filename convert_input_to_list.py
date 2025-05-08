# this sample was written by Cat Police's ai on Cat Stand discord server
""" full prompts below
write a python script that converts user input into a list of separate items of a certain type specified by user. examples:
"str 1 2 3" -> ["1", "2", "3"]
"int 69 42" -> [69, 42]

i want data type to be specified as the first item in the input, i don't need multiple input prompts
"""
# the code below is what it replied with, copied straight from the message without any modifications

import re
import sys

def convert_to_list(input_str, data_type):
 if data_type == 'str':
 return re.findall(r'\d+|\D+', input_str)
 elif data_type == 'int':
 return [int(num) for num in re.findall(r'\d+', input_str)]
 else:
 print("Invalid data type. Can be 'str' or 'int'.")
 sys.exit(1)

def main():
 if len(sys.argv) != 2:
 print("Usage: python script.py <type>input_string")
 sys.exit(1)

 data_type = sys.argv[1][:4].lower() # Take first 4 chars
 input_str = sys.argv[1][4:] # Rest of the string

 try:
 result = convert_to_list(input_str, data_type)
 print(result)
 except Exception as e:
 print(e)

if __name__ == "__main__":
 main()
