from vocabulary import Vocabulary
from string import *
import sys
def l_m():
    language = sys.argv[1]
    voca = Vocabulary(language)
    while True:
        if language.lower() == english:
            potato = input(instruction)
        elif language.lower() == korean:
            potato = input(korean_instruction)
        if potato == add:
            if language.lower() == english:
                addd = input(instruction_addd)
                adddd = input(instruction_adddd)
                voca.add(addd,adddd)
            elif language.lower() == korean:
                addd = input(instruction_korean_addd)
                adddd = input(instruction_korean_adddd)
                voca.add(addd,adddd)
        if potato == modify:
            if language == english:
                modifies = input(instruction_modifies)
                modifyyyy = input(instruction_modifyyyy)
                voca.modify(modifies,modifyyyy)
            elif language == korean:
                modifies = input(instruction_korean_modifies)
                modifyyyy = input(instruction_korean_modifyyyy)
                voca.modify(modifies,modifyyyy)
        if potato == delete:
            if language == english:
                deletee = input(instruction_deletee)
                voca.delete(deletee)
            elif language == korean:
                deletee = input(instruction_korean_deletee)
                voca.delete(deletee)
        if potato.lower() in broke:
            break
        else:
            if language == english:
                print(instruction_wrong_command)
            elif language == korean:
                print(instruction_korean_wrong_command)
