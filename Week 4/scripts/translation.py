def word_by_word(str, lexicon):
    str=str.split()
    str2=[]
    for word in str:
        if word in lexicon:
           str2.append(lexicon[word])
        else:
           str2.append(word) 
    return " ".join(str2)



print(word_by_word("Python is a language" , {"a": "一个", "is": "是", "language": "语言"}))