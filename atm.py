print("HELLO...NAMASKAR")
print("welcome to SBI ATM")
card=input("insert the card::")
if card=="credit card" or "debit card" or "prepaid card":
    print("don't remove the card")
    lan=input(" select the language::")
    if lan=="english" or "hindi":
        pin=input("enter any four digit number::")
        if num>=1000 and num<=9999:
            varx=int(input("select the options::"))
            if varx==1 or varx== 2 or varx== 3:
                if var==1:
                    print("with drawer")
                elif var==2:
                    print("mini statement")
                elif var==3:
                    print("transfer")
                else:
                    print("none")
                    vary=int("enter the type of account::")
                    if vary=="saving account" or "current account":
                        amount=int(input("enter any amount::"))
                        if amount>=200 and amount<=10000:
                            print("your transaction is being processed")
                            print("collect your cash")
                            print("remove your card")
                            print("thank you visit again")
                        else:
                            print("transaction was failed")
                    else:
                        print("nothing")
            else:
                print("nothing")
        else:
            print("enter valid amount")
    else:
        print("nothing")
else:
    print("try again")
