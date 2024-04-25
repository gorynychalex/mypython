import re

autonumpattern=r'(\w).*?(\d{3}).*?(\w{2}).*?(\d{2,3})(RUS)*$'
autonum="X123XX125"

print("true") if re.match(autonumpattern,autonum) else print("false")