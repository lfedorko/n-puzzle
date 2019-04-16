import re
from sys import argv


# >>> import re
# >>> string1 = "498results should get"
# >>> int(re.search(r'\d+', string1).group())

def parse_input(file):
    size = 0
    re_number = r"(^\s*\d+\s*)(#.+)*$"
    with open(file) as f:
        content = f.readlines()
    count = 0
    num_list = []
    for line in content:
        if re.match(r"((#)|(\s+#).+)|(^\s*$)", line):
            continue
        elif size == 0:
            size = re.match(re_number, line)
            if size:
                size = int(size.group(1))
                re_rows = "^(\s*(\d+\s+){" + re.escape(str(size - 1)) + "}\d+)(\s*#.+)*$"
            else:
                exit("Invalid size")
            if size < 3:
                exit("Size < 2")
        elif count < size and size > 0:
            res = re.match(re_rows, ' '.join(line.split()))
            if res:
                for s in res.group(1).split(' '):
                    s = int(s)
                    if s < size * size and not s in num_list:
                        num_list.append(s)
                count += 1
            else:
                exit("Invalid string : " + line)
        else:
            exit("A lot of strings!")
            break
    if size != count:
        exit("Not enough strings!")
    return num_list, size


if __name__ == '__main__':
    if len(argv) > 1:
        list, num = parse_input(argv[1])
        print(list)
    # check_input(list, size)
