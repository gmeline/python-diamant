alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def diamond(lettre):
    nb=0
    previus = 1
    while(alphabet[nb]!=lettre):
        nb += 1
    for i in range(nb+1):
        if(i==0):
            print(nb*' '+alphabet[i])
        else:
            print((nb-i)*' '+alphabet[i]+previus*' '+alphabet[i])
            previus +=2
    
    previus-=4
    for i in range(nb-1,-1,-1):
        if(i==0):
            print(nb*' '+alphabet[i])
        else:
            print((nb-i)*' '+alphabet[i]+previus*' '+alphabet[i])
            previus -=2

if __name__ == '__main__':
    diamond('C')
