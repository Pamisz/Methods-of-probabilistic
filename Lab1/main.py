class lcg:
    def __init__(self,a , c , m, seed):
        self.a = a
        self.c = c
        self.m = m
        self.seed = seed
    
    def generate(self):
        self.seed = (self.a*self.seed + self.c) % self.m
        return self.seed 
    

a = 69069
c = 1
m = 2**31
seed = 123456789
N = 100000

buff = lcg(a,c,m,seed)

numbers = [buff.generate() for _ in range(N)]
test1=0
test2=0 
test3=0 
test4=0  
test5=0 
test6=0 
test7=0 
test8=0 
test9=0 
test10=0 
zakres_start = ((2**31)-1)/10

for i in range(len(numbers)):
    if 0 < numbers[i] and numbers[i] <= zakres_start:
        test1 = test1 + 1
        
    if zakres_start < numbers[i] and numbers[i] <= 2*zakres_start:
        test2 = test2 + 1
        
    if 2*zakres_start < numbers[i] and numbers[i] <= 3*zakres_start:
        test3 = test3 + 1
        
    if 3*zakres_start < numbers[i] and numbers[i] <= 4*zakres_start:
        test4 = test4 + 1
        
    if 4*zakres_start < numbers[i] and numbers[i] <= 5*zakres_start:
        test5 = test5 + 1
        
    if 5*zakres_start < numbers[i] and numbers[i] <= 6*zakres_start:
        test6 = test6 + 1
        
    if 6*zakres_start < numbers[i] and numbers[i] <= 7*zakres_start:
        test7 = test7 + 1
        
    if 7*zakres_start < numbers[i] and numbers[i] <= 8*zakres_start:
        test8 = test8 + 1
        
    if 8*zakres_start < numbers[i] and numbers[i] <= 9*zakres_start:
        test9 = test9 + 1 
        
    if 9*zakres_start < numbers[i] and numbers[i] <= 10 * zakres_start:
        test10 = test10 + 1   
        
testy = [test1,test2,test3,test4,test5,test6,test7,test8,test9,test10]
print(testy)
    
