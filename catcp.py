#coding:utf-8
import requests
import json
import os
import subprocess


def wxPusher_send_messaget_post(data_message):
    message = data_message
    app_token = 'AT_eQOSJ7yrMMbemPPMRb49ZeUPaE5okTle'
    UID = 'UID_4VKRjdDY0MffPCNH0krl85rwQAZv'
    UID1 = 'UID_utrVi9teZRN1oLRWDxbQt0U1tkzS'
    data = {
        "appToken": app_token,
        "content": message,
        "summary": message,
        "contentType": 1,
        "uids": [UID, UID1],
        "url": "https://wxpusher.zjiecode.com",
        "verifyPay": False
    }
    json_data = json.dumps(data)

    url = "https://wxpusher.zjiecode.com/api/send/message"
    headers = {
        'Content-Type': "application/json",
    }
    request = requests.post(url, data=json_data, headers=headers)
    return request


def cat_key(cmd):
    res = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)  # 浣跨敤绠￠亾
    result = res.stdout.read()
    res.wait()
    res.stdout.close()
    return result


def send_id(data):
    res = os.system('echo -n  "%s" > /data/params/d/DongleId' % (data[0:12]).replace("+","").replace("/", ""))
    res = os.system('echo -n  "%s" > /data/params_cp/d/DongleId' % (data[0:12]).replace("+","").replace("/", ""))
    return res

def updata(data):
    need_update=input("if need update,please input y \n")
    if str(need_update) =="y":
        version=input("you need input version id\n")
        device=input("you need input deviceitem 2 or 3 \n")
        res = os.system('wget https://delta.onlymysocks.com/download/cp_byd_c%scp_%s_%s_delta.sh' % (device,data[0:12],version))


if __name__ == '__main__':
    result = cat_key("cat /data/openpilot/dump.txt")
    data = str(result, encoding="utf-8").replace("/", "")
    send_id(data)
    true_data = str(result, encoding="utf-8")
    if "==" not in data:
        os.system("echo -n  op_byd_c2_%s_11111  > /data/params/d/LastUpdatePkg" % (data[0:12]).replace("+","").replace("/", ""))
        os.system("echo -n  op_byd_c2_%s_11111  > /data/params_cp/d/LastUpdatePkg" % (data[0:12]).replace("+","").replace("/", ""))
    else:
        os.system("echo -n  op_byd_c3_%s_11111  > /data/params/d/LastUpdatePkg" % (data[0:12]).replace("+", "").replace("/",
                                                                                                                  ""))
        os.system("echo -n  op_byd_c2_%s_11111  > /data/params_cp/d/LastUpdatePkg" % (data[0:12]).replace("+","").replace("/", ""))
    wxPusher_send_messaget_post(true_data)
    updata(data.replace("+","").replace("/", ""))