

import threading
from threading import*
import time

dic = {}


def create(key, value, timeout=0):
    if key in dic:
        print("key already present in Local storage")
    else:
        if(key.isalpha()):

            if len(dic) < (1024*1024*1024) and value <= (16*1024*1024):
                if timeout == 0:
                    l = [value, timeout]
                else:
                    l = [value, time.time()+timeout]
                if len(key) <= 32:
                    dic[key] = l
            else:
                print("data limit exceeded")
        else:

            print("Invalid key Should contain only alphabets")


def read(key):
    if key not in dic:

        print("key does not present in local Storage. Please enter a valid key")
    else:
        b = dic[key]
        if b[1] != 0:
            if time.time() < b[1]:
                strn = str(key) + ":" + str(b[0])
                print(strn)
                return strn
            else:
                print("timeToLive of", key,
                      "has expired")
        else:
            strn = str(key)+":"+str(b[0])
            return strn


def delete(key):
    if key not in dic:

        print("key does not Present in local storage. Please enter a valid key")
    else:
        b = dic[key]
        if b[1] != 0:
            if time.time() < b[1]:
                del dic[key]
                print("key is successfully deleted")
            else:
                print(" TimeToLive", key,
                      "has expired")
        else:
            del dic[key]
            print("key is successfully deleted")
