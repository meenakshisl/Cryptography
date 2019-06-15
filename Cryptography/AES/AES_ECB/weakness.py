#purpose of program is to demonstrate the weakness of aes-ecb mode . IT is an independent cipher mode .So if your input contains
#two similiar blocka the corresponding cipher blocks produced too would be same and in case of encryption of large files it becomes a security 
#vulnerability...
#
#The following code checks if the cipher text contains two siliar blocks and if yes prints it
#NOTE : I have encrypted and decrypted by importing aes_ecb.py I wrote .So in order for the code to excecute properlt the mentioned file should be in the same folder.




import aes_ecb as obj
i=0
j=0
ct_list=list()

def _split(ct) :    
#------function to split the given text into blocks-----------------------------#

    n=len(ct)/16
    j=0
    for i in range(n) :
        
        ct_list.append(ct[j:(j+16)])
        j=j+16
    check_block(ct_list)


def check_block(ct_list) :
#--------function checks for similiar blocks and if it exists prints then and gives a warning--
    l=len(ct_list)
    for i in range(l) :
        for j in range(l) :

            if (i!=j) and (ct_list[i]==ct_list[j]) :
                print ct_list[i],ct_list[j]
                print "Blocks are same.Thus weakness illustrated"
                return


if __name__=="__main__" :
    #-------main function :just takes in plain text as input--------------
    pt=raw_input("Enter the plain text")
    ct=obj.encrypt_ecb(pt)
    _split(ct)







