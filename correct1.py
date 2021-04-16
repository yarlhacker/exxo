
my_json_datas = []

with open('/Users/ecolenan/Desktop/mes test/username-password-recovery-code.csv') as f:
    header = f.readlines()[0].split()
    content = f.readlines()[:1]
    for i in j:
        i = i.split(',')
        my_dict = {
            header[0]: i[0],
        }
        my_json_datas.append(my_dict)
    print(header)