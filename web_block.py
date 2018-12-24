import time
from datetime import datetime as dt
hosts_temp=r"C:\Users\DOYIN\PycharmProjects\website_blocker\hosts"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","waptrick.com","www.waptrick.com"]
''''in order for the program to actually block websites on your pc, change the file to be opened to hosts_path
instead of hosts_temp'''

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working hours...")
        with open(hosts_temp,'r+') as file:
            content=file.read()
            for item in website_list:
                if item in content:
                    pass
                else:
                    file.write(redirect+" "+item+"\n")
    else:
        print("Fun hours...")
        with open(hosts_temp, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for lines in content:
                if not any(website in lines for website in website_list):
                    file.write(lines)
            file.truncate()
    time.sleep(3)
