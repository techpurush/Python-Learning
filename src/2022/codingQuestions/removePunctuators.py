# define punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = "Hello!!!, he said ---and _ went."

import re
import string
print(string.punctuation)
group=re.findall(r'[a-zA-Z\d\s]',my_str)
print(''.join(group).strip())