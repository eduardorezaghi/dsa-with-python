import collections

def makeAnagram(a, b):
    a_count = collections.Counter(a)
    b_count = collections.Counter(b)

    res = 0
    for k, v in a_count.items():
        res += abs(v - b_count[k])

    for k, v in b_count.items():
        if k not in a_count:
            res += v

    return res

if __name__ == '__main__':
    a = 'fcrxzwscanmligyxyvym'
    b = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'

    res = makeAnagram(a, b)

    print(res)
