
# Program to find number of words in given string.

para = """ This  is  new  string  with  two  padded  data """

para.lstrip()

para.rstrip()

para_list = para.split("  ")
print("No. of words in string ",len(para_list))
print(para)