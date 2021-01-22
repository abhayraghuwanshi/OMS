#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 21:54:59 2021

@author: abhay
"""
import unittest
import time
import datetime as dt
from oms import Users, Restaurants, FoodItem, Order
        
        
class UserTests(unittest.TestCase):
    def user_login_check(self):    
        user1 = Users("test1", "test1@gamail.com", "test1", "232 RKB")
        user2 = Users("test2", "test2@gamail.com", "test2", "2324RKB")
        self.assertEqual(user1.loginCheck("test1", "test1"), "Y")
        self.assertEqual(user1.loginCheck("test2", "test2"), "N")
    
    def user_update_check(self):
        user1 = Users("test2", "test2@gamail.com", "test2", "2324RKB")
        user1.update("test1", "test2@gmail.com", "test2", "234RKB")
        self.assertEqual(user1.username, "test1")
        self.assertEqual(user1.address, "234RKB")
              
        
class RestaurantTestCase(unittest.TestCase):
    def login_check(self):
        restro1 = Restaurants("restro1", "abhay", [], 10)
        self.assertEqual(restro1.loginCheck("test1", "test1"), "Y")
        self.assertEqual(restro1.loginCheck("restro1", "test2"), "N")
        
    def test_check_order_accepting(self):
        foodItem1 = FoodItem("Pizza","200", 0)
        order1 = Order("Initiated", [foodItem1])
        restro1 = Restaurants("restro1", "abhay", [], 10)
        restro1.orders.append(order1)
        self.assertEqual(restro1.check_order_accepting(), "Y")
        
        restro2 = Restaurants("restro2", "abhay", [], 1)
        order2 = Order("Initiated", [foodItem1])
        restro2.orders.append(order2)
        self.assertEqual(restro2.check_order_accepting(), "N")

if __name__ == '__main__':
    unittest.main()
