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


def calc_similar(key, dataKey):
    commonStr = longest_common_prefix([key, dataKey])
    commonLen = len(commonStr)
    print('commonStr', commonStr, 'Len', commonLen)

    if commonLen == 0:
        return False

    if len(key) <= len(dataKey):
        minLen = len(key)
    else:
        minLen = len(dataKey)

    if minLen <= 10 and minLen == commonLen:
        print('1 key:', key, 'dataKey:', dataKey, 'commonStr:', commonStr)
        print('commonLen:', str(commonLen), 'minLen:', str(minLen), 'rate:', str(commonLen / minLen))
        return True

    if minLen <= 20 and commonLen / minLen >= 0.95:
        print('2 key:', key, 'dataKey:', dataKey, 'commonStr:', commonStr)
        print('commonLen:', str(commonLen), 'minLen:', str(minLen), 'rate:', str(commonLen / minLen))
        return True

    if minLen <= 30 and commonLen / minLen >= 0.9:
        print('3 key:', key, 'dataKey:', dataKey, 'commonStr:', commonStr)
        print('commonLen:', str(commonLen), 'minLen:', str(minLen), 'rate:', str(commonLen / minLen))
        return True

    if minLen <= 40 and commonLen / minLen >= 0.85:
        print('4 key:', key, 'dataKey:', dataKey, 'commonStr:', commonStr)
        print('commonLen:', str(commonLen), 'minLen:', str(minLen), 'rate:', str(commonLen / minLen))
        return True

    if minLen > 40 and commonLen / minLen >= 0.80:
        print('x key:', key, 'dataKey:', dataKey, 'commonStr:', commonStr)
        print('commonLen:', str(commonLen), 'minLen:', str(minLen), 'rate:', str(commonLen / minLen))
        return True

    return False


if __name__ == '__main__':
    key1 = "位置：com.optimizer.strtest.junkmanager.SessionReceiverBroadcast of Intent { act=hs.app.session.SESSION_START flg=0x10 pkg=com.mobile.security.antivirus.applock.wifi cmp=com.mobile.security.antivirus.applock.wifi/com.optimizer.strtest.junkmanager.SessionReceiver launchParam=MultiScreenLaunchParams { mDisplayId=0 mBaseDisplayId=0 mFlags=0 } (has extras) }"
    key2 = "位置：com.optimizer.strtest.junkmanager.SessionReceiverBroadcast of Intent { act=hs.app.session.SESSION_START flg=0x10 pkg=com.mobile.security.antivirus.applock.wifi cmp=com.mobile.security.antivirus.applock.wifi/com.optimizer.strtest.junkmanager.SessionReceiver (has extras) }, VisibleToUser"
    key2 = "位置：com.optimizer.strtest.junkmanager.SessionReceiverBroadcast of Intent { act=hs.app.session.SESSION_START flg=0x10 pkg=com.mobile.security.antivirus.applock.wifi cmp=com.mobile.security.antivirus.applock.wifi/com.optimizer.strtest.junkmanager.SessionReceiver launchParam=MultiScreenLaunchParams { mDisplayId=0 mBaseDisplayId=0 mFlags=0 } (has extras) }"
    # key1 = 'dsdsa'
    # key2 = 'dsdsb'
    print('key1 len', len(key1))
    print('key2 len', len(key2))
    print(calc_similar(key1, key2))

