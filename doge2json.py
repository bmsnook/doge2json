#!/usr/bin/python3

import os
import glob
import json
import lzstring

x = lzstring.LZString()

#data_from_user = input("Enter your value: ")
#print(data_from_user)

def prompt_and_read_lzstring_multiline():
  lines = []
  print("Enter lzstring-encoded data.")
  while True:
    line = input()
    if line:
      lines.append(line)
    else:
      break
  text = '\n'.join(lines)

def display_user_entered_lzstring_multiline():
  print("\n\n")
  print("You entered the following text: ")
  print(text)


## TEST if files exist
## https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-without-exceptions

## LIST files in directory
## https://stackoverflow.com/questions/13297406/using-file-extension-wildcards-in-os-listdirpath
## https://www.tutorialspoint.com/python/os_listdir.htm

## PRINT variables with strings
## https://matthew-brett.github.io/teaching/string_formatting.html

## READ and JOIN multi-line input
## https://stackoverflow.com/questions/30239092/how-to-get-multiline-input-from-user


print("INFO: getting current directory.")
my_cwd = os.getcwd()

def process_dir_glob():
  print("INFO: current directory is: {}".format(my_cwd))
  print("INFO: examining current directory (glob.glob).")
  listing = glob.glob(my_cwd + '/*')
  for filename in listing:
    if filename.endswith('.doge'):
      print("Found a doge file: {}".format(filename))
      decomp_filename = filename + ".json"
      if (os.path.isfile(decomp_filename)):
        print("INFO: file '%s' already exists." % (decomp_filename))
      else:
        print("INFO: file '%s' does NOT exist yet. Creating it." % (decomp_filename))

print("\n")
print("INFO: current directory is: {}".format(my_cwd))
print("INFO: examining current directory (listdir).")
listing2 = os.listdir(my_cwd)
for each_file in listing2:
  if each_file.endswith('.doge'):
    print("Found: {}".format(each_file))
    each_decomp_file = each_file + ".json"
    if (os.path.isfile(each_decomp_file)):
      print("INFO: file DOES exist: {}".format(each_decomp_file))
    else:
      print("INFO: file does NOT exist. Creating: {}".format(each_decomp_file))
      in_buffer = []
      with open(each_file, 'r') as each_read_in:
        line_in = each_read_in.readline()
        while line_in != '':
          in_buffer.append(line_in)
          line_in = each_read_in.readline()
        response = input("Read first file. Press ENTER to display contents.")
        text = '\n'.join(in_buffer)
        print(text)
        response = input("Output first file. Press ENTER to continue.")
        decompressed = x.decompressFromBase64(text)
        print(decompressed)
        response = input("Output first file decompressed (unformatted). Press ENTER to print formatted JSON.")
        decompressed_parsed = json.loads(decompressed)
        print(json.dumps(decompressed_parsed, indent=4, sort_keys=False))
        with open(each_decomp_file, 'w') as out_file:
#          out_file.write(decompressed)
          out_file.write(json.dumps(decompressed_parsed, indent=4, sort_keys=False))





