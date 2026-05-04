# 4. User Profile With Properties
#
# Create a UserProfile class.
#
# Practice:
#
# public attributes where appropriate
# private-style attribute _email
# property getter and setter for email
# validate email contains "@"
# static method: check strong password
# class method: create user from signup form dictionary
#
# Challenge: avoid generic get_email() and set_email() unless necessary.
import uuid


class UserProfile:
    def __init__(self, email, name, password):
        self.__email = email
        self.name = name
        self.password = password


    @property
    def get_email(self):
        return self.__email
    @property
    def set_email(self):
        return self.__email
    def validate_email(self):
        if "@" not in self.__email:
            return "This email is not valid"
    @staticmethod
    def validate_password(password):
        if password == "":
            return "This password is empty"
        elif len(password) < 8:
            return "This password is too short"
        elif len(password) > 16:
            return "This password is too long"
        else:
            return "This password is strong"

    def user_login(self):
        userProfile = {
            "name": self.name,
            "email": self.__email,
            "password": self.password
        }
        for key, value in userProfile.items():
            print(f"the name of the user ")





# user1 = UserProfile("Ousmane@speakhire.org", "Ousmane", "Talha826$")
# print(user1.validate_email)
# print(user1.validate_password)
# print(user1.get_email)
# print(user1.user_login())
# user2 = UserProfile("ousmanediallo", "Ousmane", "Talha826$")
# print(user2.validate_email)
# print(user2.validate_password)
# print(user2.get_email)
# print(user2.user_login())



# 1. Bank Account System
#
# Create a BankAccount class.
#
# Practice:
#
# class attribute: bank_name
# instance attributes: owner, balance
# property: balance
# prevent negative balance
# static method: validate account number
# class method: create account with bonus
#
# Challenge: users should not directly set balance to a negative number.

#
from dataclasses import dataclass
from dataclasses import dataclass

@dataclass
class BankAccount:
    owner: str
    balance: int = 0

    def deposit(self, amount):
        if amount <= 0 or not isinstance(amount, int):
            print("Invalid deposit amount")
            return
        self.balance += amount
        print(f"Deposited: ${amount}")

    def withdraw(self, amount):
        if amount <= 0 or not isinstance(amount, int):
            print("Invalid withdrawal amount")
            return
        if amount > self.balance:
            print("Insufficient funds")
            return
        self.balance -= amount
        print(f"Withdrew: ${amount}")

    def show_balance(self):
        print(f"{self.owner} your current balance is: ${self.balance}")


# --- MAIN PROGRAM ---
customerName = input("Enter your customer name: ")
account = BankAccount(customerName)

while True:
    choice = input("Do you want to deposit, withdraw, or exit? ").lower()

    if choice == "deposit":
        amount = int(input("Enter amount to deposit: $"))
        account.deposit(amount)
        account.show_balance()

    elif choice == "withdraw":
        amount = int(input("Enter amount to withdraw: $"))
        account.withdraw(amount)
        account.show_balance()

    elif choice == "exit":
        print("Goodbye!")
        break

    else:
        print("Invalid input")



# 2. Hospital Appointment System
#
# Create classes:
#
# Patient
# Doctor
# Appointment
#
# Practice:
#
# class attribute: hospital name
# property: appointment status
# static method: validate phone number
# class method: create appointment from form data
# immutable appointment ID
#
# Challenge: appointment status can only change through methods like cancel() or complete().
from uuid import UUID
from datetime import datetime
@dataclass
class Patient:
    full_name: str
    dob: str
    phone_number: int
    appointment_history: list

    def store_patient_info(self):
        patient_info = {
            "full_name": self.full_name,
            "dob": self.dob,
            "phone_number": self.phone_number,
            "appointment_history": self.appointment_history
        }
        return patient_info
    def schedule_appointment(self, date: datetime):
        appointment = Appointment.create_appointment({
            "date": date,
            "id": uuid.uuid4(),
            "name": self.full_name,
            "phone_number": self.phone_number,
            "dob": self.dob,

        })
        self.appointment_history.append(appointment)



@dataclass
class Doctor:
    full_name: str
    specialization: str
    available = bool
    appointment_list: list


    def accept_appointment(self):
        if not self.available:
            return "Doctor is not available at this time"
        Appointment.booked(self)
        self.available = False
        return f"{self.full_name} accepted the appointment"

    def view_appointment(self):
        for appointment in self.appointment_list:
            print(f"Appointment: {appointment}")
    def marked_appointment(self):
        result = Appointment.complete()
        self.available = True
        return result
@dataclass
class Appointment:
    patient: Patient
    doctor: Doctor
    patient_id: str = uuid.uuid4()

    @classmethod
    def schedule_appointment(cls):
        if not Doctor.available:
            return "Doctor is not available at this time"


