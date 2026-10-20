# Python 3 code to demonstrate the
# working of MD5 (string - hexadecimal)
import hashlib

k = 0
pw = list("--------")
while True:
    str2hash = str("yzbqklnj" + str(k))
    result = hashlib.md5(str2hash.encode())
    #print(str2hash, str(result.hexdigest()), pw)
    if str(result.hexdigest()).startswith("000000"):
        print(k)
        break
    k += 1
