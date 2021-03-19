"""
This script lets you create, in bulk mode, various username and password, for SSL VPN or other stuff.
"""
import random, sys, pyfiglet

#Function that creates the random password 
def passwordGenerator(pwdList):
    alphabet = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabetPlusSymbols = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ-_!.$"

    print('Di quante password hai bisogno?')
    requestedPwd = int(input())
    print('Scegli lunghezza della password: ')
    lenght = int(input())
    print('Caratteri speciali? [s/n]')
    symbolChoice = input()

    for i in range(requestedPwd):
        if symbolChoice == 's' or symbolChoice == 'S':
            passwordGenerated = ''.join(random.sample(alphabetPlusSymbols, lenght))
            pwdList.append(passwordGenerated)
        elif symbolChoice == 'n' or symbolChoice == 'N':
            passwordGenerated = ''.join(random.sample(alphabet, lenght))
            pwdList.append(passwordGenerated)
            #print(passwordGenerated)

    return(pwdList)

#Function that creates the username list, starting from 1, not zero!
def nameGenerator(usrList):

    print("Seleziona il suffisso: ")
    suffix = input()
    print("Quanti username?")
    entries = int(input())
    for i in range(1, entries+1):
        userNames = suffix + str(i)
        usrList.append(userNames)
    
    return(usrList)
    

#FUNZIONE PRINCIPALE
def main():
#while True:

    banner = pyfiglet.figlet_format('BULK MODE FTW')
    print(banner)
    print('\n')

    generatedPasswordList = []
    generatedUserList = []

    #calling the password generator function
    passwordGenerator(generatedPasswordList)
    #calling the username generator function
    nameGenerator(generatedUserList)

    
    for iter in range(len(generatedPasswordList)):
        print(f"USERNAME: {generatedUserList[iter]}\nPASSWORD: {generatedPasswordList[iter]}\n# # #")
    
    
if __name__ == "__main__":
    main()