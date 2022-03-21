import sys

#a=input("a:")
#b=input("b:")

#sys.exit()

#c=input("c:")

#sys.stderr.write("bu bir hata mesajıdır\n")
#sys.stderr.flush()

#sys.stdout.write("bu normal bir yazıdır\n")

#print(sys.argv)

#for i in sys.argv:
    #print(i)
#print(sys.argv)

def kök_bulma(a,b,c):
    delta=b**2-4*a*c

    if (delta<0):
        print("reel kök yoktur!")

    else:
        kok1= (-b + delta**0.5)/ (2*a)
        kok2= (-b - delta ** 0.5) / (2*a)
        return (kok1,kok2)


if len(sys.argv)==4:
    print("denklemin kökleri:",kök_bulma(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))

else:
    sys.stderr.write("lütfen girdiğiniz değerleri kontrol ediniz!!!")
    sys.stderr.flush()











