def main():
    myMessage = 'CABE MERAH DI DAPUR'
    myKey = 8

    ciphertext = encryptMessage(myKey,myMessage)
    print(ciphertext + '|')

def encryptMessage(key, message):
    ciphertext = [''] * key

    for column in range(key):
        currentIndex = column

        while currentIndex < len(message):
            ciphertext[column] += message[currentIndex]
            currentIndex += key

    return''.join(ciphertext)

if __name__ == '__main__':
    main()
