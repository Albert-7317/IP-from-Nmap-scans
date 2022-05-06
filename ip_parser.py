###imports###
import os

###variables###


###functions###
#function to split txt into scan down to mac
def list_get(x):
    list_get.layer_1 = []
    with open(x, 'r')as f:
        for block in f:
            if block != "\n":
                list_get.layer_1.append(block)

#function to check if specific ports are open
def ip_list(x):
    ips = []
    for line in x:
        search = line[:-18]
        if search == 'Nmap scan report':
            cut = line.split(" ")
            ips.append(cut[4])
    ip_list.ip = ips

def ip_list_2(x):
    ips = []
    for line in x:
        search = line[:-19]
        if search == 'Nmap scan report':
            cut = line.split(" ")
            ips.append(cut[4])
    ip_list_2.ip = ips
        


###setup###


###main event###
while True:
    list_get('init_scan.txt')
    ilist = list_get.layer_1
    ip_list(ilist)
    ip_list_2(ilist)
    full_ips = ip_list.ip + ip_list_2.ip
    with open('ip_2_scan.txt', 'a') as f:
        for line in full_ips:
            f.write(line)
    break