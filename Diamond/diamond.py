const alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def diamond(lettre):
  var i=0
  while(alphabet[i]!=lettre):
    print(alphabet[i]+'\n')
    i++
  while(i>=0):
    print(alphabet[i]+'\n')
    i--
