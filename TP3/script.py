import re

def main(file_name):
    
    with open(file_name,'r') as file:
        text = file.read()


    pat = r'(?i)\b(?:on|off)\b|\d+|='
    soma = 0
    estado = False

    for m in re.finditer(pat,text):
        if m.group().lower() == "off":
            estado = False
            print("Somador OFF")
        
        elif m.group().lower() == "on":
            estado = True
            print("Somador ON")
            
        elif m.group() == "=" :
            print(f"Soma = {soma}")
            
            
        elif estado and m.group != "=":
            print(m.group())
            soma += int(m.group())
        
if __name__ == '__main__':
    main('exemplo.txt')
    