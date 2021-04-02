from math import pi, floor, sqrt

#1. zadatak
def area_of_circle(radius):
    return 2 * radius * pi

print("Prvi zadatak")
r = int(input("Unesite polumjer kruga: "))
print("Površina kruga je: {}".format(area_of_circle(r)))

print()

#2. zadatak
def james_Bond(name_and_surname):
    list_of_names = name_and_surname.split(" ")
    surname = list_of_names[len(list_of_names) - 1]
    print("{}. {}".format(surname, name_and_surname))

print("Drugi zadatak")
james_Bond("Kolinda Grabar Kitarović")

print()

#3. zadatak
def remove_extension(filename):
    list_of_words_in_filename = filename.split(".")
    list_of_words_in_filename.pop(len(list_of_words_in_filename) - 1)
    new_filename = ".".join(list_of_words_in_filename)
    print(new_filename)

print("Treći zadatak")
remove_extension('sibirski_plavac.prvi_dio.mp4')

print()

#4. zadatak
def isPalindrome(string):
    string_lowercase = string.lower()
    list_of_words_in_string = string_lowercase.split(" ")
    all_in_one_string = "".join(list_of_words_in_string)
    
    if all_in_one_string == all_in_one_string[::-1]:
       print('Niz {} je palindrom.'.format(string))
    else:
        print('Nizg {} nije palindrom.'.format(string))

print("Četvrti zadatak")
isPalindrome('A mene tu ni minute nema')

print()

#5. zadatak
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            print("Godina {}. je prijestupna".format(year))
        else:
            print("Godina {}. nije prijestupna".format(year))
    else:
        print("Godina {}. nije prijestupna".format(year))

print("Peti zadatak")
print(is_leap_year(2004))

print()

#6. zadatak
def date_of_Catholic_Easter(year):
    a = year % 19
    b = year % 4
    c = year % 7
    k = floor(year/100)
    p = floor((13 + 8*k)/25)
    q = floor(k/4)
    M = (15 - p + k - q) % 30
    N = (4 + k - q) % 7 
    d = (19*a + M) % 30
    e = (2*b + 4*c + 6*d + N) % 7
    
    if 22 + d + e <= 31:
        print("Uskrs je {}. ožujka {}. godine".format((22 + d + e), year))
    else:
        print("Uskrs je {}. travnja {}. godine".format((d + e - 9), year))

print("Šesti zadatak")
date_of_Catholic_Easter(2021)

print()

#7. zadatak
def read_words(src, dest):
    f = open(src, 'r', encoding='utf-8')
    list_of_words = f.readlines()
    f.close()

    list_without_newlines = []

    for word in range(len(list_of_words)):
        list_without_newlines.append(list_of_words[word].strip("\n"))
    
    sentence = " ".join(list_without_newlines)
    
    f = open(dest, 'w', encoding='utf-8')
    f.write(sentence)
    f.close()

print()

#8. zadatak

print()

#9. zadatak
def calc_Fermat_number(n):
    return 2 ** 2 ** n + 1 # Fermatov broj je 2^2^n + 1, a ne -1

print("Deveti zadatak")
print(calc_Fermat_number(2))

print()

#10. zadatak
def isPrime(n):
    if n & 1 == 0:
        return False
    
    max = sqrt(n)
    i = 3
    while i <= max:
        if n % i == 0:
            return False
        i += 2
    return True

print("Deseti zadatak")
print(isPrime(577))

print()

#11. zadatak
def caesar_cypher(word):
    list_of_letters = list(word)
    list_of_original_asciies = []
    list_of_new_asciies = []
    list_of_new_letters = []

    for letter in list_of_letters:
        list_of_original_asciies.append(ord(letter))
    
    for ascii in list_of_original_asciies:
        if ascii == 88 or ascii == 89 or ascii == 90 or ascii == 120 or ascii == 121 or ascii == 122:
            list_of_new_asciies.append(ascii - 23)
        else:
            list_of_new_asciies.append(ascii + 3)

    for ascii in list_of_new_asciies:
        list_of_new_letters.append(chr(ascii))
    
    cyphred_word = "".join(list_of_new_letters)
    print(cyphred_word)

print("Jedanaesti zadatak")
caesar_cypher("INCOGNITO")