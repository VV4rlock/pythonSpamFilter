from learn import Learn
from decimal import *
from re import findall
learn_path = "./new_train"
learn = Learn(learn_path)

# print(learn.number_of_bad_words, learn.number_of_good_words)
module = learn.number_of_good_words + learn.number_of_bad_words
probably_of_good_examp=Decimal(learn.number_of_good_example / learn.number_of_examles)
probably_of_bad_examp=Decimal(learn.number_of_bad_example / learn.number_of_examles)
CONST_OF_IMPORTANT=3


def probability_b(word):
    bad, good = 0, 0
    try:
        good = learn.good[word]
        bad = learn.bad[word]
    except:
        pass
    numb = bad+good
    if numb <= CONST_OF_IMPORTANT:
        return Decimal(0.5)
    return Decimal(bad/numb)


def probability_g(word):
    bad, good = 0, 0
    try:
        good = learn.good[word]
        bad = learn.bad[word]
    except:
        pass
    numb = bad + good
    if numb <= CONST_OF_IMPORTANT:
        return Decimal(0.5)
    return Decimal(good / numb)


def compute_all_probability(message):
    list_of_words = findall(r"\b[A-Za-z-\']{3,}\b", message)
    # print(list_of_words)
    prob_in_bad = {}
    prob_in_good = {}
    for word in list_of_words:
        good = probability_g(word)
        bad = probability_b(word)
        if bad != 0.0 and word not in prob_in_bad:
                prob_in_bad[word] = bad
        if good != 0.0 and word not in prob_in_good:
                prob_in_good[word] = good
                # print(good, bad)
    probab_bad = Decimal(1.0)
    probab_good = Decimal(1.0)
    for i in prob_in_bad:
        probab_bad *= prob_in_bad[i]
    for i in prob_in_good:
        probab_good *= prob_in_good[i]
    return probab_good*probably_of_good_examp, probab_bad*probably_of_bad_examp
