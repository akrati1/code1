class strict_increase():
    def expanding(self,l):
        (i,temp1)=(1,0)
        (inc,dec)=(0,0)
        while i < len(l):
            tem=self.diff(l[i],l[i-1])
            if  tem > temp1 :
                temp1=tem
                if i==1:
                    inc==0
                if i>1:
                    inc=inc+1
                if dec>0:
                    dec=dec-1
                if inc>1:
                    return False
            elif  tem < temp1 :
                temp1=tem
                dec=dec + 1 
                if inc > 0 :
                    inc=inc-1
                if dec > 1:
                    return False 
            else :
                return False        
            i=i+1  
        return True
    def diff(self,a,b):
        ma=max(a,b)
        mi=min(a,b)
        return (ma-mi)
def main():
    si=strict_increase()
    l=[1,5,1]
    res=si.expanding(l) 
    print(res)  
if __name__ == "__main__":
    main() 
    
    
    # accordian([-2,1,5,2,8,3]) output=True
    """Explanation: Differences between adjacent elements 
    are 1-(-2) = 3, 5-1 = 4, 5-2 = 3, 8-2 = 6, 8-3 = 5, so the differences increase, decrease, 
    increase and then decrease."""
    # l=[12,55,22,88,40]  output=True. 
