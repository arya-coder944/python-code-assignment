#count vowels in a string


def countvowels(text):
    vowels = "aeiouAEIOU"
    count=0

    for c in text:
        if c in vowels:
            count +=1
    return count
text = input("Enter your Text:")
print("The count of Vowels:", countvowels(text))
