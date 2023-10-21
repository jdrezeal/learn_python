print('This is test page')

def id_reg():
    print("Creating user id ......")
    id_name=input("Please enter user name: ")
    id_pass=input("Please enter password: ")

    my_id={'name'    :id_name,
           'pass_id' :id_pass
           }
    print("Register successful !")
    return my_id

def login_id(my_id):
    count = 0

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
num_ppl=0
while True:

    if num_ppl == 5 :
        print("Database is FULL!!")
        break
    else:
        id_dict = id_reg()
        num_ppl +=1
        print(f"user number: {num_ppl}")

    login_id(id_dict)
