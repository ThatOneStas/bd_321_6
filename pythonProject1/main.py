import json
def myfunc(FirstName,LastName,FathersName):
    FullName = f"{LastName} {FirstName[0]}. {FathersName[0]}."
    print(FullName)

def fib(first_number,second_number,end_number):
    fib_numbers = []
    while second_number <= end_number:
        next_number = first_number + second_number
        first_number = second_number
        second_number = next_number
        if second_number <= end_number:
            fib_numbers.append(next_number)
    print(fib_numbers)

if __name__ == '__main__':

    # FirstName = input('Imia: ').capitalize()
    # LastName = input('Prizvyshche: ').capitalize()
    # FathersName = input('Pobatkovi: ').capitalize()
    # myfunc(FirstName, LastName, FathersName)


    fib(1, 2, 100)

    print('\n')


    with open('users_data.json', 'r') as f:
        users = json.load(f)

    def Adder(n,b):
        users.append({
         "id": len(users)+1,
         "owner_name": n,
         "balance": b
        })
        with open('users_data.json', 'w') as file:
            json.dump(users, file)

    Cond1 = input('Wanna add user? (Y/N): ')
    if Cond1.upper() == "Y":
        n = input('Vvedit imia: ').title()
        b = int(input('Vvedit balans: '))
        Adder(n,b)

    IdRecepient = int(input('Vvedit id otrymuvacha: '))
    IdSender = int(input('Vvedit id dlya znyattya: '))
    MoneyQuant = int(input('Vvedit summu perekazu: '))

    Cond2 = True
    def Calc(IdRecepient,IdSender,MoneyQuant,Cond2,users):
        for item in users:
            if item['id'] == IdSender:
                if item['balance'] >= MoneyQuant:
                    item["balance"] -= MoneyQuant
                    with open('users_data.json', 'w') as file:
                            json.dump(users, file)
                    print(f"{item['owner_name']}, баланс = {item['balance']}")
                else:
                    Cond2 = False
        for item in users:
            if item['id'] == IdRecepient:
                if Cond2 == True:
                    item["balance"] += MoneyQuant
                    with open('users_data.json', 'w') as file:
                        json.dump(users, file)
                    print(f"{item['owner_name']}, баланс = {item['balance']}")
                else:
                    print('Summa zavelyka.')
    if IdRecepient > len(users) or IdSender > len(users):
        print('Nepravylne ID odnogo z korystuvachiv.')
    else:
        Calc(IdRecepient,IdSender,MoneyQuant,Cond2,users)
    # # userNbalance.append({
    #     "owner_name": UserName,
    #     "balance": SBalance
    # })
    # UserName_2 = input('Vvedit vlasnyka: ').title()

    # for user in userNbalance:
    #     if user['owner_name'] == UserName_2:
    #         user['balance'] -= Znyattya