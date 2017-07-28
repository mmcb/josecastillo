class CreditCard:
    
    '''
    this is a doc string that lets you 
    write multi-line comments for better
    DOCUMENTATION!!!
    '''

    def __init__(self, card_number):
        self.card_number = card_number
        self.card_type = 'Not Valid'
        self.valid = False

#Create and add your method called `determine_card_type` to the CreditCard class here:
    def determine_card_type(self):
        m = ["51", "52", "53", "54", "55"]
        a = ["34", "37"]
        v = ["4"]
        d = ["6011"]
        if self.card_number[:4] in d: 
            self.card_type = "Discover"
        elif self.card_number[:2] in m:
            self.card_type = "Mastercard"
        elif self.card_number[:2] in a: 
            self.card_type = "AMEX"
        elif self.card_number[0] in v: 
            self.card_type = "Visa"
        else:
            self.card_type = "Not valid"
        return self.card_type

#Create and add your method called `check_length` to the CreditCard class here:
    def check_length(self):
        if self.card_type == "Not valid": # IF check to make sure that if the len(self.card_number) is correct, but type is unknown
            print("Not a valid card type. Discard length")
        elif len(self.card_number) == 16:
            print("It's got to be a VISA or MC or Discovery")
        elif len(self.card_number) == 15:
            print("It's got to be an AMEX")
        else:
            print("Not a credit card")
        return 'not none!'
    
# #Create and add your method called 'validate' to the CreditCard class here:
    def validate(self):
        if self.card_type != "Not valid": # Must add check here to avoid calculatng mod%10 if card not any of above types
            dig = []
            all_dig = []
            num_str_reversed = self.card_number[::-1]
            even = False
            for i in num_str_reversed:
                num = int(i)
                if even == True:
                    num *= 2
                    dig.append(num if num < 10 else 1+num%10)
                    even = False
                else:
                    all_dig.append(num)
                    even = True
            
            check_sum = sum(dig) + sum(all_dig)
            if check_sum % 10 == 0:
                self.valid = True
            else:
                self.valid = False
            return self.valid # Must return something in order for print() in main() to display something.
        else:
            self.valid = False
            print("Unidentifiable Card number") #Display message in the case that the card is not Visa/Mastercard/AMEX/Discover
            # report_fraud()
            return self.valid
    
    def report_fraud(self):
        print("oh shit")

    def main(self):
        print(self.determine_card_type())
        print(self.check_length())
        print(self.validate())
# num = input()

cc = CreditCard('5515460934365316')
# cc2 = CreditCard('5517339408272344')

# cc.determine_card_type()

# cc.check_length()

# cc.validate() # Do not need to run validate() if being invoked in main() method.
cc.main()













# #do not modify assert statements

# cc = CreditCard('9999999999999999')

# assert cc.valid == False, "Credit Card number cannot start with 9"
# assert cc.card_type == "INVALID", "99... card type is INVALID"

# cc = CreditCard('4440')

# assert cc.valid == False, "4440 is too short to be valid"
# assert cc.card_type == "INVALID", "4440 card type is INVALID"

# cc = CreditCard('5515460934365316')

# assert cc.valid == True, "Mastercard is Valid"
# assert cc.card_type == "MASTERCARD", "card_type is MASTERCARD"

# cc = CreditCard('6011053711075799')

# assert cc.valid == True, "Discover Card is Valid"
# assert cc.card_type == "DISCOVER", "card_type is DISCOVER"

# cc = CreditCard('379179199857686')

# assert cc.valid == True, "AMEX is Valid"
# assert cc.card_type == "AMEX", "card_type is AMEX"

# cc = CreditCard('4929896355493470')

# assert cc.valid == True, "Visa Card is Valid"
# assert cc.card_type == "VISA", "card_type is VISA"

# cc = CreditCard('4329876355493470')

# assert cc.valid == False, "This card does not meet mod10"
# assert cc.card_type == "INVALID", "card_type is INVALID"

# cc = CreditCard('339179199857685')

# assert cc.valid == False, "Validates mod10, but invalid starting numbers for AMEX"
# assert cc.card_type == "INVALID", "card_type is INVALID"