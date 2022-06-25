def find_long_substr_len(s):
    ret = ''
    for i in range(0, len(s)):
        curr_s = find_sub(s, i)
        if len(curr_s) > len(ret):
            ret = curr_s
    return len(ret)


def find_sub(s, start):
    ret = ''
    for j in range(start, len(s)):
        if s[j] in ret:
            break
        ret = ret + s[j]
    return ret


if __name__ == '__main__':
    s1 = 'pwwkewabca'
    res = find_long_substr(s1)
    print(s1)
    print(res)
