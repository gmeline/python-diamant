alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def diamond(lettre):
    nb=0
    previus = 1
    buffer = ''
    while(alphabet[nb]!=lettre):
        nb += 1
    for i in range(nb+1):
        if(i==0):
            buffer+= nb*' '+alphabet[i]+'\n'
        else:
            buffer+=(nb-i)*' '+alphabet[i]+previus*' '+alphabet[i]+'\n'
            previus +=2

    previus-=4
    for i in range(nb-1,-1,-1):
        if(i==0):
            buffer+=nb*' '+alphabet[i]+'\n'
        else:
            buffer+=(nb-i)*' '+alphabet[i]+previus*' '+alphabet[i]+'\n'
            previus -=2
    print(buffer)
    return (buffer)

if __name__ == '__main__':
    diamond('C')
