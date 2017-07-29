#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 10:39:28 2017

@author: Jose Castillo
"""

# Project Number 1
class CreditCard(object):
    
    def __init__(self, card_number):
        self.card_number = card_number
        self.card_type = self.card_type
        self.valid = self.valid
        
    def check_length(self):
        card_length = len(self.card_number)
        
        
        
        if card_length == 16:
            print(self.card_type)
            
            
        elif card_length == 15:
            print(self.card_type)
            
        else:
            self.card_type = "Please try again"
        
    
        
    
        
    def determine_card_type(self):
        visa_card = ["4"]
        
        master_card = ["51","52","53","54","55"]
        
        amex_card = ["34","37"]
        
        discovery_card = ["6011"]
        
        if self.card_number[:5] == master_card:
            self.card_type = "Master Card"
        elif self.card_number[:2] == amex_card:
            self.card_type = "American Express Card"
        elif self.carda_type[:1] == discovery_card:
            self.card_type = "Discovery Card"
        elif self.card_type[:1] == visa_card:
            self.card_type = "Visa Card"
        else:
            self.card_number = "Not a valid card"
        
        return self.card_type
            
   
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
        print("This card is suspicious!")

    def main(self):
        print(self.determine_card_type())
        print(self.check_length())
        print(self.validate())
# num = input()

cc = CreditCard('5515460934365316')    
            
            
            


        
        
