import math
from os import system, name
from time import sleep
from collections import defaultdict

class Account:
    '''
        MAIN CLASS
    '''
    class_list = {}
    data = []
    temp = []
    def __init__(self):
        self.class_list
        self.data
        self.temp

    def menu(self):
        print("=========================================")
        print("|       Welcome to Bank GankBank        |")
        print("=========================================")
        print("1. Sign up")
        print("2. Sign in")
        print("3. Exit")
        print("=========================================")

    def create_account(self):
        print("=========================================")
        print("|        Sign up a new account         |")
        print("=========================================")
        self.__Name = input("Input your name : ")
        self.__AccNum = input("Input Your Account Number : ")
        self.__Pin  = input("Input Your PIN : ")
        self.__ammount = float(input("Input your first deposite (min: $100) : "))
        self.data.append(self.__Name)
        self.data.append(self.__AccNum)
        self.data.append(self.__ammount)
        self.class_list[self.__Pin] = [self.__Name,self.__AccNum,self.__ammount]                                                    
        print("=========================================")
        print("Your Account Has Been Create")
    
    def clear(self): 
        sleep(2)
        if name == 'nt': 
            _ = system('cls') 
        else: 
            _ = system('clear')
        



class ATM(Account):
    def __init__(self):
        print("")
    
    def summon(self):
        self.menu()
        choice = int(input("Input Your Choice : "))
        while True:
            if choice == 1:
                self.create_account()
                break
            elif choice == 2:
                self.login()
            else:
                print("Thank Your, Have A Nice Day :)")
    def menuATM(self):
        print("=========================================")
        print("|                  Menu                 |")
        print("=========================================")
        print("1. Withdraw")
        print("2. Transfer")
        print("3. Check Balance")
        print("4. Next Menu")
        print("5. Log Out")
        print("6. Exit")
        print("=========================================")
        choice = int(input("Input Your Choice : "))
        while True:
            if choice == 1:
                self.withdraw()
                break
            elif choice == 2:
                self.transfer()
            elif choice == 3:
                self.display()
            elif choice == 4:
                self.display()
            elif choice == 5:
                self.summon()
            elif choice == 6:
                self.clear()
                print("You can access this apps on Github")
                print("visit github.com/andres-sumihe/OOP-with-python-3")
                print("Thanks")
                quit()

            else:
                print("Please enter valid input")
        

    def login(self):
        print("=========================================")
        print("|         Sign in your account          |")
        print("=========================================")
        print(self.class_list)
        InAccNum = input("Input Your Account Number : ")
        InputPin = input("Input Your PIN :")
        for i in self.class_list:
            if InputPin == i:
                print("test", i[0])
                if self.class_list[i[0]][1] == InAccNum:
                    # self.temp.append(self.class_list[i[0]][2])
                    self.temp.append(i[0])
                    print(self.temp[0])
                    print("Login Success")
                    # self.clear()
                    self.menuATM()
            else: break
        else:
            print("Please Sign up")
            self.summon()
                    
    def transfer(self):
        reciever = input("Enter destination account number: ")
        amount = float(input("Enter amount to be Deposited: "))
        for i in self.class_list:
            if reciever in self.class_list[i][1]:
                self.class_list[i][2] += amount
                self.class_list[self.temp[0]][2] -= amount
                print(self.class_list[self.temp[0]][2])
                print("Found")
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.class_list[self.temp[0]][2] >= amount:
            self.class_list[self.temp[0]][2] -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
    def display(self):
        self.clear()
        print("\n Net Available Balance= ", self.class_list[self.temp[0]][2])
        self.menuATM()



class online_payment(ATM):
    def __init__(self):
        print("")
    
    def menuATM(self):
        print("=========================================")
        print("|                  Menu                 |")
        print("=========================================")
        print("1. Withdraw")
        print("2. Transfer")
        print("3. Check Balance")
        print("4. Next Menu")
        print("5. Log Out")
        print("6. Exit")
        print("=========================================")
        choice = int(input("Input Your Choice : "))
        while True:
            if choice == 1:
                self.withdraw()
                break
            elif choice == 2:
                self.transfer()
            elif choice == 3:
                self.display()
            elif choice == 4:
                self.summon_online_payment()
            elif choice == 5:
                self.summon()
            elif choice == 6:
                self.clear()
                print("You can access this apps on Github")
                print("visit github.com/andres-sumihe/OOP-with-python-3")
                print("Thanks")
                quit()

            else:
                print("Please enter valid input")
    def menu_online_payment(self):
        print("=========================================")
        print("|       Welcome to Online Payment       |")
        print("=========================================")
        print("1. Pulsa")
        print("2. Token Listrik")
        print("3. Exit")
        print("=========================================")
        
    def pulsa(self):
        print("\n=========================================")
        print("|       welcome to pulsa purchase       |")
        print("=========================================")
        print("\nplease choose your Perdana card: ")
        print("1. TELKOMSEL")
        print("2. XL")
        print("3. IM3")
        print("4. AXIS")
        print("5. TRI")
        print("6. Back")
        
    def token_listrik(self):
        print("\n=========================================")
        print("|    welcome to Token Listrik purchase  |")
        print("=========================================")
    
    def menu_pulsa(self):
        self.pulsa()
        choise_pulsa = int(input("Input Your Choice : "))
        while True:
            if choise_pulsa == 1:
                int(input("TELKOMSEL \nEnter your mobile number: "))
                print("Select the credit you want to buy: ")
                print("1. Rp.5,000 \n2. Rp.10,000 \n3. Rp.20,000 \n4. Rp.50,000 \n5. Rp.100,000 \n6. Back")
                ptelkomsel = int(input("Input Your Choice: "))
                while True:
                    if ptelkomsel == 1:
                        if self.class_list[self.temp[0]][2] >= 5000 :
                            telkomsel5 = self.class_list[self.temp[0]][2] - 5000
                            print("Telkomsel credit purchases successful")
                            print("Your remaining balance is ",telkomsel5)
                            print("\nThank Your, Have A Nice Day :)")
                        else : 
                            print("the balance is not enough!\n")
                            online_payment()
                            self.menu_online_payment()
                            self.summon_online_payment()
                        break
                    elif ptelkomsel == 2:
                        if self.class_list[self.temp[0]][2] >= 10000 :
                            telkomsel10 = self.class_list[self.temp[0]][2] - 10000
                            print("Telkomsel credit purchases successful")
                            print("Your remaining balance is ",telkomsel10)
                            print("\nThank Your, Have A Nice Day :)")
                        else : 
                            print("the balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif ptelkomsel == 3:
                        if self.class_list[self.temp[0]][2] >= 20000 :
                            telkomsel20 = self.class_list[self.temp[0]][2] - 20000
                            print("Telkomsel credit purchases successful")
                            print("Your remaining balance is ",telkomsel20)
                            print("\nThank Your, Have A Nice Day :)")
                        else : 
                            print("the balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif ptelkomsel == 4:
                        if self.class_list[self.temp[0]][2] >= 50000 :
                            telkomsel50 = self.class_list[self.temp[0]][2] - 50000
                            print("Telkomsel credit purchases successful")
                            print("Your remaining balance is ",telkomsel50)
                            print("\nThank Your, Have A Nice Day :)")
                        else : 
                            print("the balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif ptelkomsel == 5:
                        if self.class_list[self.temp[0]][2] >= 100000 :
                            telkomsel100 = self.class_list[self.temp[0]][2] - 100000
                            print("Telkomsel credit purchases successful")
                            print("Your remaining balance is ",telkomsel100)
                            print("\nThank Your, Have A Nice Day :)")
                        else : 
                            print("the balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif ptelkomsel == 6:
                        self.pulsa()
                        self.menu_pulsa()
                        break
                    else :
                        print("enter the correct input")
                        self.menu_pulsa() 
                break
            elif choise_pulsa == 2:
                int(input("XL \nEnter your mobile number: "))
                print("Select the credit you want to buy: ")
                print("1. Rp.5,000 \n2. Rp.10,000 \n3. Rp.20,000 \n4. Rp.50,000 \n5. Rp.100,000 \n6. Back")
                pxl = int(input("Input Your Choice: "))
                while True:
                    if pxl == 1:
                        if self.class_list[self.temp[0]][2] >= 5000 :
                            pxl5 = self.class_list[self.temp[0]][2] - 5000
                            print("Telkomsel credit purchases successful")
                            print("Your remaining balance is ",pxl5)
                            print("\nThank Your, Have A Nice Day :)")
                        else : 
                            print("the balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif pxl == 2:
                        if self.class_list[self.temp[0]][2] >= 10000 :
                            pxl10 = self.class_list[self.temp[0]][2] - 10000
                            print("Telkomsel credit purchases successful")
                            print("Your remaining balance is ",pxl10)
                            print("\nThank Your, Have A Nice Day :)")
                        else : 
                            print("the balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif pxl == 3:
                        if self.class_list[self.temp[0]][2] >= 20000 :
                            pxl20 = self.class_list[self.temp[0]][2] - 20000
                            print("Telkomsel credit purchases successful")
                            print("Your remaining balance is ",pxl20)
                            print("\nThank Your, Have A Nice Day :)")
                        else : 
                            print("the balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif pxl == 4:
                        if self.class_list[self.temp[0]][2] >= 50000 :
                            pxl50 = self.class_list[self.temp[0]][2] - 50000
                            print("Telkomsel credit purchases successful")
                            print("Your remaining balance is ",pxl50)
                            print("\nThank Your, Have A Nice Day :)")
                        else : 
                            print("the balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif pxl == 5:
                        if self.class_list[self.temp[0]][2] >= 100000 :
                            pxl100 = self.class_list[self.temp[0]][2] - 100000
                            print("Telkomsel credit purchases successful")
                            print("Your remaining balance is ",pxl100)
                            print("\nThank Your, Have A Nice Day :)")
                        else : 
                            print("the balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif pxl == 6:
                        self.pulsa()
                        self.menu_pulsa()
                        break
                    else :
                        print("enter the correct input")
                        self.menu_pulsa()
                break
            elif choise_pulsa == 3:
                int(input("IM3 \nEnter your mobile number: "))
                print("Select the credit you want to buy: ")
                print("1. Rp.5,000 \n2. Rp.10,000 \n3. Rp.20,000 \n4. Rp.50,000 \n5. Rp.100,000 \n6. Back")
                pim3 = int(input("Input Your Choice: "))
                while True:
                    if pim3 == 1:
                        if self.class_list[self.temp[0]][2] >= 5000 :
                            pim35 = self.class_list[self.temp[0]][2] - 5000
                            print("Telkomsel credit purchases successful")
                            print("Your remaining balance is ",pim35)
                            print("\nThank Your, Have A Nice Day :)")
                        else : 
                            print("the balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif pim3 == 2:
                        if self.class_list[self.temp[0]][2] >= 10000 :
                            pim310 = self.class_list[self.temp[0]][2] - 10000
                            print("Telkomsel credit purchases successful")
                            print("Your remaining balance is ",pim310)
                            print("\nThank Your, Have A Nice Day :)")
                        else : 
                            print("the balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif pim3 == 3:
                        if self.class_list[self.temp[0]][2] >= 20000 :
                            pim320 = self.class_list[self.temp[0]][2] - 20000
                            print("Telkomsel credit purchases successful")
                            print("Your remaining balance is ",pim320)
                            print("\nThank Your, Have A Nice Day :)")
                        else : 
                            print("the balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif pim3 == 4:
                        if self.class_list[self.temp[0]][2] >= 50000 :
                            pim350 = self.class_list[self.temp[0]][2] - 50000
                            print("Telkomsel credit purchases successful")
                            print("Your remaining balance is ",pim350)
                            print("\nThank Your, Have A Nice Day :)")
                        else : 
                            print("the balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif pim3 == 5:
                        if self.class_list[self.temp[0]][2] >= 100000 :
                            pim3100 = self.class_list[self.temp[0]][2] - 100000
                            print("Telkomsel credit purchases successful")
                            print("Your remaining balance is ",pim3100)
                            print("\nThank Your, Have A Nice Day :)")
                        else : 
                            print("the balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif pim3 == 6:
                        self.pulsa()
                        self.menu_pulsa()
                        break
                    else :
                        print("enter the correct input")
                        self.menu_pulsa()
                break
            elif choise_pulsa == 4:
                int(input("AXIS \nEnter your mobile number: "))
                print("Select the credit you want to buy: ")
                print("1. Rp.5,000 \n2. Rp.10,000 \n3. Rp.20,000 \n4. Rp.50,000 \n5. Rp.100,000 \n6. Back")
                paxis = int(input("Input Your Choice: "))
                while True:
                    if paxis == 1:
                        if self.class_list[self.temp[0]][2] >= 5000 :
                            paxis5 = self.class_list[self.temp[0]][2] - 5000
                            print("Telkomsel credit purchases successful")
                            print("Your remaining balance is ",paxis5)
                            print("\nThank Your, Have A Nice Day :)")
                        else : 
                            print("the balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif paxis == 2:
                        if self.class_list[self.temp[0]][2] >= 10000 :
                            paxis10 = self.class_list[self.temp[0]][2] - 10000
                            print("Telkomsel credit purchases successful")
                            print("Your remaining balance is ",paxis10)
                            print("\nThank Your, Have A Nice Day :)")
                        else : 
                            print("the balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif paxis == 3:
                        if self.class_list[self.temp[0]][2] >= 20000 :
                            paxis20 = self.class_list[self.temp[0]][2] - 20000
                            print("Telkomsel credit purchases successful")
                            print("Your remaining balance is ",paxis20)
                            print("\nThank Your, Have A Nice Day :)")
                        else : 
                            print("the balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif paxis == 4:
                        if self.class_list[self.temp[0]][2] >= 50000 :
                            paxis50 = self.class_list[self.temp[0]][2] - 50000
                            print("Telkomsel credit purchases successful")
                            print("Your remaining balance is ",paxis50)
                            print("\nThank Your, Have A Nice Day :)")
                        else : 
                            print("the balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif paxis == 5:
                        if self.class_list[self.temp[0]][2] >= 100000 :
                            paxis100 = self.class_list[self.temp[0]][2] - 100000
                            print("Telkomsel credit purchases successful")
                            print("Your remaining balance is ",paxis100)
                            print("\nThank Your, Have A Nice Day :)")
                        else : 
                            print("the balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif paxis == 6:
                        self.pulsa()
                        self.menu_pulsa()
                        break
                    else :
                        print("enter the correct input")
                        self.menu_pulsa()
                break
            elif choise_pulsa == 5:
                int(input("TRI \nEnter your mobile number: "))
                print("Select the credit you want to buy: ")
                print("1. Rp.5,000 \n2. Rp.10,000 \n3. Rp.20,000 \n4. Rp.50,000 \n5. Rp.100,000 \n6. Back")
                ptri = int(input("Input Your Choice: "))
                while True:
                    if ptri == 1:
                        if self.class_list[self.temp[0]][2] >= 5000 :
                            ptri5 = self.class_list[self.temp[0]][2] - 5000
                            print("Telkomsel credit purchases successful")
                            print("Your remaining balance is ",ptri5)
                            print("\nThank Your, Have A Nice Day :)")
                        else : 
                            print("the balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif ptri == 2:
                        if self.class_list[self.temp[0]][2] >= 10000 :
                            ptri10 = self.class_list[self.temp[0]][2] - 10000
                            print("Telkomsel credit purchases successful")
                            print("Your remaining balance is ",ptri10)
                            print("\nThank Your, Have A Nice Day :)")
                        else : 
                            print("the balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif ptri == 3:
                        if self.class_list[self.temp[0]][2] >= 20000 :
                            ptri20 = self.class_list[self.temp[0]][2] - 20000
                            print("Telkomsel credit purchases successful")
                            print("Your remaining balance is ",ptri20)
                            print("\nThank Your, Have A Nice Day :)")
                        else : 
                            print("the balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif ptri == 4:
                        if self.class_list[self.temp[0]][2] >= 50000 :
                            ptri50 = self.class_list[self.temp[0]][2] - 50000
                            print("Telkomsel credit purchases successful")
                            print("Your remaining balance is ",ptri50)
                            print("\nThank Your, Have A Nice Day :)")
                        else : 
                            print("the balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif ptri == 5:
                        if self.class_list[self.temp[0]][2] >= 100000 :
                            ptri100 = self.class_list[self.temp[0]][2] - 100000
                            print("Telkomsel credit purchases successful")
                            print("Your remaining balance is ",ptri100)
                            print("\nThank Your, Have A Nice Day :)")
                        else : 
                            print("the balance is not enough!\n")
                            self.menu_pulsa()
                        break
                    elif ptri == 6:
                        self.pulsa()
                        self.menu_pulsa()
                        break
                    else :
                        print("enter the correct input")
                        self.menu_pulsa()
                break
            elif choise_pulsa == 6:
                online_payment()
                self.menu_online_payment()
                self.summon_online_payment()
                break
            else :
                self.menu_pulsa()
                break
            
    def menu_token_listrik(self):
        self.token_listrik()
        int(input("Enter your Token number: "))
        print("Select the credit you want to buy: ")
        print("1. Rp.20,000 \n2. Rp.50,000 \n3. Rp.100,000 \n4. Rp.150,000 \n5. Rp.200,000 \n6. Back")
        token = int(input("Input Your Choice: "))
        while True:
            if token == 1:
                if self.class_list[self.temp[0]][2] >= 20000:
                    tokenlistrik20 = self.class_list[self.temp[0]][2] - 20000
                    print("Your electric token purchases successful")
                    print("Your remaining balance is ", tokenlistrik20)
                    print("\nThank Your, Have A Nice Day :)")
                    break
                else : 
                    print("the balance is not enough!\n")
                    self.menu_token_listrik()
                    break
            elif token == 2:
                if self.class_list[self.temp[0]][2] >= 50000:
                    tokenlistrik50 = self.class_list[self.temp[0]][2] - 50000
                    print("Your electric token purchases successful")
                    print("Your remaining balance is ", tokenlistrik50)
                    print("\nThank Your, Have A Nice Day :)")
                    break
                else : 
                    print("the balance is not enough!\n")
                    self.menu_token_listrik()
                    break
            elif token == 3:
                if self.class_list[self.temp[0]][2] >= 100000:
                    tokenlistrik100 = self.class_list[self.temp[0]][2] - 100000
                    print("Your electric token purchases successful")
                    print("Your remaining balance is ", tokenlistrik100)
                    print("\nThank Your, Have A Nice Day :)")
                    break
                else : 
                    print("the balance is not enough!\n")
                    self.menu_token_listrik()
                    break
            elif token == 4:
                if self.class_list[self.temp[0]][2] >= 150000:
                    tokenlistrik150 = self.class_list[self.temp[0]][2] - 150000
                    print("Your electric token purchases successful")
                    print("Your remaining balance is ", tokenlistrik150)
                    print("\nThank Your, Have A Nice Day :)")
                    break
                else : 
                    print("the balance is not enough!\n")
                    self.menu_token_listrik()
                    break
            elif token == 5:
                if self.class_list[self.temp[0]][2] >= 200000:
                    tokenlistrik200 = self.class_list[self.temp[0]][2] - 200000
                    print("Your electric token purchases successful")
                    print("Your remaining balance is ", tokenlistrik200)
                    print("\nThank Your, Have A Nice Day :)")
                    break
                else : 
                    print("the balance is not enough!\n")
                    self.menu_token_listrik()
                    break
            elif token == 6:
                    online_payment()
                    self.menu_online_payment()
                    self.summon_online_payment()
                    break
            else :
                print("enter the correct input")
                self.menu_token_listrik()
                break
            
        
    
    def summon_online_payment(self):
        self.menu_online_payment()
        choice_online_payment = int(input("Input Your Choice : "))
        while True:
            if choice_online_payment == 1:
                self.menu_pulsa()
                break
            elif choice_online_payment == 2 :
                self.menu_token_listrik()
                break
            elif choice_online_payment == 3 :
                print("Thank Your, Have A Nice Day :)")
                break
            else:
                print("enter the correct input")
                self.summon_online_payment()
                break



class send_money(Account):   
    def __init__(self):
        print("=========================================")
        print("|       Welcome to Send Money           |")
        print("=========================================")
    def menu_send_money(self):
        print("1. Transfers between accounts")
        print("2. Transfers Virtual Account")
        print("3. Exit")
        print("=========================================")
        
        
    def menu_tranfer_rekening(self):
        int(input("Input destination account: "))
        trans = int(input("Input Nominal to be transferred : "))
        while True:
            if self.class_list[self.temp[0]][2] >= trans :
               transfer_rek = self.class_list[self.temp[0]][2] - trans
               print("\nSuccessful! ")
               print("\nYour Balance : ",transfer_rek)
               break
            else :
                print("Your balance is not enough!!")
                break

        
    def menu_virtual_acc(self):
        int(input("Input destination Virtual Account  : "))
        trans = int(input("Input Nominal to be transferred : "))
        while True:
            if self.class_list[self.temp[0]][2] >= trans :
               transfer_rek = self.class_list[self.temp[0]][2] - trans
               print("\nSuccessful! ")
               print("\nYour Balance : ",transfer_rek)
               break
            else :
                print("Your balance is not enough!!")
                break
        
        
        
    def summon_send_money(self):
        choice_send_money = int(input("Input Your Choice : "))
        while True:
            if choice_send_money == 1:
                self.menu_tranfer_rekening()
                choice2 = str(input("ingin melakukan transaksi lagi? Y/N "))
                if choice2 == 'y' or choice2 == 'Y':
                    pass
                else :
                    self.menu_send_money()
                    break
            elif choice_send_money == 2 :
                self.menu_virtual_acc()
                choice3 = str(input("ingin melakukan transaksi lagi? Y/N "))
                if choice3 == 'y' or choice3 == 'Y':
                    pass
                else :
                    self.menu_send_money()
                    break
            elif choice_send_money == 3 :
                print("Thank Your, Have A Nice Day :)")
                break
            else:
                print("enter the correct input")
                self.summon_send_money()
                break

s = online_payment()
while True:
    s.summon()
