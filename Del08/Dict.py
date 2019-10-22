import pickle

database = pickle.load(open('userData/database.p','rb'))
userName = raw_input('Please enter your name: ')

if userName in database:
    thing = database[userName][0]
    thing['logins'] += 1
    database[userName] = [thing]
    print('Welcome back ' + userName + '.')
else:
    login = {'logins' : 1}
    database[userName] = [login]
    print('Welcome ' + userName + '.')

print(database)

pickle.dump(database,open('userData/database.p','wb'))
