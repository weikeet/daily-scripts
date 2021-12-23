# 比较任意两个 apk so 文件差异

1. 输出 apk so 文件列表
2. 输出 每个 apk 所缺少的 so 文件

## Usage

```shell
$ python3 compare_two_apk_so.py app1.apk app2.apk
```

## output sample

```shell
$ python3 compare_two_apk_so.py /Users/weicools/Desktop/app-space10-arm64-v8a-debug.apk /Users/weicools/Desktop/app-space10-armeabi-v7a-debug.apk

/Users/weicools/Desktop/app-space10-arm64-v8a-debug.apk so list:
lib/arm64-v8a/libBugly.so
lib/arm64-v8a/libEncryptorP.so
lib/arm64-v8a/libProcessDaemon.so
lib/arm64-v8a/libapminsighta.so
lib/arm64-v8a/libapminsightb.so
lib/arm64-v8a/libavmdl.so
lib/arm64-v8a/libguard.so
lib/arm64-v8a/libimage.so
lib/arm64-v8a/libjcore242.so
lib/arm64-v8a/libjdc.so
lib/arm64-v8a/liblpk.so
lib/arm64-v8a/libmmkv.so
lib/arm64-v8a/libmsaoaidauth.so
lib/arm64-v8a/libnllvm1632808251147706677.so
lib/arm64-v8a/libpangleflipped.so
lib/arm64-v8a/libpl_droidsonroids_gif.so
lib/arm64-v8a/libsgcore.so
lib/arm64-v8a/libttboringssl.so
lib/arm64-v8a/libttcrypto.so
lib/arm64-v8a/libttffmpeg.so
lib/arm64-v8a/libttmplayer.so
lib/arm64-v8a/libttmverify.so
lib/arm64-v8a/libumeng-spy.so
lib/arm64-v8a/libvcn.so
lib/arm64-v8a/libvcnverify.so
lib/arm64-v8a/libvideodec.so

------------------------------------------------------

/Users/weicools/Desktop/app-space10-armeabi-v7a-debug.apk so list:
lib/armeabi-v7a/libBugly.so
lib/armeabi-v7a/libEncryptorP.so
lib/armeabi-v7a/libProcessDaemon.so
lib/armeabi-v7a/libapminsighta.so
lib/armeabi-v7a/libapminsightb.so
lib/armeabi-v7a/libavlengine.so
lib/armeabi-v7a/libavmdl.so
lib/armeabi-v7a/libguard.so
lib/armeabi-v7a/libimage.so
lib/armeabi-v7a/libjcore242.so
lib/armeabi-v7a/libjdc.so
lib/armeabi-v7a/liblibcolor.so
lib/armeabi-v7a/liblpk.so
lib/armeabi-v7a/libmmkv.so
lib/armeabi-v7a/libmsaoaidauth.so
lib/armeabi-v7a/libnllvm1632808251147706677.so
lib/armeabi-v7a/libpangleflipped.so
lib/armeabi-v7a/libpl_droidsonroids_gif.so
lib/armeabi-v7a/libsgcore.so
lib/armeabi-v7a/libt2.so
lib/armeabi-v7a/libttboringssl.so
lib/armeabi-v7a/libttcrypto.so
lib/armeabi-v7a/libttffmpeg.so
lib/armeabi-v7a/libttmplayer.so
lib/armeabi-v7a/libttmverify.so
lib/armeabi-v7a/libumeng-spy.so
lib/armeabi-v7a/libvcn.so
lib/armeabi-v7a/libvcnverify.so
lib/armeabi-v7a/libvideodec.so

------------------------------------------------------

/Users/weicools/Desktop/app-space10-arm64-v8a-debug.apk 缺少的 so 文件：
libavlengine.so
liblibcolor.so
libt2.so

/Users/weicools/Desktop/app-space10-armeabi-v7a-debug.apk 缺少的 so 文件：
```
