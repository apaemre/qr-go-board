import string
import segno

qrcode = segno.make(input(), micro=False)
qrcode.save('demo.txt')
qrcode.save('demo.png')

alphaDict = dict(zip(range(0,52), string.ascii_letters))
black = ""
white = ""

f = open("demo.txt", "r")
textTowrite = f.read().split()
n = len(textTowrite)

for i in range(n):
    for j in range(n):
        if textTowrite[i][j] == "0":
            white += "[" + (alphaDict[i] + alphaDict[j]) + "]" 
        else:
            black += "[" + (alphaDict[i] + alphaDict[j]) + "]" 

with open('demo.sgf', 'w') as f:
    f.write(f"(;FF[4]GM[1]SZ[{str(n)}]ST[2]CA[UTF-8]AW{white}AB{black})")