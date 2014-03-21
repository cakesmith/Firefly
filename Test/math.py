class test:


    mylist = []
    
    def setint(n):
        
        c = n % 10
        
        
        
        if n < 10:
            return c
        else:
            test.mylist.append(test.setint(n/10))
            
        
