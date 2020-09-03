
## 分类实现
1. 先统计画师对应的插画数量 存到dict中
id_dc Map<String, Integer>: (UserId, 插画数量)

2. 移动插画到对应插画师文件夹（判断文件夹是否存在，不存在需要创建文件夹）

## 画师文件夹重命名
获取所有文件夹

```python
folders = [name for name in os.listdir(pixiv_image_folder)
         if os.path.isdir(os.path.join(pixiv_image_folder, name))]
```

调用API 得到对应画师名字
```text
//API
https://api.imjad.cn/pixiv/v1/?type=member&id={UserId}
//示例
https://api.imjad.cn/pixiv/v1/?type=member&id=3753428
```

文件操作参考
https://python3-cookbook.readthedocs.io/zh_CN/latest/c05/p13_get_directory_listing.html