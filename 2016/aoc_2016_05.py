# Python 3 code to demonstrate the  
# working of MD5 (string - hexadecimal) 
import hashlib

k = 0
pw = list("--------")
while True:
    str2hash = str(k).join("NinTobias")
    result = hashlib.md5(str2hash.encode()) 
    if str(result.hexdigest()).startswith("00000"):
        try:
            pw[int(result.hexdigest()[5])] = result.hexdigest()[6]
            print("Char found!", "".join(pw), result.hexdigest())
        except Exception:
            pass
    k += 1