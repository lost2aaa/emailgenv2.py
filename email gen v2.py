import random
import string
import datetime
x = datetime.datetime.date()
email_length = 10
format = '@fbi.ac'
password_length = 30
def email_gen(length):
        email = string.ascii_letters + string.digits #using the string module to create our email
        mail_gen = ''.join(random.choice(email) for _ in range(length)) #using .join we are putting items into this string 
        return mail_gen

def password_gen(length):
    password = string.ascii_letters + string.digits + string.hexdigits + '-'
    password_generator = ''.join(random.choice(password) for _ in range (length)) #same as before
    return password_generator 


while True:
  amount = int(input("amount to generate:> "))
  
  print("writing entry...")
  with open("data.txt", "w") as entry:
    for _ in range(amount):
      genned_email = email_gen(email_length)
      genned_pw    = password_gen(password_length)
      # write data to entry
      entry.write(f"Email: {genned_email + format}; Pass: {genned_pw}\n {(x.strftime('%a'))}")
  print("done")