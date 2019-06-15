
def checkp1(a) :
    ct=0
    for i in range(2,int(a**0.5)+1,) :
        if(a%i==0) :
            ct=1
            break
    if ct==0 :
        return "Prime"
    else :
        return "Composite"


if __name__ =="__main__" :
    a=input()
    print checkp1(a)

