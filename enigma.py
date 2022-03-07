class Enigma:
    def __init__(self,w1,position1,w2,position2,w3,position3,umkehrwalze):
        walze1 = [Walze(),Walze(),Walze(),Walze(),Walze()]
        
        
    

class Walze:
    
    übertragskerbe=1000
    position=0
    
    def __init__(self,nummer):
        if(nummer=='1'):
            self.verdrahtung=[5,11,13,6,12,7,4,17,22,26,14,20,15,23,25,8,24,21,19,16,1,9,2,18,3,10]
            self.übertragskerbe=17
            
        if(nummer=='2'):
            self.verdrahtung=[1,10,4,11,19,9,18,21,24,2,12,8,23,20,13,3,17,7,26,14,16,25,6,22,15,5]
            self.übertragskerbe=5
            
        if(nummer=='3'):
            self.verdrahtung=[2,4,6,8,10,12,3,16,18,20,24,22,26,14,25,5,9,23,7,1,11,13,21,19,17,15]
            self.übertragskerbe=22
            
        if(nummer=='4'):
            self.verdrahtung=[5,19,15,22,16,26,10,1,25,17,21,9,18,8,24,12,14,6,20,7,11,4,3,13,23,2]
            self.übertragskerbe=10
            
        if(nummer=='5'):
            self.verdrahtung=[22,26,2,18,7,9,20,25,21,16,19,4,14,8,12,24,1,23,13,10,17,15,6,5,3,11]
            self.übertragskerbe=26
            
        if(nummer=='6'):
            self.verdrahtung=[10,16,7,22,15,21,13,6,25,17,2,5,14,8,26,18,4,11,1,19,24,12,9,3,20,23]
            self.übertragskerbe=100 #zwei Kerben!
            
        if(nummer=='7'):
            self.verdrahtung=[14,26,10,8,7,18,3,24,13,25,19,23,2,15,21,6,1,9,22,12,16,5,11,17,4,20]
            self.übertragskerbe=100 #zwei Kerben!
            
        if(nummer=='8'):
            self.verdrahtung=[6,11,17,8,20,12,24,15,3,2,10,19,16,4,26,18,1,13,5,23,14,9,21,25,7,22]
            self.übertragskerbe=100 #zwei Kerben!
            
        if(nummer=='A'):
            self.verdrahtung=[5,10,13,26,1,12,25,24,22,2,23,6,3,18,17,21,15,14,20,19,16,9,11,8,7,4]
        if(nummer=='B'):
            self.verdrahtung=[25,18,21,8,17,19,12,4,16,24,14,7,15,11,13,9,5,2,6,26,3,23,22,10,1,20]
        if(nummer=='C'):
            self.verdrahtung=[6,22,16,10,9,1,15,25,5,4,18,26,24,23,7,3,20,11,21,17,19,2,14,13,8,12]
            
    def drehen(self):
        self.position+=1