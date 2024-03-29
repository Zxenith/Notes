def lengthOfLongestSubstring(s):
    i, j = 0, 0
    lens = []
    x = len(s)

    if x == 0 or x == 1:
        return x

    while j < x:
        sub = s[i:j]

        if j == x - 1:
            if s[j] not in sub:
                j += 1

            lens.append(len(sub))
            break

        if s[j] not in sub:
            j += 1

        else:
            ind = sub.index(s[j])
            lens.append(len(sub))
            i = i + ind + 1
            j += 1

    lens.append(len(s[i:j]))

    return max(lens)
