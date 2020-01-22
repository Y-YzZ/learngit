import json

# https://a03a.qianfan123.com/dpos-web/s/a03a24103/sale/v2/list?filter=%5B%7B%22property%22%3A%22created%20bco%22%2C%22value%22%3A%5B%222019-12-01%22%2C%222019-12-31%22%5D%7D%5D&sort=%5B%5D&start=14000&limit=1000
with open("a5.txt", "r", encoding="utf-8") as f1:
    a1 = f1.read()
a2 = json.loads(a1)
ll = a2["data"]


with open("a.csv", "a", encoding="utf-8") as f:
    for i in ll:
        f.write(i["number"])
        f.write(",")
        f.write(str(i["paymentInfo"]))
        f.write(",")
        f.write(str(i["amount"]))
        f.write(",")
        f.write(i["cashier"]["name"])
        f.write(",")
        f.write(i["lastModified"])
        f.write('\n')
