#generate_password


         #Task No.3 , (PASSWORD GENERATOR)

import random
def  generate_password():
    
            password=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j', 'k', 
             'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
             'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6',
             '7', '8', '9']
            
            user_prompt=int(input("ENTER LENGTH OF THE PASSWORD :"))

            passwd="" 
            for x in range(user_prompt):
                passwd=passwd+random.choice(password)
                
            print("YOUR GENERATED PASSWORD IS :",passwd)

generate_password()
                                       
     