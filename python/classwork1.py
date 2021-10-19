vowels=['a','e','i','o','u','A','E','I','O','U']
arg1=input('Select an alphabet: ')
if (arg1 in vowels): print(f'{arg1} is a vowel')
else: print(f'{arg1} is not a vowel. Probably a consonant.')