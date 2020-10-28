alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," ",".",",",":",";","1","2","3","4","5","6","7","8","9","0"]
encrypte = ["3","O","¤","k","£","n","Y","€","j","h","#","M","v","å","2","g","*","c","?","r","e","'","s","z","a","q",">","~","´","Å","ø","N","Ä","ñ","ô","|","@","$","{",")","L","?","6","P","<",'"',"ɇ","ƒ","Œ","¥","¦","ª",";","1","(","Æ","$","¼","§",".","¿","À","ē","Ŧ","ƨ","ǟ","ȼ"]


def encryptMsg(msg):
    nwMsg = ""
    for x in msg:
        letter = alphabet.index(x)
        nwMsg = nwMsg + encrypte[letter]
    return nwMsg

def decryptMsg(msg):
    nwMsg = ""
    for x in f:
        i = encrypte.index(x)
        msg = msg + alphabet[i]
    return nwMsg
