# -*- coding: utf-8 -*-
import os ,time
print("歡迎使用一鍵安裝vps")
start = time.time()
yyy=0
zzz=26
print("完成率---"+str(yyy)+"/"+str(zzz))
os.system("sudo apt update")
yyy+=1
print("完成率---"+str(yyy)+"/"+str(zzz))
os.system("sudo apt -y upgrade")
yyy+=1
print("完成率---"+str(yyy)+"/"+str(zzz))
os.system("sudo apt install -y python3-pip")
yyy+=1
print("完成率---"+str(yyy)+"/"+str(zzz))
os.system("pip3 install six")
yyy+=1
print("完成率---"+str(yyy)+"/"+str(zzz))
os.system("pip3 install rsa")
yyy+=1
print("完成率---"+str(yyy)+"/"+str(zzz))
os.system("pip3 install thrift")
yyy+=1
print("完成率---"+str(yyy)+"/"+str(zzz))
os.system("pip3 install requests")
yyy+=1
print("完成率---"+str(yyy)+"/"+str(zzz))
os.system("pip3 install gtts")
yyy+=1
print("完成率---"+str(yyy)+"/"+str(zzz))
os.system("pip3 install bs4")
yyy+=1
print("完成率---"+str(yyy)+"/"+str(zzz))
os.system("pip3 install html5lib")
yyy+=1
print("完成率---"+str(yyy)+"/"+str(zzz))
os.system("pip3 install wikipedia")
yyy+=1
print("完成率---"+str(yyy)+"/"+str(zzz))
os.system("pip3 install pytz")
yyy+=1
print("完成率---"+str(yyy)+"/"+str(zzz))
os.system("pip3 install goslate")
yyy+=1
print("完成率---"+str(yyy)+"/"+str(zzz))
os.system("pip3 install googletrans")
yyy+=1
print("完成率---"+str(yyy)+"/"+str(zzz))
os.system("pip3 install akad")
yyy+=1
print("完成率---"+str(yyy)+"/"+str(zzz))
os.system("pip3 install pafy")
yyy+=1
print("完成率---"+str(yyy)+"/"+str(zzz))
os.system("pip3 install humanize")
yyy+=1
print("完成率---"+str(yyy)+"/"+str(zzz))
os.system("pip3 install humanfriendly")
yyy+=1
print("完成率---"+str(yyy)+"/"+str(zzz))
os.system("pip3 install psutil")
yyy+=1
print("完成率---"+str(yyy)+"/"+str(zzz))
os.system("pip3 install youtube_dl")
yyy+=1
print("完成率---"+str(yyy)+"/"+str(zzz))
os.system("pip3 install livejson")
yyy+=1
print("完成率---"+str(yyy)+"/"+str(zzz))
os.system("pip3 install hyper")
yyy+=1
print("完成率---"+str(yyy)+"/"+str(zzz))
os.system("pip3 install threadpool")
yyy+=1
print("完成率---"+str(yyy)+"/"+str(zzz))
os.system("pip3 install httpx")
yyy+=1
print("完成率---"+str(yyy)+"/"+str(zzz))
os.system("pip3 install speedtest_cli")
yyy+=1
print("完成率---"+str(yyy)+"/"+str(zzz))
os.system("pip3 install lesting.api.client")
yyy+=1
print("完成率---"+str(yyy)+"/"+str(zzz))
os.system("pip3 install paramiko")
yyy+=1
print("完成率---"+str(yyy)+"/"+str(zzz))
print("vps環境安裝完畢")
elapsed_time = time.time() - start
print("安裝時間共計: %s秒" % (elapsed_time))
exit()
