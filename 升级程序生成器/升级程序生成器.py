#!/usr/vin/env python
# coding: utf-8


import base64
import os
import sys

	  
'''        
s =  'active:20170512|download:https://github.com/alisuki/Update/raw/fy_erp/v4.0/inst.pyc'
for i in range(0,5):
    s=base64.encodestring(s)
    print s
'''
   
   
#二进制加密任何字符串或文件
def ecrypt_all(strs,en_de):		#第二个参数en表示加密，de表示解密
	if en_de == 'en':
		for i in range(0,5):
			strs = base64.encodestring(strs)
	else:
		for i in range(0,5):
			strs = base64.decodestring(strs)
		
    return(strs)






     
