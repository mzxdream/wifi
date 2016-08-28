import requests
import bs4
import time

def readPhone3(file_name):
    phone3_list = []
    for line in open(file_name):
        phone3_list.append(line[:-1])

    return phone3_list

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

def getSHPhone(phone3_file, phone_file, phone_tmp):
    phone3_list = readPhone3(phone3_file)
    phone7_list = []
    for phone3 in phone3_list:
        for i in range(0, 10000):
            suffix = str(i).zfill(4)
            phone7_list.append(phone3 + suffix)
    fp_tmp = open(phone_tmp, "r+")
    last_num = fp_tmp.readline()
    skip = True
    if not last_num:
        skip = False
    else:
        skip = True
        last_num = last_num[:-1]

    for phone7 in phone7_list:
        if skip:
            if phone7 == last_num:
                skip = False
            continue
        if isSHPhone(phone7):
            fp = open(phone_file, "a+")
            print(phone7)
            fp.write(phone7 + '\n')
            fp.close()
        fp_tmp.seek(0)
        fp_tmp.write(phone7 + '\n')


if __name__ == "__main__":
    getSHPhone("phone3.dict", "phone_sh.dict", "phone_tmp.dict")
