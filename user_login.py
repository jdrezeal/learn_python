print('This is test page')


my_id={'name'    :'jdsam',
       'pass_id' :'abc123'
       }
count = 0
#print(my_id)
#print(my_id['name'],my_id['pass_id'])

while True:
    username=input("Please enter username: ")
    password = input("Please enter password: ")
    if username == my_id['name'] and password == my_id['pass_id']:
        print(f"Welcome, {username} ^ ^")
        break
    elif count==2:
        print(f"Exceed number of tried, please contact support!!")
        break
    else:
        count +=1
        print(f"Wrong username or password, please try again!")

