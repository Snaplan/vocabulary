from vocabulary import Vocabulary
import sys
def main():
    language = sys.argv[1]
    voca = Vocabulary(language)
    while True:
        potato = input('''Please enter \'add\' or \'modify\' or \'delete\'.\n''')
        if potato == 'add':
            addd = input('Please enter the word you want to add')
            adddd = input('Please enter the meaning of the word you want to add')
            voca.add(addd,adddd)
        if potato == 'modify':
            modifies = input('Please enter the word you want to modify')
            modifyyyy = input('Please enter the meaning of the word you want to modify')
            voca.modify(modifies,modifyyyy)
        if potato == 'delete':
            deletee = input('Please enter the word you want to delete')
            voca.delete(deletee)
        if potato == 'stop' or potato == "break":
            break