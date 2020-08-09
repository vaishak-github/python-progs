def decrypt(n):
    print(n)
    for i in range(0,len(n)):
        if n[i]==str(0):
            x=n.replace(str(0),"a")
        if n[i]==str(1):
            x=n.replace(str(1),"e")
        if n[i]==str(2):
            x=n.replace(str(2),"i")
        if n[i]==str(2):
            x=n.replace(str(2),"o")
        if n[i]==str(3):
            x=n.replace(str(3),"u")
    y=x[::-1]
    print("decrypted val",y)
    if "aca" in y:
        print(y.replace("aca",""))
def encrypt(val):
    n= val[::-1]
    print(n)

    for i in range(0,len(n)):
        if n[i]=="a":
            x=n.replace("a", str(0))
        if n[i]=="e":
            x=n.replace("e", str(1))
        if n[i]=="i":
            x=n.replace("i", str(2))
        if n[i]=="o":
            x=n.replace("o", str(2))
        if n[i]=="u":
            x=n.replace("u", str(3))
    a=x+"aca"
    print("The encrypted value is",a)
    decrypt(a)
def take_values():
    val=str(input())
    encrypt(val)
take_values()
