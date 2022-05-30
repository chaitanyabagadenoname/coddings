l=[]
while True :
	c=int(input('''
	                     1 push elements
	                     2 pop elements
	                     3 peek elements
	                     4 display stack
	                     5 exit 
	 
	Enter the number of performance type :-'''))
	if c==1:
		n=input("Enter the value :-")
		l.append(n)
		print(l)
	elif c==2:
		if len(l)==0:
			print("Empty stack")
		else:
			p=l.pop()
			print(p)
			print(l)
			
	elif c==3:
		if len(l)==0:
			print("Empty stack")
		else:
			print("last stack value :-",l[-1])
	
	elif c==4:
		print("dispaly stack :",l)
		
	elif c==5:
		break;
	else:
		print("invalice performance")
			