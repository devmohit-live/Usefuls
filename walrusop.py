"""
Python 3.8 Log Changes 

"""

"""
1> Walrus Operator 
"""


a,b=[],[]

"""
Traditional way

"""
def trad():
    while(True):
        inp=input("Enter a name :")
        if inp=='q':
            break
        else:
            a.append(inp)

"""
Walrus Operator :=

assignments and check/comdition at the same time


"""

def wal():
    while (inp:=input("Enter a name : ") ) != 'q':
        b.append(inp)

if __name__ == "__main__":
    print(" Traditional way : ")
    trad()
    print(a)

    print("Walrus Operator")
    wal()
    print(b)