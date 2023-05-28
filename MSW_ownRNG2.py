
# chek-in
def check(analytic_seed, analytic_seed_remover):
    duplicit = []
    for _ in range(len(analytic_seed)):
        # print("Číslo pozice:", _)

        y = analytic_seed[_]
        print("y je:", y)

        analytic_seed_remover.remove(y)
        print("Zbylé znaky ke kontrole:", analytic_seed_remover)

        if y not in analytic_seed_remover:
            print("Ales gute!")

        else:
            print("Schoda na znaku!:",y)
            duplicit.append(y)
            next

    print("DUPLICITY:", duplicit)
    print("POČET DUPL. ZNAKŮ:", len(duplicit))
    return duplicit


# --------------------------------------------------------------------------------------
# READ CSV SOUBORU
import pandas as pd
import re

slovnik = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
    't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26,
    'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36,
    'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45,
    'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52,
    '0': 53, '1': 54, '2': 55, '3': 56, '4': 57, '5': 58, '6': 59, '7': 60, '8': 61, '9': 62,
    '!': 63, '@': 64, '#': 65, '$': 66, '%': 67, '^': 68, '&': 69, '*': 70, '(': 71, ')': 72,
    '-': 73, '_': 74, '=': 75, '+': 76, '[': 77, ']': 78, '{': 79, '}': 80, '|': 81, '\\': 82,
    ';': 83, ':': 84, '\'': 85, '"': 86, ',': 87, '.': 88, '/': 89, '<': 90, '>': 91, '?': 92,
    '`': 93, '~': 94
}


# export historie do csv, přes rozšíření chromu, scraping nevyšel
data_set = pd.read_csv("history.csv")

analytic_seed = []

# PŘEVOD COLUMN -> DATALISTU -> TOLIST()
order = data_set['order'].tolist()
id = data_set['id'].tolist()
date = data_set['date'].tolist()

time = data_set['time'].tolist()
title = str(data_set['title'].tolist())
url = str(data_set['url'].tolist())
VisitCount = data_set['visitCount'].tolist()
TypedCount = data_set['typedCount'].tolist()

# převod characters titlu z historie
title_num = []

counter = 0
for i in range(len(title)):
    counter += 1
    for ch in title[i]:
        if ch in slovnik and ch in title_num:
            dupl_char = slovnik[ch] + counter
            title_num.append(dupl_char)
        elif ch in slovnik:
            title_num.append(slovnik[ch])
        else:
            next


print("TITLE NUM:", title_num)


#TO SAME PRO URL
url_num = []

for i in range(len(url)):
    counter += 3
    for ch in url[i]:
        if ch in slovnik:
            dupl_char_url = slovnik[ch]
            url_num.append(dupl_char_url)
        elif ch in slovnik and ch in url_num:
            dupl_char_url = slovnik[ch] + counter
            url_num.append(dupl_char_url)
        else:
            next

print("URL NUM:", url_num)

# ------------------------------------------------------------------------------------------------------------
#SEED GENERATOR
analytic_seed = []
pocet_cisel = 1000
digits_to_keep = 5

k = 0
for x in range(pocet_cisel):
    k += 1

    rn = title_num[x] + url_num[x]
    shorted_number = round((rn//10**(len(str(rn)) - digits_to_keep)))

    if re.search('.*99', str(shorted_number)) or re.search('.*999', str(shorted_number)):
        shorted_number += k
        analytic_seed.append(shorted_number)

    else:
        analytic_seed.append(shorted_number)

analytic_seed_remover = analytic_seed.copy()

check(analytic_seed, analytic_seed_remover)

