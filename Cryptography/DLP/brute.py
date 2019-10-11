def brute(g,p,y) :
    i=2
    sol = pow(g,i,p)
    if sol == y :
        return 2;
    if(y==g) :
        return 1
    if(y==1) :
        return p-1
    for i in range(3,p-1) :
        sol = pow(g,i,p)
        if sol == y :
            return i


if __name__ == "__main__" :
    g,p,y = map(int,raw_input().split(' '))
    print(brute(g,p,y))
