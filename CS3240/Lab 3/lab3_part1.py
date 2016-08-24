__author__ = 'Reid'

from Crypto.Hash import SHA256

def main():
    d = {}
    pInput = " "
    num = 1
    while (pInput != ""):
        uString = "User " + str(num) + ": "
        u = input(uString)
        p = SHA256.new()
        pString = "Password: "
        pInput = input(pString)
        p.update(str.encode(pInput))
        print(p.hexdigest())
        if (pInput != ""):
            d.update({u:p.hexdigest()})
        num += 1
    while (True):
        u = input("User: ")
        if u in d:
            p = SHA256.new()
            pInput = input("Password: ")
            p.update(str.encode(pInput))
            pCheck = d[u]
            if (pCheck == p.hexdigest()):
                print("login succeeds")
            elif (pCheck != p.hexdigest()):
                print("login fails")
        else:
            print("user not found")
    print("Done")
    return 0

if __name__ == "__main__":
    main()
