def count_words(lst):

    counted_words = dict()

    for item in lst:
        if item in counted_words:
            counted_words[item] += 1
        else:
            counted_words[item] = 1

    return counted_words

print(count_words(["hi", "bye", "hi", "bye", "hey", "sup", "hi"]))