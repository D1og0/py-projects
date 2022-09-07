text = input('text: ')
    
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lit_alphabet = ['4', '8', 'c', 'd', '3', 'f', '6', 'h', '1', 'j', 'k', '1', 'm', 'n', '0', 'p', 'q', 'r', '5', '7', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
newtext = ''
    
for char in text.lower():
    newtext += lit_alphabet[alphabet.index(char)]
        
print(newtext)