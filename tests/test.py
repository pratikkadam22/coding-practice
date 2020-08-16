import re
def match(s):
    pattern = '[1-9a-z]'
    result = re.match(pattern, s)
    if result:
        return True
    else:
        return False
s = '123955785adadgihldgjkh'

print(match(s))