import datetime
'''datetime'''

'''storing builtin funtion of date'''
realTime = datetime.datetime.now()
minute =str(datetime.datetime.now().minute)
second =str(datetime.datetime.now().second)
microsecond=str(datetime.datetime.now().microsecond)
uniqueNum = minute + second + microsecond

'''storing textfile data in dictionary'''
def dic_file():
    file = open("books.txt","r")
    dicnumbers = {}
    booksid = 1
    for line in file:
        if line == "\n":
            continue
        line= line.replace("\n","")
        dicnumbers[booksid] = line.split(",")
        booksid = booksid + 1
    file.close()
    return dicnumbers
    print("\n")
    
'''storing dictionary for global use in variable'''  
stockBooksInfo = dic_file()


'''change quantity value from string to integer''' 
for value in stockBooksInfo.values():
    value[2] = int(value[2])
    
'''First heading of program'''
print("\n -------------Welcome to the library management system--------------")

'''arrange dictionary data in table'''
def tabular_format():
    print("\n\n-------------------------------------------------------------------")
    print("{:<13}{:<25}{:<14}{:<10}{:<10}".format("Book ID","Book Name","Author","Quantity","Price"))
    print("-------------------------------------------------------------------")
    for bookID, value in stockBooksInfo.items():
        print(" ","{:<10}{:<23}{:<18}{:<9}{:<10}".format(bookID,value[0],value[1],value[2],value[3]))
    print("-------------------------------------------------------------------")

def borrow_process():
    Totalprice = 0
    Totalborrowed = ""
    bor_name = ""
    loop = False
    test = True
    while loop == False:
        try:
            id_num = int(input("Enter id to borrow books: "))
            if (id_num <= 5 and id_num > 0):
                while(True):
                    for key, value in stockBooksInfo.items():
                        if key == id_num:
                            if value[2] <= 0:
                                print("\n------------------------------------\nBook is not available.\n------------------------------------\n")
                                input("Press any key to continue.\n")
            
                                test = False
                            else:
                                print("\n------------------------------------\nBook is available\n"
                                    "------------------------------------\n")
                                while(True):
                                    bor_name = (input("Enter the name of the borrower: "))
                                    if bor_name:
                                        value[2] -= 1
                                        price = float(value[3].replace("$",""))
                                        bor_book = (value[0])
                                        Totalborrowed = "\n" + Totalborrowed + bor_book + "\n"
                                        Totalprice = Totalprice + price
                                        print("\n------------------------------------\nSuccessfully borrowed\n------------------------------------")
                                        tabular_format()
                                        test = True
                                        break
                                    else:
                                        print("\n------------------------------------\nPlease input something \n------------------------------------\n")
                                    
                    break
                if not test:
                    continue
                        
                        
                                        
                '''For multiple choice'''
                while True:
                    print("Do you want to borrow another book? \n")
                    Boolen = (input("If 'Yes' enter 'y' or enter any words to exit this loop:"))            
                    if (Boolen.upper()=='Y'):
                        while(True):
                            id_numinner = int(input("Enter id to borrow books: "))
                            if (id_numinner <= 5 and id_numinner > 0):
                                for key, value in stockBooksInfo.items():
                                    
                                    if key == id_numinner:
                                        if value[2] <= 0:
                                            print("\n------------------------------------\nBook is not available.\n------------------------------------\n")
                                            input("Press any key to continue.")
                                            
                                        else:
                                            print("\n------------------------------------\nSuccessfully borrowed\n------------------------------------\n")
                                            value[2] -= 1
                                            bor_book = str(value[0])
                                            Totalborrowed = Totalborrowed + bor_book + "\n"
                                            price = float(value[3].replace("$",""))
                                            Totalprice = Totalprice + price
                                            tabular_format()
                                        
                                break
                            else:
                                print("\n------------------------------------\nPlease input valid id \n------------------------------------\n")
                    else:
                        
                        '''assist to generate bill of the borrower'''
                        file = open("borrow_database.txt","a")
                        file.write("\n-------------------------------------------------------------------\n                        Customer's Details                     \n-------------------------------------------------------------------\n")
                        file.write("The name of the borrower is: "+ bor_name+"("+str(uniqueNum)+")"+"\n"+"The total price is: $"+str(Totalprice)+"\n"+"The date and time while borrowing book was:"+str(realTime)+"\n"+"The borrowed books are: "+Totalborrowed+"\n")
                        file.write("-------------------------------------------------------------------")
                        file.close()

                        
                        '''display details of borrower in terminal'''
                        print("\n-------------------------------------------------------------------\n                        Customer's Details                     \n-------------------------------------------------------------------")
                        print("The name of the borrower is: "+ bor_name+"("+str(uniqueNum)+")"+"\n"+"The total price is: $"+str(Totalprice)+"\n"+"The date and time while borrowing book was:"+str(realTime)+"\n"+"The borrowed books are: "+Totalborrowed)
                        print("-------------------------------------------------------------------")
                        print()
                        print("\n-------------------------------------------------------------------\n               Thank You for borrowing books\n--------------------------------------------------------------------")

                        '''assist to update text file after borrowing books'''
                        file = open("books.txt","w")
                        for value in stockBooksInfo.values():
                            file.write(value[0]+","+value[1]+","+str(value[2])+","+value[3]+"\n")
                        file.close()
                        break
                loop = True
                
            else:
                print("\n----------------------------------------\nBookid not available\n---------------------------------------\n")
        except:
            print("\n----------------------------------------\nPlease input valid Bookid \n---------------------------------------\n")
    
def return_process():
    totalReturn = ""
    returnName = ""
    totalCharge = 0
    while True:
        try:
            id_num = int(input("Enter id to return books: "))
            if (id_num <= 5 and id_num > 0):
                while True:
                    returnName = (input("\nEnter the name who want to return book: "))
                    if (returnName):
                        for key, value in stockBooksInfo.items():
                            if key == id_num:
                                value[2] += 1
                                price = float(value[3].replace("$",""))
                                returnValue = str(value[0])
                                totalReturn = "\n" + totalReturn + returnValue + "\n"
                                Boolen = (input("\nHas it been more than 10 days?\nIf yes enter 'y' or input any word to continue loop :"))
                                if (Boolen.upper()=='Y'): 
                                    lateDays = int(input("\nInput the number of days that was late: "))
                                    charge = 0.2*lateDays
                                    totalCharge = totalCharge + charge
                                    print("\n-----------------------------------------------------------\nThe charge for not submitting this book in time is: $",charge,"\n-----------------------------------------------------------\n")
                                    tabular_format()
                                else:
                                    continue
                        break
                    else:
                        print("\n-----------------------------------------------------------\nPlease,Input something\n-----------------------------------------------------------\n")
                    
            else:
                print("\n-----------------------------------------------------------\nBookid not available\n-----------------------------------------------------------\n")
                continue                    
            '''For multiple choice'''
            while True:
                print("Do you want to return another book? \n")
                Boolen = (input("If 'Yes' enter 'y' or enter any words to exit:"))            
                if (Boolen.upper()=='Y'): 
                    id_numinner = int(input("Enter id to return books: "))
                    Boolen = (input("\nHas it been more than 10 days?\nIf yes enter 'y' or input any number to continue another process :"))
                    if (Boolen.upper()=='Y'): 
                        lateDays = int(input("\nInput the number of days that was late: "))
                        charge = 0.2*lateDays
                        totalCharge = totalCharge + charge
                        print("\n-----------------------------------------------------------\nThe charge for not submitting this book in time is: $",charge,"\n-----------------------------------------------------------\n")
                    for key, value in stockBooksInfo.items():
                        if key == id_numinner:
                            value[2] += 1
                            returnValue = str(value[0])
                            totalReturn = totalReturn + returnValue + "\n"
                            tabular_format()
                else:                     
                    '''assist to know about the detail of book returned'''
                    file = open("return_database.txt","a")
                    file.write("\n-------------------------------------------------------------------\n")
                    file.write("                        Customer's Details                     \n")
                    file.write("-------------------------------------------------------------------\n")
                    file.write("The name who has returned book is: "+ returnName+"("+str(uniqueNum)+")"+"\n"+"The date and time while returning book was:"+str(realTime)+"\n"+"The returned books are: "+totalReturn+
                               "The total charge is: $"+str(totalCharge))
                    file.write("\n-------------------------------------------------------------------")
                    file.close()

                                
                    '''display details of borrower in running code'''
                    print("\n-------------------------------------------------------------------\n")
                    print("                        Customer's Details                     \n")
                    print("-------------------------------------------------------------------\n")
                    print("The name who has returned book is: "+ returnName+"("+str(uniqueNum)+")"+"\n"+"The date and time while returning book was:"+str(realTime)+"\n"+"The returned books are: "+totalReturn+
                          "The total charge is: $",str(totalCharge))
                    print("-------------------------------------------------------------------")
                    print()
                    print("\n----------------------------------------\n         Thank You for returning books\n---------------------------------------")
                    '''assist to update text file after borrowing books'''
                    file = open("books.txt","w")
                    for value in stockBooksInfo.values():
                        file.write(value[0]+","+value[1]+","+str(value[2])+","+value[3]+"\n")
                    file.close()
                    break
            break
        except:
            print("\n----------------------------------------\nPlease input valid bookid\n----------------------------------------\n")
