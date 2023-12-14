#NETWORK PROVIDER CHECKER
MTN=["0","6","7","8"]
GLO=["5","7"]
AIRTEL=["2","1","4"]
ETISALAT=["0","1"]
print("="*50)
print("$"*5,"WELCOME TO MY NETWORK PROVIDER CHECKER","$"*5)
print("="*50)
while True:
    phone_no=str(input("enter your phone number"))
    if len(phone_no)>11 or len(phone_no)<11:
        print("No network provider information available🙄🙄!")
    elif phone_no[3] in MTN:
        print("this number is MTN")
    elif phone_no[3] in GLO:
        print("this number is GLO") 
    elif phone_no[3] in AIRTEL:
        print("this number is AIRTEL")
    elif phone_no[3] in ETISALAT:
        print("this number is ETISALAT")  
    else:
        print("invalid number try again later thank you🤩🤩!")  