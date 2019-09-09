def accordian(l):
    (i,temp1)=(1,0)
    (inc,dec)=(0,0)
    while i < len(l):
        tem=diff(l[i],l[i-1])
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

def diff(a,b):
    ma=max(a,b)
    mi=min(a,b)
    return (ma-mi)
      
def main():
l=[1,5,2,8,3]
res=accordian(l)
print(res)
if __name()__==__main()__:
     main()
