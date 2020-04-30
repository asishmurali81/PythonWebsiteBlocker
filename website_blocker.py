from datetime import datetime as dt
import time

hosts_dir = "c:\Windows\System32\drivers\etc\hosts"
hosts_temp = "D:\GitRepository\PythonWebsiteBlocker\hosts"
redirect = "127.0.0.1"
websitelist = ["https://www.facebook.com/", "https://www.hotstar.com/gb"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 16) < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print('working hours')
        with open(hosts_temp,'r+') as file:
            content=file.read()
            for website in websitelist:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        print('Fun Hours')
        with open(hosts_temp,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websitelist):
                    file.write(line)
            file.truncate()
    time.sleep(5)
