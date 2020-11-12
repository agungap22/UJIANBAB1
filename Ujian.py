

################################# NOMOR 1 ##############################
# def create_phone_number (number) :
#     numberlist=list(number)
#     numberstr=str(number)
#     symbol='!@#$%&*()_+-=[]{\}|,.<>/?;:`~'    
#     if numberstr.isalpha():
#         print ("Invalid Input. No alphabet")
#     elif int(number) < 0 :
#         print ("Input only positive number")
#     elif len(numberlist) < 10 :
#         print ("Digits must be in length of 10, not more or less")
#     elif  numberstr in symbol :
#         print ("Invalid input. No symbols.")
#     else :
#         # print ("(",str(numberlist[0:3]),")",str(numberlist[3:6]),"-",str(numberlist[6:11]))
#         print ("(",str(number[0:3]),")",str(number[3:6]),"-",str(number[6:11]))
    

# create_phone_number(number=input("Input Number (ONLY NUMBER) :"))

################################# NOMOR 2 ##############################
# def move_zero(x) :
#     print(x)
#     kosong =[]
#     kosong2 =[]
#     for i in range(len(x)):
#         if x[i]=='0' or x[i]==0:
#             continue
#         else : 
#             kosong.append(x[i])
#     for y in range(len(x)):
#         if x[y] == 0 or x[y] =='0':
#             kosong2.append(x[y])
#         else :
#             continue
#     for z in range(len(kosong2)):
#         kosong.append(kosong2[z])
#     return kosong
    
# x = [0,0,0,0,True,0,0,9,6,4,'a','mobil']  
# print(move_zero(x)) 

################################# NOMOR 3 ##############################
# import statistics as st

class Statistic:
    def mean(self) :
       a = 0
       for i in self :
        a += i
       
       r=a//len(self)
       return r 
    
    def median(self) :
        b = self.sort()
        if : 
        elif : len(b) % 2 = 0 :
            c = len(b)//2
            tengah =(b[c+1]+b[c])//2
        return tengah
        else :
           c = (len(b)+1)//2
           tengah=b[c]
        return tengah    

    # def mode(self) :

    def std(self) :
        for i in len(self):

S = Statistic()







