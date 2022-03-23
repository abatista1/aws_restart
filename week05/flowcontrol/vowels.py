#Read a sentence from STDIN
#Count the number of vowels in this sentence

sentence = input("Sentence: ")

total = 0

for v in "aieou":
    frequency = sentence.lower().count(v)
    total += frequency
    print("{} ---> {}".format(v,frequency))
    
print("Vowel count = {}".format(total))

