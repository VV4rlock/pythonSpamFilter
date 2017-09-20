import learn
import neuralnetwork
import os
import re

learn_path = "./new_train"
dictionary = learn.Learn(learn_path)

condition=True if True else False
amount_of_internal_layers=1
input_len=5
output_len=2

important_dict=[]
for i in dictionary.common:
    if dictionary.common[i]>500:
        important_dict.append(i)

print(len(important_dict))
with open("words", "w") as f:
    f.write(" ".join(important_dict))