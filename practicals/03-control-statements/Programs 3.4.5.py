if __name__ == '__main__':

    while True:
        password = input('Please enter a password(8-12 characters long): ')
        repeat = input('Please re enter your password: ')
        if password in ['password', 'letmein', 'sesame', 'hello', 'justinbieber']:
            print('Please choose a unique password')
        else:
            if 7 <len(password) < 13 and password == repeat:
                print('Password Set')
                break
            if password != repeat:
                print('Error password did not match')
            else:
                print('Error incorrect length')