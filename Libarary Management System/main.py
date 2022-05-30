'''This system is develop to make library management system'''
from functions import*  
'''function runLibrary is created'''
def runLibrary():
    '''Using while loop to execute our main program'''
    tabular_format()
    loop = False
    while loop == False:
        try:
            print("\n")
            print("Enter 1. To Borrow a book")
            print("Enter 2. To return a book")
            print("Enter 3. To exit")
            num=(input("Select a choice from 1-3: "))
            '''create new line by giving null parameter in print statement'''
            print()
            if num:
                num = int(num)
                if(num==1):
                    borrow_process()       
                            
                elif(num==2):
                    return_process()
                elif(num==3):
                    print("------------------------------------\nThank you for using this system \n------------------------------------\n")
                    '''return helps to break the program when 3 is entered by user'''
                    return 
                else:
                    print("------------------------------------\nPlease enter valid number from 1-3 \n------------------------------------\n")
            else:
                print("Please enter an option.")
                input("Press Enter to continue.")
                
        except:
            print("------------------------------------\nInvalid input. Please try again\n------------------------------------\n")

'''This statement helps to run the runlibrary funtion'''
runLibrary()
