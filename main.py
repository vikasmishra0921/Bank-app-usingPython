import json
import random
import string
from pathlib import Path



class Bank:
    database = 'data.json'
    data = []

    try:
      if Path(database).exists():
        with open(database) as fs:
          data = json.loads(fs.read())
      else:
        print("No such file exist")
    except Exception as err:
      print(f"An error occured as {err}")

    @classmethod
    def __update(cls):
      with open(cls.database,"w") as fs:
        fs.write(json.dumps(Bank.data))


    @classmethod
    def __accountNGenrator(cls):
      alpha = random.choices(string.ascii_letters, k = 3)
      num = random.choices(string.digits, k =3)
      id = alpha + num
      random.shuffle(id)
      return "".join(id)

    def createaccount(self):
      info = {
        "name": input("Enter Your Name : "),
        "age": int(input("What is your age ? : ")),
        "email": input("Enter your email. : "),
        "pin": input("Set your pin. : "),
        "account no.": Bank.__accountNGenrator(),
        "Balance": 0
      }

      if info["age"]< 18 :
        CAA = 18 - info["age"]  
        print(f"You can create account after {CAA} years.")
        return
          
          
      elif len(info["pin"]) < 4:
        print("Pin can't be less than 4 number")
      elif len(info["pin"]) >  4:
        print("Pin can't be more than 4 number")
      elif not info["pin"].isdigit():
         print("Pin must contain only numbers")
      else:
        info["pin"] = int(info["pin"]) 
        print("Pin set successfully!")

        for i in info :
          print(f"{i}: {info[i]}")
        print("Please note down your account number.")

        Bank.data.append(info)
        Bank.__update()

    def depositMoney(self):
      accountNumber = input("Please Enter your account number... : ")
      pin = int(input("Please Enter your pin : "))

      userData = [i for i in Bank.data if i['account no.'] == accountNumber and i["pin"] == pin]

      if userData == False:
        print("Sorry, no Data Found")
      
      else:
        amount = float(input("Enter Amount you want to deposit : "))
        if amount > 10000 :
          print("You can't deposit more than 10000 at once, Please visit nearest Branch.")
        elif amount < 0:
          print("You have to deposit minimum 1 rupees.")
        else:
          userData[0]["Balance"] += amount
          Bank.__update()

          print(f"{amount} rupees has been deposited successfully")

    def withdrawMoney(self):
      accountNumber = input("Please Enter your account number... : ")
      pin = int(input("Please Enter your pin : "))

      userData = [i for i in Bank.data if i['account no.'] == accountNumber and i["pin"] == pin]

      if userData == False:
        print("Sorry, no Data Found")
      
      else:
        amount = float(input("Enter Amount you want to withdraw : "))
        if amount > userData[0]["Balance"] :
          print("Insufficient Balance...")
        else:
          if amount > 10000 :
            print("You can't withdraw more than 10000 at once, Please visit nearest Branch.")
          elif amount < 0:
            print("You have to withdraw minimum 100 rupees.")
          else:
            userData[0]["Balance"] -= amount
            Bank.__update()

            print(f"{amount} rupees has been withdrawed successfully")
            print(f"Remaining Balance is {userData[0]['Balance']}")
          
    def showDetails(self):
      accountNumber = input("Please Enter your account number... : ")
      pin = int(input("Please Enter your pin : "))

      userData = [i for i in Bank.data if i['account no.'] == accountNumber and i["pin"] == pin]

      print("Your Information is : \n")

      for i in userData[0]:
        print(f"{i}:{userData[0][i]}")
    
    def updateDetails(self):
      accountNumber = input("Please Enter your account number... : ")
      pin = int(input("Please Enter your pin : "))

      userData = [i for i in Bank.data if i['account no.'] == accountNumber and i["pin"] == pin]

      if not userData:
        print("No User found")

      else:
        print("You can not change age and account number.")

        print("Fill the details for change or leave it empty if no change and press Enter to save the details")

        newData = {
          "name" : input("Please Enter Name or press enter to skip : "),
          "email": input("Please Enter new email or press enter to skip : "),
          "pin": input("Please enter new pin or press enter to skip : ")
        }


        if newData["name"] == "":
          newData["name"] = userData[0]["name"]
        if newData["email"] == "":
          newData["email"] = userData[0]["email"]
        if newData["pin"] == "":
          newData["pin"] = userData[0]["pin"]
        
        newData["age"] = userData[0]["age"]
        newData["account no."] = userData[0]["account no."]
        newData["Balance"] = userData[0]["Balance"]

        if type(newData['pin']) == str:
          newData['pin'] = int(newData['pin'])



        for i in newData:
          if newData[i] == userData[0][i]:
            continue
          else:
            userData[0][i] = newData[i]

        Bank.__update()
        print("Details Updated successfully.")

    def DeleteDetails(self):
      accountNumber = input("Please Enter your account number... : ")
      pin = int(input("Please Enter your pin : "))

      userData = [i for i in Bank.data if i['account no.'] == accountNumber and i["pin"] == pin]

      if not userData:
        print("User not found")
      else:
        check = input("Press y for confirmation and n for cancelling the deletion : ")
        if check == 'n' or check == 'N':
          print("Cancelled")
        else:
          index = Bank.data.index(userData[0])
          Bank.data.pop(index)

          print("Account deleted successfully.")
          Bank.__update()

user = Bank()
print("Press 1 for creating an account")
print("Press 2 for depositing the money in the account")
print("Press 3 for withdrawing the money from the account")  
print("Press 4 for details")
print("Press 5 for Updating the details")
print("Press 6 for deleting your account")

check = int(input("Enter your response : "))

if check == 1:
  user.createaccount()
if check == 2:
  user.depositMoney()
if check == 3:
  user.withdrawMoney()
if check == 4:
  user.showDetails()
if check == 5:
  user.updateDetails()
if check == 6:
  user.DeleteDetails()