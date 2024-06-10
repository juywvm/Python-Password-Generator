H=input
D=''
B=print
import sys,os,random as F,string as C
from colorama import Fore as A,Back,Style
import pyperclip as Q
E=D
def G():os.system('cls'if os.name=='nt'else'clear')
def R():B(D);B(" -- Welcome back to Batus's Password Generator -- ");B(D);B(A.WHITE+' Choose Password Type: ');B(A.WHITE+' 1. Random Generated Password '+A.GREEN+'( Lowercase )');B(A.WHITE+' 2. Random Generated Password '+A.GREEN+'( Uppercase )');B(A.WHITE+' 3. Random Generated Password '+A.GREEN+'( Lowercase + Uppercase )');B(A.WHITE+' 4. Random Generated Password '+A.GREEN+'( Lowercase + Uppercase + Numbers )');B(A.WHITE+' 5. Random Generated Password '+A.GREEN+'( Lowercase + Uppercase + Numbers + Special Symbols )');B(A.WHITE+' 6. Random Generated Password '+A.GREEN+'( Lowercase + Special Symbols ) ');B(A.WHITE+' 7. Random Generated Password '+A.GREEN+'( Lowercase + Numbers ) ');B(A.WHITE+' 8. Random Generated Password '+A.GREEN+'( Uppercase + Special Symbols ) ');B(A.WHITE+' 9. Random Generated Password '+A.GREEN+'( Uppercase + Numbers ) ');B(A.WHITE+' 10. Random Generated Password '+A.GREEN+'( Special Symbols ) ');B(A.WHITE+' 11. Random Generated Password '+A.GREEN+'( Special Symbols + Numbers ) ');B(D);C=H(A.WHITE+' Select Number: ');G();return int(C)
def S(length,chars):return D.join(F.choice(chars)for A in range(length))
def J():global E;E=D
def I():
	P='Type your custom string: ';O='yes'
	while True:
		E=R();L=int(H(A.WHITE+'Enter the desired length for the password: '))
		if E==1:F=C.ascii_lowercase
		elif E==2:F=C.ascii_uppercase
		elif E==3:F=C.ascii_lowercase+C.ascii_uppercase
		elif E==4:F=C.ascii_lowercase+C.ascii_uppercase+C.digits
		elif E==5:F=C.ascii_lowercase+C.ascii_uppercase+C.digits+C.punctuation
		elif E==6:F=C.ascii_lowercase+C.punctuation
		elif E==7:F=C.ascii_lowercase+C.digits
		elif E==8:F=C.ascii_uppercase+C.punctuation
		elif E==9:F=C.ascii_uppercase+C.digits
		elif E==10:F=C.punctuation
		elif E==11:F=C.punctuation+C.digits
		else:B(A.RED+'Invalid selection. Please run the program again.');sys.exit()
		I=D;M=H(A.WHITE+'Would you like to add a custom string to your password? (yes/no): ').strip().lower()
		if M==O:
			G();B(D);I=H(A.WHITE+P)
			while len(I)>=L:G();B(D);B(A.RED+'Custom string length should be less than the total password length.');B(D);I=H(A.WHITE+P)
			G();N=H(A.WHITE+'Are you going to add your custom string to the beginning or end of your password? (beginning/end): ').strip().lower()
		T=L-len(I);K=S(T,F)
		if M==O:
			if N=='beginning':G();J=I+K
			elif N=='end':G();J=K+I
			else:B(A.RED+'Invalid position. Adding custom string at the end by default.');J=K+I
		else:J=K
		B(D);B(A.GREEN+'Your generated password is: '+A.WHITE+J);B(D);Q.copy(J);B('Copied to clipboard... Made by batus with love.');B(D);B(D);B(A.WHITE+'Would you like to:');B(A.WHITE+'1. Return to menu');B(A.WHITE+'2. Exit');B(D);U=H(A.WHITE+'Select Number: ');G()
		if U=='2':break
if __name__=='__main__':G();I()
