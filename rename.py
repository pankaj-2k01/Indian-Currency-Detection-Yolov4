import os
import stat

def main():
   
    folder = "Images/2000"
    print(os.listdir(folder))
    name=2000
    for i in range(1,51):
        os.rename(folder+'/'+str(i)+'.png',folder+'/'+str(name)+'.png')
        os.rename(folder+'/'+str(i)+'.txt',folder+'/'+str(name)+'.txt')

        os.rename(folder+'/'+str(i)+'_cb.png',folder+'/'+str(name)+'_cb.png')
        os.rename(folder+'/'+str(i)+'_cb.txt',folder+'/'+str(name)+'_cb.txt')

        os.rename(folder+'/'+str(i)+'_sharp.png',folder+'/'+str(name)+'_sharp.png')
        os.rename(folder+'/'+str(i)+'_sharp.txt',folder+'/'+str(name)+'_sharp.txt')
        name=name+1
        
        



main()