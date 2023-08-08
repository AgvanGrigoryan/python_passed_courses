import string
alphabet = string.ascii_lowercase
def encrypt(letter,moved_alphabet):
    try:
        index = alphabet.index(letter)
        return moved_alphabet[index]
    except ValueError:
        return letter

def decrypt(letter,moved_alphabet):
    try:
        index = moved_alphabet.index(letter)
        return alphabet[index]
    except ValueError:
        return letter

def move_alphabet(step):
    return alphabet[step:]+alphabet[:step]
             
def encrypt_or_decrypt(msg, key, mode):
    moved_alphabet = move_alphabet(key)
    res = ''
    work_mode_func = work_mode[mode]
    for letter in msg:
        res+= work_mode_func(letter, moved_alphabet)
    return res


def get_mode():
    while True:
        mode = input('Encrypt or Decrypt (e or d): ')
        if mode not in ['e','d']:
            print('Input only e or d for Encrypt or Decrypt!')
        else:
            return mode
            

def get_key():
    while True:
        step = input('Enter the key (0<step<26): ')
        if not step.isdigit() or int(step)<=0 or int(step)>=26:
            print('Enter the number between 0 and 26!')
            continue
        return int(step)

work_mode = {'e': encrypt,'d':decrypt}
while True:
    mode = get_mode()   
    msg = input('Enter the message wich you want to encrypt: ')
    key = get_key()
    print('Result : ' + encrypt_or_decrypt(msg,key,mode))



        
    
