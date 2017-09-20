import numpy as np
import os
import re

# sigmoid function
def nonlin(x, deriv=False):
    if (deriv == True):
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))

with open("SPAMTrain.label") as f:  # description of message
    temp_test = f.read().splitlines()

lable = {}  # discribe class of file with message

for i in temp_test:
    temp = i.split()
    lable[temp[1]] = temp[0]

learn_path = "./new_train"
pattern = r"\b[A-Za-z-\']{3,}\b"



X=[]
Y=[]
with open("words") as f:
    important_dict = f.read().split()

files = sorted(os.listdir(learn_path))
for i in files:
    with open(os.path.join(learn_path, i)) as f:
        try:
            file = f.read()
            f.close()
        except UnicodeDecodeError:
            os.remove(os.path.join(learn_path, i))
            continue

    words_in_letter = re.findall(pattern, file)
    input_for_network = []
    for j in important_dict:
        if j in words_in_letter:
            input_for_network.append(1)
        else:
            input_for_network.append(0)


    X.append(input_for_network)
    if lable[i]=='1':
        Y.append(1.0)
    else:
        Y.append(0.0)




# output dataset
y = np.array([Y]).T #выход

# seed random numbers to make calculation
# deterministic (just a good practice)
np.random.seed(1)

# initialize weights randomly with mean 0
syn0 = 2 * np.random.random((len(important_dict), 1)) - 1

eps=1
alpha=1
X=np.array(X)
for iter in range(10000):
    # forward propagation
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))
    # how much did we miss?
    l1_error = y - l1
    # multiply how much we missed by the
    # slope of the sigmoid at the values in l1
    l1_delta = l1_error * nonlin(l1, True)
    # update weights
    syn0 += np.dot(l0.T, l1_delta)
    print(iter)


#print("Output After Training:")
#for i in range(len(important_dict)):
#    print(i,y[i,0],l1[i,0])

test_path = "./test"

t=[]
check=[]
right=0
files = sorted(os.listdir(test_path))
for i in files:
    with open(os.path.join(test_path, i)) as f:
        try:
            file = f.read()
            f.close()
        except UnicodeDecodeError:
            os.remove(os.path.join(test_path, i))
            continue

    words_in_letter = re.findall(pattern, file)
    input_for_network = []
    for j in important_dict:
        if j in words_in_letter:
            input_for_network.append(1)
        else:
            input_for_network.append(0)


    t.append(input_for_network)
    if lable[i]=='1':
        check.append(1.0)
    else:
        check.append(0.0)

l0 = t
l1 = nonlin(np.dot(l0, syn0))
right_pos=0
right_lie=0
all_pos=0
all_lie=0
wrong_in_good=0
wrong_in_bad=0
unknown=0
print("Output :")
for i in range(len(t)):
    if check[i]==1.0:
        all_pos+=1
        if l1[i,0]>0.9:
            right_pos+=1
        elif l1[i,0]<0.1:
            wrong_in_good+=1
        else:
            unknown+=1
    else:
        all_lie+=1
        if l1[i,0]<0.1:
            right_lie+=1
        if l1[i,0]>0.9:
            wrong_in_bad+=1
        else:
            unknown += 1

print("\n\n\n\n\nНЕЙРОННАЯ СЕТЬ\n")
print("точность определения класса \'не спам\': _________________________", right_pos/all_pos)
print("ошибочное отнесение сообщений класса \'не спам\' к классу \'спам\': ", wrong_in_good/all_pos)
print("точность определения класса    \'спам\': _________________________", right_lie/all_lie)
print("ошибочное отнесение сообщений класса \'спам\' к классу \'не спам\': ", wrong_in_bad/all_pos)
print("процент сообщений, не отнесенных ни к какой из кадегорий: ______", unknown/(all_pos+all_lie))
