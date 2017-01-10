#!/usr/vin/env python
# coding: utf-8


import base64
import os
import sys

        
with open('package.tgz') as ecry:
    ecry = ecry.read()
    for i in range(0,5):
        ecry = base64.encodestring(ecry)

with open('package.sec','w') as outsec:
    outsec.write(ecry)

   
   


     
