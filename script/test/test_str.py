# -*- coding: utf-8 -*-


def longest_common_prefix(strs):
    if not strs: return ''
    ss = list(map(set, zip(*strs)))
    res = ''
    for i, x in enumerate(ss):
        x = list(x)
        if len(x) > 1:
            break
        res = res + x[0]
    return res


def calc_similar(s1, s2):
    commonStr = longest_common_prefix([s1, s2])
    commonLen = len(commonStr)
    if len(s1) <= len(s2):
        minLen = len(s1)
    else:
        minLen = len(s2)

    print('commonStr:', commonStr)
    print('commonLen:', str(commonLen), 'minLen:', str(minLen))
    print(str(commonLen / minLen))

    if minLen <= 10 and minLen != commonLen:
        return False

    if minLen <= 20 and commonLen / minLen >= 0.95:
        return True

    if minLen <= 30 and commonLen / minLen >= 0.9:
        return True

    if minLen <= 30 and commonLen / minLen >= 0.85:
        return True
    return False


if __name__ == '__main__':
    print(calc_similar("dacvvdxddsfxcsvsv", "dacvvdxddsfxcvvdscsdd"))
