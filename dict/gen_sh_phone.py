def genSHPhone(phone7_file, phone_all_file):
    fp = open(phone_all_file, "w")
    for line in open(phone7_file):
        prefix = line[:-1]
        for i in range(0, 10000):
            suffix = str(i).zfill(4)
            fp.write(prefix + suffix + "\n")
    fp.close()

genSHPhone("phone_sh.dict", "phone_sh_all.dict")


