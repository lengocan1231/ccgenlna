#!/usr/bin/env python2
#-*- coding: iso-8859-1 -*-.
import getopt
import time
import os 
import sys
import datetime
from random import randint
 
version = "1.0.0"
os.system ("clear")
import random
import requests
import requests as reqs
print '''\033[1;31m
╔═══╗╔═══╗╔═══╗╔═══╗╔═╗─╔╗
║╔═╗║║╔═╗║║╔═╗║║╔══╝║║╚╗║║
║║─╚╝║║─╚╝║║─╚╝║╚══╗║╔╗╚╝║
║║─╔╗║║─╔╗║║╔═╗║╔══╝║║╚╗║║
║╚═╝║║╚═╝║║╚╩═║║╚══╗║║─║║║
╚═══╝╚═══╝╚═══╝╚═══╝╚╝─╚═╝
                                                               '''
print ("\033[1;34m+----------------------------+\033[0m")
print '''\033[1;37m  \tCCGen and Checker'''
print '''\033[1;32m     Edit by: Le Ngoc An'''
print '''\033[1;32m      FB: @zorobeanst '''
print '''\033[1;32m       Source: @Jorgebarba '''
print ("\033[1;34m+----------------------------+\033[0m") 
def BinChecker():
    FBin = (raw_input("\033[1;33mNhap BIN: : \033[0m"))
    Bin = FBin.replace(' ' , '')
    Bin = Bin.replace('x' ,'')
    Bin = Bin.replace('X', '')
    Bin = Bin[:6]
  
    url = "https://www.lookupbin.com/bin?bin=" + Bin
  
    response = reqs.get(url)
  
    if "is not a known BIN" in (response.text):
      print "\n", Bin, "is not a known BIN"
  
      check = raw_input("\nWARNING....!..The BIN is not proper BIN. CC with these BIN may not works properly \n Do you want to change the BIN (yes/no | Default:yes): ")
      if check in ['n', 'N', 'No', 'no', 'NO']:
        quit()
      else:
        BinChecker()
    else:
      if "BIN" in (response.text):
        BIN = ((response.text).split("BIN:",2)[-1]).split("</div></div>", 1)[0][28:]
        print ("\033[1;34m+----------------------------+\033[0m")
        print "\033[1;33mBIN:\033[0m", BIN
  
      if "Network" in (response.text):
        Network = str((response.text).split("Network:",2)[-1]).split("</div></div>", 1)[0][28:]
        print "\033[1;33mType:\033[0m", Network
  
      if "Brand" in (response.text):
        Brand = str((response.text).split("Brand:",2)[-1]).split("</div></div>", 1)[0][28:]
        print "\033[1;33mMARCA:\033[0m", Brand
  
      if "Type" in (response.text):
        Type = str((response.text).split("Type:",2)[-1]).split("</div></div>", 1)[0][28:]
        print "\033[1;33mLoai:\033[0m", Type
  
      if "Prepaid" in (response.text):
        Prepaid = (response.text).split("Prepaid:",2)[-1].split("</div></div>", 1)[0][28:]
        print "\033[1;33mTra Truoc:\033[0m", Prepaid
  
      if 'Country:' in (response.text):
        Country = str((response.text).split("Country:",2)[-1]).split("</div></div>", 1)[0][28:]
        print "\033[1;33mNuoc:\033[0m", Country
      if "Bank:" in (response.text):
        Bank = ((response.text).split("Bank:",2)[-1]).split("</div></div>", 1)[0][28:]
        print "\033[1;33mNgan Hang:\033[0m", Bank
        print ("\033[1;34m+----------------------------+\033[0m")
      print "\n\033[1;31mWARNING .... Khong chiu trach nhiem ve hoat dong cua ban..!..!\033[0m"
      ccgen(FBin, Network)
  
def ccgen(FBin, Network):
    if (len(FBin) < 16):
      FBin = FBin+((16-(len(FBin)))*'x')
    
    TBin = FBin
    nocc = input("\n\033[1;32mNhap so the can gen : \033[0m")
    m = input("\n\033[1;32mNhap thang : \033[0m")
    y = input("\n\033[1;32mNhap nam : \033[0m")
  
    print "\n\033[1;36mThe duoc tao:\033[0m"
    print ("\033[1;34m+----------------------------+\033[0m")
    print "\033[1;31mCredit Card No |\033[1;33m Month |\033[1;37m Years |\033[1;36m CVV |\033[1;32mCard Status \033[0m"
    for i in range(nocc):
      for i in range(len(TBin)):
        n = str(random.randint(0, 9))
        #if (len(m) == 1):
          #m = '0' + m       
        if (Network == 'amex'):
          cv = str(random.randint(1000, 9999))
        else:
          cv = str(random.randint(100, 999))	
  
        c = TBin[i]
        if (c == 'x' or c == 'X'):
          FBin = FBin[:i] + str(n) + FBin[i+1:]
  
      cc = FBin + '|' + str(m) + '|' +  str(y) + '|' + cv
      ccchecker(cc)
  
def ccchecker(cc):
  
    url = "https://mrchecker.net/card/ccn1/alien07.php"
    
    form = {
      'ajax':'1',
      'cclist':cc,
      'do':'check'
    }
  
    response = reqs.post(url, form, stream = True)
  
    if 'Live' in (response.text):
      print cc, "\033[1;32m| Live\033[0m"
    elif 'Unknown' in (response.text):
      print cc, "\033[1;33m| Unknown\033[0m"
    else :
      print cc, "\033[1;31m| Die\033[0m"
  
BinChecker()
print ("\033[1;34m+----------------------------+\033[0m")
print '\n\033[1;33mNeu khong co the LIVE, vui long thu lai\033[0m'
  #
