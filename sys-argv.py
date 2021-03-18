# https://youtu.be/jhki0o54_xY

import sys
#print( sys.argv ) 

### Example 1
# if len(sys.argv) > 1: # checar se foi colocado algum argumento
#     for arg in sys.argv[:1]: #a partir do index 1 
#         print(arg)
# else:
#     print('No arguments provided.')

### Example 2
# if len(sys.argv) > 1:
#     total = sum(int(arg) for arg in sys.argv[1:] if arg.isdigit())
#     print(f"Total is: {total}")

# else:
#      print('No arguments provided.')
### https://youtu.be/_pOOPKu_x78

#usr_str = input("Enter a string: ")
#usr_action=input("Enter a action for your string, (it could be lower/upper/title): ")

if len(sys.argv) != 3:
    print("Something is wrong!")
    print(f"{sys.argv[0]} <your string> <lower/upper/title>")
    sys.exit()

usr_str = sys.argv[1]
usr_action =sys.argv[2]

if usr_action =="lower":
    print(usr_str.lower())
elif usr_action=="upper":
    print(usr_str.upper())
elif usr_action == "title":
    print(usr_str.title())
else:
    print("Your option is invalid, please select one of these options: upper/lower/title. \nThanks")