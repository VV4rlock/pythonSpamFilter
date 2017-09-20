import compute
import os
import re

with open("SPAMTrain.label") as f:  # description of message
    temp_test = f.read().splitlines()

lable = {}  # discribe class of file with message

for i in temp_test:
    temp = i.split()
    lable[temp[1]] = temp[0]

test_path = "./test"


right_pos=0
right_lie=0
all_pos=0
all_lie=0
unknown=0
wrong_in_good=0
wrong_in_bad=0
files = sorted(os.listdir(test_path))
for i in files:
    with open(os.path.join(test_path, i)) as f:
        try:
            file = f.read()
            f.close()
        except UnicodeDecodeError:
            os.remove(os.path.join(test_path, i))
            continue
    #print(re.findall(r"\b[A-Za-z-\']{3,}\b", file))
    good, bad = compute.compute_all_probability(file)
    #if (good/bad>1 and lable[i]=='1') or (bad/good>1 and lable[i]=='0'):
        #right+=1
    if lable[i]=='1':
        all_pos+=1
        if good / bad > 1:
            right_pos += 1
        elif bad / good > 1:
            wrong_in_good+=1
        else:
            unknown+=1
    else:
        all_lie+=1
        if bad / good > 1:
            right_lie += 1
        elif good / bad > 1:
            wrong_in_bad+=1
        else:
            unknown+=1


print("\n\n\n\n\nНАИВНЫЙ БАЙЕСОВСКИЙ КЛАССИФИКАТОР\n")
print("точность определения класса \'не спам\': _________________________", right_pos/all_pos)
print("ошибочное отнесение сообщений класса \'не спам\' к классу \'спам\': ", wrong_in_good/all_pos)
print("точность определения класса    \'спам\': _________________________", right_lie/all_lie)
print("ошибочное отнесение сообщений класса \'спам\' к классу \'не спам\': ", wrong_in_bad/all_pos)
print("процент сообщений, не отнесенных ни к какой из кадегорий: ______", unknown/(all_pos+all_lie))