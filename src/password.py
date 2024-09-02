import re
import sys

if len(sys.argv) != 2:
    print(f"{sys.argv[0]} expected exactly one argument.")
    sys.exit(1)

password = sys.argv[1]
is_valid = False

# Do all the requirement checks here.
length_pw = len(password)
if (
    17 > length_pw > 6
    and re.search("[a-z]", password)
    and re.search("[A-Z]", password)
    and re.search("[$#@]", password)
):
    is_valid = True


print(is_valid)
