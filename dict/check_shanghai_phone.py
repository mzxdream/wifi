import requests
import bs4
import time

def isSHPhone(phone):
    while True:
        try:
            res = requests.get("http://www.ip138.com:8080/search.asp?action=mobile&mobile=" + phone)
            res.encoding = 'gbk'
            if (res.status_code != 200):
                print(res.status_code)
                time.sleep(1)
            else:
                break
        except:
            time.sleep(5)
            print("-----------", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    soup = bs4.BeautifulSoup(res.text)
    contents = soup.find_all("td", class_="tdc2")[1].contents
    local = contents[len(contents)-1]
    if (local.find("上海") != -1):
        return True
    return False

def checkSHPhone(file_name):
    phone7_list = []
    for line in open(file_name):
        phone7_list.append(line[:-1])

    if (len(phone7_list) == 0):
        return
    print(len(phone7_list))
    phone7_range_list = []
    start = end = int(phone7_list[0])
    for i in range(1, len(phone7_list)):
        num = int(phone7_list[i])
        if end == num - 1:
            end = num
        else:
            phone7_range_list.append({"start": start, "end": end})
            start = end = num

    for obj in phone7_range_list:
        if (isSHPhone(str(obj["start"]-1))
            or not isSHPhone(str(obj["start"]))
            or not isSHPhone(str(obj["end"]))
            or isSHPhone(str(obj["end"]+1))):
            print("err:", obj["start"], "----------", obj["end"])
        else:
            print(obj["start"], "----------", obj["end"])

checkSHPhone("phone_sh.dict")

