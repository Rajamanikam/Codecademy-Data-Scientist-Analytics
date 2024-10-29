# importing CSV, JSON library

import csv
import json

# creating a list of users whose passwords have been compromised

compromised_users = []

## getting compromised users names from csv file and storing in list

with open('passwords.csv') as password_file:
  password_csv = csv.DictReader(password_file)

  for password_row in password_csv:
    # print(password_row['Username'])
    compromised_users.append(password_row['Username'])


## creating a new text file and writing compromised users names into it

with open('compromised_users.txt', 'w') as compromised_user_file:
  for compromised_user in compromised_users:
    compromised_user_file.write(compromised_user + "\n")

## creating a new json file and writing newly created dictionary items into it

with open('boss_message.json', 'w') as boss_message:
  boss_message_dict = {"recipient": "The Boss", "message": "Mission Success"}
  json.dump(boss_message_dict, boss_message)


slash_null_sig = """
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""

## creating a new csv file and writing a multiline string signature into it

with open('new_passwords.csv', 'w') as new_passwords_obj:
  new_passwords_obj.write(slash_null_sig)
