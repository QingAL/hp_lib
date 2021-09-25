# hp_lib
## 百度OCR申请
https://blog.csdn.net/weixin_36630761/article/details/108253355  
需要记录 AppID、API Key 和 Secret Key 分别代替 baiduOCR.py 中29 - 31行中
## 安装环境
```Shell
pip install numpy
pip install fuzzywuzzy
pip install Pillow
pip install baidu-aip
pip install pyautogui
```
## mousePosition.py
### 运行
```Shell
python mousePosition.py
```
用来检测问题框的屏幕坐标，分别将鼠标放在问题框的左上角和右下角，记录位置坐标。  
有的问题框坐标会变化，可以记录多次，分别代替baiduOCR.py 中 52、53行的代码

## baiduOCR.py
### 运行
```Shell
python baiduOCR.py
```
题目出现时，点击 q 和 w 分别对应不同的答题框架，在控制台输出答案。