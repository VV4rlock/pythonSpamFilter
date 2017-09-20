import re
import os.path

class Learn:

    def __init__(self, learn_path):
        self.bad = {}
        self.good = {}
        self.common={}
        self.number_of_good_words = 0
        self.number_of_bad_words = 0
        self.number_of_good_example=0
        self.number_of_bad_example=0
        self.number_of_examles=0

        usual_words = ["the", "The", "she", "She", "him", "his", "have", "has", "her", "Have",
                       "and", "had", "Has", "Had", "for", "And"]

        pattern = r"\b[A-Za-z-\']{3,}\b"

        files = sorted(os.listdir(learn_path))
        with open("SPAMTrain.label") as f:
            temp_test = f.read().splitlines()

        lable = {}                         # discribe class of file with message

        for i in temp_test:
            temp = i.split()
            lable[temp[1]] = temp[0]

        #os.path.join(learn_path)
        for i in files:
            with open(os.path.join(learn_path, i)) as f:
                try:
                    file = f.read()
                    self.number_of_examles+=1
                    f.close()
                except UnicodeDecodeError:
                    os.remove(os.path.join(learn_path, i))
                    continue

            for word in re.findall(pattern, file):
                if word in usual_words:
                    continue
                if word in self.common:
                    self.common[word] += 1
                else:
                    self.common[word] = 1
                if lable[i] == '1':       # good
                    self.number_of_good_example += 1
                    if word not in self.good:
                        self.good[word] = 1
                        self.number_of_good_words += 1
                    else:
                        self.good[word] += 1
                        self.number_of_good_words += 1
                else:                     # bad
                    self.number_of_bad_example += 1
                    if word not in self.bad:
                        self.bad[word] = 1
                        self.number_of_bad_words += 1
                    else:
                        self.bad[word] += 1
                        self.number_of_bad_words += 1
