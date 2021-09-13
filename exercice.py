#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    if len(string)%2==0:
        return True


def remove_third_char(string: str) -> str:
    return string.replace(string[2],'')


def replace_char(string: str, old_char: str, new_char: str) -> str:
    return string.replace('w','z')


def get_nb_char(string: str, char: str) -> int:
    nbre=0
    for letter in (string):
     if letter== char:
        nbre +=1
    return nbre


def get_nb_words(string: str) -> int:
    nbre=1
    if string=='':
        nbre = 0
    else:
        for letter in (string):
            if letter==' ':
                nbre +=1
    return nbre
    
    return 0


def main() -> None:
    string = "Bonjour!"
    print(len(string))
    parity = 'pair' if is_even_len(string) else 'impair'
    print(f"Le nombre de caractère dans la chaine '{string}' est {parity}")

    string = "Sam est cool!"
    print(f"On supprime le 3e caratère dans la chaine '{string}'. Résultat: {remove_third_char(string)}")

    string = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: '{string}'. Résultat: {replace_char(string, 'w', 'z')}")
    string= "hello"
    print(f"Le nombre d'occurrence de l dans hello est : {get_nb_char(string, 'l')}")
    
    string = "Baby shark doo doo doo doo doo doo"
    print(f"Le nombre de mots dans la chaine {string} est: {get_nb_words(string)}")


if __name__ == '__main__':
    main()
