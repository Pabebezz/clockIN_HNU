# 环境配置
`pip install  -r requirements.txt`

selenium 在 Firefox 的 Driver,路径写在default.yml中

下载并安装 tesseract-ocr:（window）并将.exe添加至path
(ubuntu)
`sudo apt-get install tesseract-ocr`

建立default.yml，里面内容包括
```
# 自动打卡配置信息
seleniumFirefoxDriver_path: 
# 帐号密码
username: 
web_password:
# 家庭住址
home: 
# 手动测量验证码的坐标 
rangle: (340, 301, 438, 328)

# 邮件信息配置
# 发信方的信息：发信邮箱，QQ邮箱授权码
from_addr: 
email_password: 
# 收信方邮箱
to_addr: 
# 发信服务器
smtp_server:
```
 # 运行
`python main.py`

PS:若要实现每天自动打卡，确认主板是否支持定时开机，然后设置一个定时计划就ok