
import re

text_to_search = """abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890


Ha HaHa

MetaCharacters (Need to be escaped):
.[{()\^$|?*+

coreyms.com

321-555-4321
123.555.1234
322*212*1212
2182128.8219192.98212

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. Tsht"""

# pattern = re.compile(r'^a')   # ^ look for pattern at the start of string when not inside the bracket.

# pattern = re.compile(r'Tsht$')  # $ look for pattern at the exact end of string.

# pattern = re.compile(r'M\w\.')    # \w repreent single alphanumewric char.

# pattern = re.compile(r'\w+\.com')  # finding pattern with .com.

# pattern = re.compile(r'M(r|s|rs)')  # searching for optional pattern 

# pattern = re.compile(r'\d+\.\d+\.\d*')  # searching for mobile number with dot(.) as a seperator.

# pattern = re.compile(r'\d+.\d+.\d+')  

# pattern = re.compile(r'\w+[rcs]')  # any word containing rcs as a char.

# pattern = re.compile(r'\w{3}')   # search for 3 alphabetic characters.

# pattern = re.compile(r'\w{3,5}')  # aearch for range of characters.

# pattern = re.compile(r'\bHa')  # space before the pattern.

# pattern = re.compile(r'\BHa')  # No space before teh character.

pattern = re.compile(r'Mr?')  # ? represent 0 or 1 char .


matches = pattern.finditer(text_to_search)

# finditer method return ietertor object whcih can loop over.

for match in matches:
    print(match)