#1
def fillable(stock, str, num):
    try:
        return stock[str] >= num
    except:
        return False
    
#2
def user_contacts(data):
    users = {}
    
    for user in data:
        for u in user:
            if len(user) != 2:
                users[user[0]] = None
            else:
                users[user[0]] = user[1]
        
    return(users)

