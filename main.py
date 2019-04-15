import re
from sys import argv


def parse_file(file):
    size = 0
    re_number = r"(^\s*\d+\s*)(#.+)*"
   # re_rows = r"(\s*\d+\s*)+{" + str(size) + r"}(#.+)*"
    with open(file) as f:
        content = f.readlines()
    count = 0
    for line in content:
        if re.match(r"(#)|(\s+#).+", line):
            print("comment")
        elif size == 0:
            res = re.match(re_number, line)
            if res:
                print(res[0][0])
                size = int(res[0][0])
        elif count < size:
            exit('Soryan')
        print(line)


if __name__ == '__main__':
    if len(argv) > 1:
        parse_file(argv[1])
