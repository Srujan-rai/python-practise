secret_word="india"
guess=""
i=3
while guess!=secret_word and i!=0:
    guess = input("enter the guess ")
    i=i-1
if i==0:
    print("you lost")
else:
    print("you guessed right")