#create the encryption code
codes = {'A':'*','a':'>','B':'0','b':'.','C':',','c':'<','D':'6','d':'?','E':'/','e':']','F':'-','f':'5','G':'+',
'g':'[','H':'=','h':'9','I':'~','i':':','J':';','j':'8','K':'{','k':'90','L':'*0','l':'1','M':'??','m':'44','N':'}','n':'!@',
'O':'()','o':'2','P':'$%','p':'*&','Q':'3','q':'.,','R':'7','r':'!^','S':'++','s':'56','T':'88','t':'4','U':'.?','u':'87','V':'12',
'v':'%','W':'$','w':'^','X':'#','x':'&','Y':'@','y':'(','Z':'!','z':')','.':'00',':':'Rx',' ':'pp',',':'FS','<':'}u'}


#open the text file and read its contents
security_file = open("info_security.txt",'r')
input_file = security_file.read()
security_file.close


#create a 2nd file
outfile = open("encrypted_version.txt",'w')


#write the encrypted version to the second file
for char in input_file:
    outfile.write(codes[char])

outfile.close
   
  

