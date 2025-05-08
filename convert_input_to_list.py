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
