'''  1  1  1    becomes   3  2  1
     2  2  2              3  2  1
     3  3  3              3  2  1'''
#correct opt
class rotate:
    def rotate(self,l):
        new = []
        old = []
        for i in range(0,len(l)):
            length = len(l)
            for j in range(0,len(l)):
                old.append(l[length-1][i])
                #print( change,i,j)
                length -= 1
            new.append(old[:])
            old.clear()#
        return new        

def main():
    rt=rotate()
    lst =[[1,1,1],
        [2,2,2],
        [3,3,3] ]
    res=rt.rotate(lst) 
    print(res) 
if __name__ == "__main__":
    main()  
