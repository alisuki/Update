#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import urllib
import base64


#二进制加解密字符串或文件
#第二个参数en表示加密，de表示解密
def ecrypt_all(strs,ende):
	if ende == 'en':
		for i in range(0,5):
			strs = base64.encodestring(strs)
	if ende == 'de':
		for i in range(0,5):
			strs = base64.decodestring(strs)
	else:
		print('参数语法错误！')
	return(strs)

#下载更新包
urllib.urlretrieve('https://raw.githubusercontent.com/alisuki/Update/fy_erp/v4.0/package.sec','/tmp/.package.sec')

#停止旧进程

#解密压缩包到新文件
with open('.package.sec','rb') as strs:
	strs = strs.read()
	strs = ecrypt_all(strs,'de')
with open('.package.tgz','w') as outfile:
	outfile.write(strs)
	
#解压到相应目录
os.system('tar -xzf outfile -C /etc/fyerp')

#设置权限
os.system('chmod 755 /etc/fyerp/*')

#更新rc.local
shutil.move('/etc/fyerp/rc.local','/etc/rc.local')

#运行新文件
os.system('bash /etc/fyerp/ecryptoo')

#清理缓存与垃圾
os.remove('.package.tgz')
os.remove('.package.sec')
os.remove(sys.argv[0])

