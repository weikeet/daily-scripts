## fabric2csv 使用说明

####安装依赖
本脚本依赖`beatiful soup`库，所以需要先运行`pip install beautifulsoup4`


####操作步骤

1. 在fabric网页上选择对应的 Launcher 和版本
2. 一直往下拉页面，知道页面加载出足够多的 crash 条目
3. 打开 Google Chrome 的开发者工具。More Tools -> Developer Console 或 Option+Command+I
4. 点击 Developer Console 的左上角的箭头，然后点击某条 Crash 中的任何页面元素，则 Developer Console 中应定位到某一个<tr>标签
5. 选中外层的<table>标签，点击F2，全选<table>标签的内容，copy 到 crashlytics_page.html内
6. 运行命令`python fabric2csv.py`
7. copy `csvfile.csv`的内容到Google Sheet内