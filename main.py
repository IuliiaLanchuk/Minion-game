
def counting(a, string):
    counter = 0
    for i in range(len(string)):
        if a in string:
            index = string.find(a)
            s = list(string)
            s[index] = '*'
            string = ''.join(s)
            counter += 1
    return counter


def minion_game(string):
    s = string.upper()
    Stuart = {}
    Stuart_res = 0
    Kevin = {}
    Kevin_res = 0
    alphabet = "AEIOUBCDFGHJKLMNPQRSTVWXYZ"
    vowels = "AEIOU"
    for i in range(len(s)):
        if s[i] in alphabet:
            amount_v = s.count(s[i])
            if s[i] in vowels:
                Kevin[s[i]] = amount_v
            else:
                Stuart[s[i]] = amount_v
            changable = s[i]
            for j in range(i+1, len(s)):
                if s[j] in alphabet:
                    slog = changable+s[j]
                    amount_slog = counting(slog, s)
                    if slog[0] in vowels:
                        Kevin[slog] = amount_slog
                    else:
                        Stuart[slog] = amount_slog
                    changable = slog
                else:
                    continue
        else:
            continue

    print('Kevin =', Kevin)
    for i in Kevin.values():
        Kevin_res += i
    print('Kevin result =', Kevin_res)
    print('Stuart =', Stuart)
    for i in Stuart.values():
        Stuart_res += i
    print('Stuart result =', Stuart_res)
    if Kevin_res > Stuart_res:
        print('Kevin', Kevin_res)
    elif Kevin_res < Stuart_res:
        print('Stuart', Stuart_res)
    else:
        print('Draw')


if __name__ == '__main__':
    s = 'BANANA'
    minion_game(s)


