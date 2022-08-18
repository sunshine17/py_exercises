
def uniq_ch(str):
    '''
    Input: s = "loveleetcode"
    Output: 2

    Use a dictionary to keep tracking characters' index.
        - key: ch
        - value: 
            - '>=0': index in str, means it's a non-repeating charactor
            - '-1': it's a repeating charactor
    
    '''
    dic = {}
    for i in range(len(str)):
        ch = str[i]
        index = dic.get(ch) 
        if index is None:   # it's a non-repeating character
            dic[ch] = i
        elif index >= 0:   # it's a repeating character
            dic[ch] = -1    # mark it 
    max_id = len(str)
    min_index = max_id
    for ch, index in dic.items():
        if index == -1:
            continue
        if index < min_index:
            min_index = index

    return -1 if min_index == max_id else min_index


if __name__ == '__main__':
    s = "loveleetcode"
    assert uniq_ch(s) == 2
    print(uniq_ch(s))
