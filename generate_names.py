import random
from nltk.corpus import words

english_words = words.words()
non_names = []
sur_names = []

with open('surnames.txt') as infile:
    read_surname = infile.read().splitlines()

with open('male.txt') as infile:
    read_male = infile.read().splitlines()

with open('female.txt') as infile:
    read_female = infile.read().splitlines()

for line in read_surname:
    sur_names.append(line.split('\t')[0].lower().capitalize())

first_names = list(set(read_male + read_female))
sur_names.remove('Wang')
first_names.remove('Alison')
first_names.remove('Naomi')
sur_names.remove('Nguyen')

full_names = []
for name in first_names:
    full_names.append(name+' '+random.choice(sur_names))

with open('full_names.txt','w') as outfile:
    for name in full_names:
        if len(name.split())==2:
            outfile.write(name+'\n')

for x in range(7500):
	non_names.append(random.choice(english_words).capitalize()+' '+random.choice(english_words).capitalize())

with open('non_names.txt','w') as outfile:
    for name in non_names:
        outfile.write(name+'\n')