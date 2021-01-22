#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 15:09:52 2021

@author: abhay
"""
import datetime as dt
import time
    
user_data = []
restaurant_data = []
foodItem_data = []
order_data = []

class Users:
  def __init__(self, username, email, password, address):
    self.username = username
    self.email = email
    self.password = password
    self.address = address
    self.order  = []
  
  def update(self, usrn, mail, pswrd, add):
    self.username = usrn
    self.email = mail
    self.password = pswrd
    self.address = add
    print("Updated")
      
  def loginCheck(self, usrname, pswrd):
    if (usrname==self.username and pswrd == self.password ):
        return "Y"
    else :
        return "N"
    
                
class FoodItem:
    def __init__(self, productName, productPrice, productId):
        self.productName = productName
        self.productPrice = productPrice
        self.productId = productId 
            

class Restaurants:
    def __init__(self, name, password, food_menu, processing_order_count):
        self.name = name
        self.password = password
        self.food_menu = food_menu
        self.processing_order_count = processing_order_count
        self.orders = []

    def getName(self):
        return self.name
       
    def loginCheck(self, usrname, pswrd):
        if (usrname==self.name and pswrd == self.password ):
            return "Y"
        else :
            return "N"
        
    def check_order_accepting(self):
        count = 0
        for order in self.orders:
            if order.delivery_time > (dt.datetime.now()) :
                count  = count + 1
        if count >= self.processing_order_count :
            return "N"
        else :
            return "Y"
        
        
class Order:
    def __init__(self, status, foodItem):
        self.status = status
        self.foodItem  = foodItem
        self.time = dt.datetime.now()
        self.delivery_time = dt.datetime.now() + dt.timedelta(minutes=30)
        
    def update_status(self):
        self.status = "Delivered"
        
restro1 = Restaurants("restro1", "abhay", [], 10)
user = Users("user1","abhay@gmail.com", "abhay", "232")
foodItem1 = FoodItem("Pizza","200", 0)
foodItem2 = FoodItem("Dhosa", "80", 1)
order1 = Order("Initiated", [foodItem1])

user.order.append(order1)
restro1.orders.append(order1)
restro1.food_menu.extend([foodItem1, foodItem2] )
user_data.append(user)
restaurant_data.append(restro1)

        
def UserLoginOrSingupPage():
    print("#"*50)
    print("User Login/Signup Page")
    print("#"*50)
    print("Press 1 :for User SigIn")
    print("Press 2 :for User Signup")
    print("Press E :for Exit")
    x = input("Press any Button: ")
    if x == "1":
        UserSignInPage()
    elif x=="2":
        UserSignUpPage()
    elif(x=='E'):
        MainMenu()
    else :
        UserLoginOrSingupPage()

def UserSignInPage():
    found = False
    username = input("Username: ")
    password = input("Password: ")
    for data in user_data:
        if (data.loginCheck(username, password)=='Y'):
            found = True
            user = data
            break
    if(found==True):
        AvailableFunctionalityUsers(user)
    else:
        print("Invalid username/password! Try Again")
        UserSignInPage()

def UserSignUpPage():
     print("#"*50)
     print(" User Signup Page")
     print("#"*50)
     username = input("Username: ")
     email = input("Email: ")
     password = input("Password: ")
     re_password = input("Password: ")
     address = input("Address: ")
     if (password!=re_password):
         print("Password donot match")
         print("Y for Yes or N for No")
         x = input("Do u want to try again?")
         if (x=="Y"):  
             UserSignUpPage()
         else:
             UserLoginOrSingupPage()
     else:
         u = Users(username, email, password, address)
         user_data.append(u)
         AvailableFunctionalityUsers(u)
     
def AvailableRestaurants(user):
    print("#"*50)
    print("List of Available restaurant")
    print("#"*50)
    for i in range(0, len(restaurant_data)):
        print("Press", i, ": to select", restaurant_data[i].name)
    print("E for exit")
    x = input("Press any key: ")
    if x=="E":
        AvailableFunctionalityUsers(user) 
    elif int(x) <  len(restaurant_data) and restaurant_data[int(x)]:
        RestroItemPage(restaurant_data[int(x)], user)
    else :
        AvailableRestaurants(user)
    
    
def RestroItemPage(restro, user):
    print("#"*50)
    print("Select Item from", restro.name)
    print("#"*50)
    print("E to Exit \nC to Continue")
    inpt = input("Press Any Key: ")
    if inpt == "E":
       AvailableFunctionalityUsers(user)
    for i in range(0, len(restro.food_menu)):
        print("Press", i, ":for", restro.food_menu[i].productName, "Price:", restro.food_menu[i].productPrice )
    items = []
    if restro.check_order_accepting() == "Y" :
        for i in range(20):
            x = input("Select any Item: ")
            y = input("Add quantity: ")
            print("A : to add more item")
            print("E : Exit")
            print("P : Place order")
            z = input("Press Any Key: ")
            if z == "A":
                items.extend([restro.food_menu[int(x)]]*int(y))
            elif z == "P":
                items.extend([restro.food_menu[int(x)]]*int(y))
                new_order  = Order("Initiated", items)
                print("Order Placed")
                print("order itme", items)
                user.order.append(new_order)
                restro.orders.append(new_order)
                AvailableFunctionalityUsers(user)
            elif z=='E':
                AvailableRestaurants(user)
            else :
                RestroItemPage(restro, user)
    else :
        print("Not Accepting any orders right now")
        inpt = input ("Press E to exit: ")
        if inpt == "E":
            AvailableFunctionalityUsers(user)
        else :
            RestroItemPage(restro, user)
    
def GetUserProfile(user):
    print("#"*50)
    print("User Profile Details")
    print("#"*50)   
    #username, email, password, address
    print("username :", user.username)
    print("email :", user.email)
    print("address :", user.address)
    x  = input("Press E to exit :")
    if x == "E":
        AvailableFunctionalityUsers(user)
    else :
        GetUserProfile(user)
        
# remaining
def EditUserDetail(user):
    print("#"*50)
    print("U can update username, email, password, address")
    print("to update any field ")
    print("#"*50)
    change = ["username", "email", "password", "address"]
    for i in range(len(change)):
        print("Press", i,": to change", change[i] )
    print("E to exit")
    payload = {
            "username":user.username,
            "password":user.password,
            "email":user.email,
            "address":user.address
    }
    x  = input("Press any Key :")
    if x=="E":
        AvailableFunctionalityUsers(user)
    elif x in [str(i) for i in range(0, len(change))]:
        payload[change[int(x)]] = input("Enter New Value: ")
        user.update(payload["username"], payload["password"], payload["email"], payload["address"])
        EditUserDetail(user)
    else :
        EditUserDetail(user)
        
def DeleteUserProfile(user):
    print("#"*50)
    print("Delete Profile Page")
    print("#"*50)
    print("Y for Yes\n N for NO")
    x = input("Do u want to delete ur Profile")
    if (x=="Y"):
        user_data.remove(user)
        del user
        UserSignUpPage()
    else :
        print("Do u want to exit? \nPress E for exit\1 to retry")
        x = input("Press :")
        if x == "1":
            DeleteUserProfile(user)
        elif x == "E":
            AvailableFunctionalityUsers()
        else :
            DeleteUserProfile(user)

def ViewUserOrderDetails(user):
    print("#"*50)
    print("Order Details")
    print("#"*50)
    for i in range(len(user.order)):
        if user.order[i].delivery_time < dt.datetime.now() :
            user.order[i].update_status()
        print("#"*20)
        print("Order:",i, ",Status:", user.order[i].status)
        for itm in user.order[i].foodItem:
            print( "Item Name: ", itm.productName, ",Price :", itm.productPrice)
        print("#"*20)
    print("E : to exit")
    x = input("Press any Key : ")
    if x=="E":
        AvailableFunctionalityUsers(user)
    else:
        ViewUserOrderDetails(user)
        
    
def Logout(user):
    UserSignUpPage()

def SearchRestaurant(user):
    print("#"*50)
    print("Search Restaurants")
    print("#"*50)
    found = False
    res = ""
    srch = input("Search :")
    for data in restaurant_data:
       if data.name.lower().find(srch.lower()) >= 0:
           found = True
           res = data
           break
    if found :
        print(" Match Found!! ")
        RestroItemPage(res, user)    
    else:
        print("Cannot find Anything matching these \n1 to retry \nE to Exit")
        x = input("Press: ")
        if x=='1': 
            SearchRestaurant(user)
        elif(x=='E'):
            AvailableFunctionalityUsers(user)
    
def AvailableFunctionalityUsers(user):
    print("#"*50)
    print("Here are the list of functionality you can try")
    print("#"*50)
    print("press 1 : To See all Available Restuarants" )
    print("press 2 : To Edit User Details" )
    print("press 3 : To See all Orders" )
    print("press 4 : To get Ur Profile") 
    print("press 5 : To delete Ur Profile")
    print("press 6 : Logout")
    print("press 7 : Search Restaurant")
    print("press E : To exit")
    x = input("Press Any Button: ")
    switcher  = {
         "1": AvailableRestaurants,
         "2": EditUserDetail,
         "3": ViewUserOrderDetails,
         "4": GetUserProfile,
         "5": DeleteUserProfile,
         "6": Logout,
         "7": SearchRestaurant,
    }
    switcher[x](user)


###############################################################################
# Restaurants Functionality
###############################################################################
        
def RestaurantsLoginOrSingupPage(): 
    print("Press 1 for Restaurants SigIn")
    print("Press 2 for Restaurants Signup")
    print("Press E for Exit")
    x = input("Press any Button: ")
    if x == "1":
        RestaurantSignInPage()
    elif x=="2":
        RestaurantSignUpPage()
    elif(x=='E'):
        MainMenu()
    else :
        RestaurantsLoginOrSingupPage()
        
def RestaurantSignInPage():
    found = False
    name = input("name: ")
    password = input("Password: ")
    restro = ""
    for data in restaurant_data:
        if (data.loginCheck(name, password)=='Y'):
            found = True
            restro = data
            break
    if(found==True):
        AvailableFunctionalityRestaurants(data)
    else:
        print("Invalid username/password! Try Again")
        RestaurantSignInPage()

def RestaurantSignUpPage():
    print("#"*50)
    print("Signup Restaurants")
    print("#"*50)  
    username = input("Username: ")
    password = input("Password: ")
    re_password = input("Password: ")
    processing_order_count = input("Max processing Order Count: ")
    if (password!=re_password):
         print("Password donot match")
         print("Y for Yes or N for No")
         x = input("Do u want to try again?")
         if (x=="Y"):  
             RestaurantSignUpPage()
         else:
             RestaurantsLoginOrSingupPage()
    else:
         u =  Restaurants(username, password, [], processing_order_count)
         restaurant_data.append(u)
         AvailableFunctionalityRestaurants(u)

def AvailableFunctionalityRestaurants(res):
     print("#"*50)
     print("Here are the list of functionality you can try")
     print("#"*50)
           
     print("Press 1: Add Menu")
     print("Press 2: Update menu")
     print("press E : Logout")
     
     inpt = input("Press Any Key: ")
     if inpt == "1":
         AddMenuItem(res)
     elif(inpt == '2'):
         UpdateMenuItem(res)
     elif(inpt == "E"):
         RestaurantsLoginOrSingupPage()
     else :
         AvailableFunctionalityRestaurants(res)

def AddMenuItem(res):
    print("#"*50)
    print("Add Menu")
    print("#"*50)
           
    pName = input("Item Name : ")
    pPrice = input("Item Price: ")
    pId = len(res.food_menu)
    item = FoodItem(pName, pPrice, pId)
    res.food_menu.append(item)
    print("Press 1: Add More")
    print("Press E: Exit")
    inpt = input("Press Any Key: ")
    if inpt == "1":
        AddMenuItem(res)
    elif(inpt == 'E'):
         AvailableFunctionalityRestaurants(res)

def UpdateMenuItem(res):
    print("#"*50)
    print("Update Menu")
    print("#"*50)  
    for data in res.food_menu:
        print("press ", data.productId, " to edit", data.productName )
    print("E: to exit")
    x = input("Press Key: ")
    if x=="E":
        AvailableFunctionalityRestaurants(res)
    for data in res.food_menu:
        if data.productId == x:
            print("Press 1 to edit : Product Name \nPress 2 to edit Product Price")
            print("E to Exit")
            y = input("Press key: ")
            if y=="1":
                newName = input("enter new Name: ")
                data.productName = newName
                print("Successful!")
            elif y == '2':
                newPrice = input("enter new Price: ")
                data.productPrice = newPrice
            elif y=="E":
                AvailableFunctionalityRestaurants(res)
            else :
                UpdateMenuItem(res)
    print("E to exit \nAny other key to retry")
    z = input("Press Key: ")
    if z == "E":
       AvailableFunctionalityRestaurants(res)
    else :
        UpdateMenuItem(res)
        
        
def MainMenu():
    print("#"*50)
    print("Welcome to OMS")
    print("#"*50)
          
    print("Press 1 for User SigIn/Signup \nPress 2 for Restaurants SignIn/SignUp")
    x = input("Press any button: ")
    if x=="1":
        UserLoginOrSingupPage()
    elif (x=="2"):
        RestaurantsLoginOrSingupPage()
    else :
        MainMenu()
        
if __name__ == '__main__':
    MainMenu()




###############################################################
#                  Unit Test
###############################################################

        
    

       
            

    
     
     
     
