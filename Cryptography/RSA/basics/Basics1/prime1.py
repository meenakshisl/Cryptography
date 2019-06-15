def checkp2(a) :
    for i in range(2,a+1,) :
        if(a%i==0) :
            break
    
    if i<a :
        return "Composite"
    else :
        return "Prime"
if __name__ =="__main__" :
    a=input()
    print checkp2(a)

