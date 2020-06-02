alphabet = {"A":"Alpha","B":"Beta","C":"Charlie","D":"Delta","E":"Echo","F":"Foxstrot","G":"Golf","H":"Hotel","I":"India","J":"Juliett","K":"Kilo","L":"Lima","M":"Mike","N":"November","O":"Oscar","P":"Papa","Q":"Quebec","R":"Romeo","S":"Sierra","T":"Tango","U":"Uniform","V":"Victor","W":"Whiskey","X":"X-Ray","Y":"Yankee","Z":"Zulu" } # Complete this dictionary

name = input("Enter your lastname:").upper()

print("\nConverting lastname using NATO Phonetic Alphabet\n")

Nato_alphabet = ''
n = 0
for letter in name:
    if letter in alphabet and name.isalpha()==True:
        Nato_alphabet = Nato_alphabet + "-" + alphabet[letter]
    else:
        n=1
        break
if n == 0:
    print(Nato_alphabet[1:])
else:
    print("Please enter only alphabets")
