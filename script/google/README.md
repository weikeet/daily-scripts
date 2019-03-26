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

### Q & A
1. 登录时概率出现以下错误，重新运行脚本即可
```log
Traceback (most recent call last):
  File "fetch_play_console_data.py", line 220, in <module>
    load_page_data(url, email, password, int(page_count))
  File "fetch_play_console_data.py", line 145, in load_page_data
    password_next.click()
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/selenium/webdriver/remote/webelement.py", line 80, in click
    self._execute(Command.CLICK_ELEMENT)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/selenium/webdriver/remote/webelement.py", line 633, in _execute
    return self._parent.execute(command, params)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/selenium/webdriver/remote/webdriver.py", line 321, in execute
    self.error_handler.check_response(response)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/selenium/webdriver/remote/errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.WebDriverException: Message: unknown error: Element <div role="button" id="passwordNext" class="U26fgb O0WRkf zZhnYe e3Duub C0oVfc nDKKZc DL0QTb" jscontroller="VXdfxd" jsaction="click:cOuCgd; mousedown:UX7yZ; mouseup:lbsD7e; mouseenter:tfO1Yc; mouseleave:JywGue; focus:AHmuwe; blur:O22p3e; contextmenu:mg9Pef;touchstart:p6p2H; touchmove:FwuNnf; touchend:yfqBxc(preventMouseEvents=true|preventDefault=true); touchcancel:JMtRjd;" jsshadow="" jsname="Njthtb" aria-disabled="false" tabindex="0">...</div> is not clickable at point (742, 465). Other element would receive the click: <div class="ANuIbb IdAqtf" jsname="k4HEge" tabindex="0"></div>
  (Session info: chrome=73.0.3683.86)
  (Driver info: chromedriver=73.0.3683.68 (47787ec04b6e38e22703e856e101e840b65afe72),platform=Mac OS X 10.14.2 x86_64)
```