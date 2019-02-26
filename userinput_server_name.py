def string():
    print("Enter server name:")
    server_name=input()
    print("Enter the DB name:")
    db_name=input()
    print("enter username:")
    user_name=input()
    print("enter the password:")
    password=input()
    
    return "Server_Name="+server_name+";DB_Name="+db_name+";Username="+user_name+";Password="+password

print(string())
