


def mode_detect(m) :
    if len(m)%16!=0 :
        return 0
    ml=[m[i:i+16] for i in range(0,len(m),16)]
    for i in range(len(ml)) :
        for j in range(len(ml)) :
            if ml[i]==ml[j] and i!=j :
                print i
                return 1
    return 0


if __name__ =="__main__" :
    f=open("ch8.txt","r")
    line=f.readlines()
    for i in line :
        mode_detect((i.strip()).decode('hex'))




    
