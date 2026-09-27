
def find_pos(tuplee,str):
    lst=[]
    for key,val in tuplee:
        if val == str:
           lst.append(key)
    return lst





text = [('I', 'PRON'), ('love', 'VERB'), ('Python', 'PROPN'),
('and', 'CCONJ'), ('use', 'VERB'), ('it', 'PRON'),
('constantly', 'ADV')]
print(find_pos(text, "VERB"))