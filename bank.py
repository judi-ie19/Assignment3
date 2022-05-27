class Bank:

  def __init__(self,accountname,accountnumber,bankname,accountbalance):
    self.accountname=accountname
    self.accountnumber=accountnumber
    self.bankname=bankname
    self.accountbalance=accountbalance


  def deposit(self):
      amount=int(input("Enter amount")) 
      amount+= self.accountbalance
      return amount
  def withdraw(self):
      amount=int(input("Enter amount")) 
      self.accountbalance-=amount
      return self.accountbalance
       
       
 

    


