import sys, random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    myMessage = 'CABE MERAH DI DAPUR'
    myKey = 'BADCFEHGJILKNMPORQTSVUXWZY'
    myMode = 'enkripsi'

    if not keyIsValid(myKey):
        sys.exit('Terdapat error pada kunci atau simbol')
    if myMode == 'enkripsi':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'dekripsi':
        translated = decryptMessage(myKey, myMessage)
        
    print('Menggunakan Kunci: %s'% (myKey))
    print('Pesan Ter%s:'% (myMode))
    print(translated)

    #transposisi
    myMessage2 = str(translated)
    myKey2 = 8
    ciphertext = encryptMessage2(myKey2, myMessage2)
    print('Pesan Terenskripsi Tahap 2:')
    print(ciphertext + '|')
    
def keyIsValid(key):
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()
    return keyList == lettersList

def encryptMessage(key, message):
    return translateMessage(key, message, 'enkripsi')

def decryptMessage(key, message):
    return translateMessage(key, message, 'dekripsi')

def translateMessage(key, message, mode):
    translated = ''
    charsA = LETTERS
    charsB = key
    if mode == 'dekripsi':
        charsA,charsB = charsB, charsA

    for symbol in message:
        if symbol.upper() in charsA:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            translated += symbol

    return translated

def getRandomKey():
    key = list(LETTERS)
    random.shuffle(key)
    return''.join(key)

def encryptMessage2(key, message):
    ciphertext = [''] * key
    for column in range(key):
        currentIndex = column
        while currentIndex < len(message):
            ciphertext[column] += message[currentIndex]
            currentIndex +=  key
    return ''.join(ciphertext)

if __name__ == '__main__':
    main()

    
        
