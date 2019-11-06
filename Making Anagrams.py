def anagram(word1,word2):
    list1 = list(word1)
    list2 = list(word2)
    for f, b in zip(list1, list2):
        for i in list2:
            if i == f:
                list1.remove(f)
                list2.remove(i)
    print(len(list1)+len(list2))


anagram('lol','ahmed')

