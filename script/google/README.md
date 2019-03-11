## Crash && ANR统计工具

1. 配置Python3环境
2. 安装所需依赖
    - BeautifulSoup
    - selenium
    - lxml
    
    ```bash
    pip3 install beautifulsoup4
    pip3 install selenium
    pip3 install lxml
    ```
3. 安装WebDriver
    - 没有HomeBrew，安装HomeBrew: `ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
    - 安装chromedriver: `brew cask install chromedriver`
4. 执行脚本
    - `python3 fetch_play_console_data.py`
    - 输入ANR/Crash Url
    ![](https://blog-1251678165.cos.ap-chengdu.myqcloud.com/2019-03-11-055128.jpg)
    - 输入需要爬取多少页数据
    - 输入账号/密码