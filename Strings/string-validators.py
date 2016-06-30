import re

i_Str = raw_input()

print True if re.search(r'[a-zA-Z0-9]+', i_Str, re.M) else False
print True if re.search(r'[a-zA-Z]', i_Str, re.M) else False
print True if re.search(r'[0-9]', i_Str, re.M) else False
print True if re.search(r'[a-z]', i_Str, re.M) else False
print True if re.search(r'[A-Z]', i_Str, re.M) else False