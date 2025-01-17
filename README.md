# wechat-reply
用于在微信上快速接龙的脚本
## 准备

- 首先，安装`itchat-uos`版本

```shell
pip install itchat-uos==1.5.0.dev0
```

- 建议修改`itchat\components\login.py`脚本，保证成功登录。具体代码参考[github issue](https://github.com/why2lyj/ItChat-UOS/pull/14/files)

```python
           if status == '200':
                isLoggedIn = True
            elif status == '201':
                if isLoggedIn is not None:
                    logger.info('Please press confirm on your phone.')
                    isLoggedIn = None
                time.sleep(0.5)  # 添加这一行
            elif status != '408':
                break
        if isLoggedIn:
            break
        elif self.isLogging:
            logger.info('Log in time out, reloading QR code.')
```

## 运行

- 修改并通过`find_group_info.py`查找group信息，将会保存到json文件中
- 使用`main.py`完成对应功能
