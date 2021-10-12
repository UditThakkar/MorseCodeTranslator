def morse(txt):
    encrypt = {'A':'.-', 'B':'-...', 'C':'-.-.',
               'D':'-..', 'E':'.', 'F':'..-.',
               'G':'--.', 'H':'....', 'I':'..',
               'J':'.---', 'K':'-.-', 'L':'.-..',
               'M':'--', 'N':'-.', 'O':'---',
               'P':'.--.', 'Q':'--.-', 'R':'.-.',
               'S':'...', 'T':'-', 'U':'..-',
               'V':'...-', 'W':'.--', 'X':'-..-',
               'Y':'-.--', 'Z':'--..', ' ':'.....'}
    decrypt = {v: k for k, v in encrypt.items()}
    
    if '-' in txt:
        return ''.join(decrypt[i] for i in txt.split())
    return ' '.join(encrypt[i] for i in txt.upper())

def main():
    msg = input('Morse code: ')
    output = morse(msg)
    print(output)

if __name__ == '__main__':
   main()
  