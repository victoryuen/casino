import numbers
def set_up_board():
    num_list = list(range(37))
    #num_list = list(map(str, num_list))
    #num_list.append("00")
    for i in num_list:
        print(i, end=' ')
        if(i%12==0):
            print("\n")
        
    

def place_bet():
    while True:
        user_input = input("Please enter a bet: ")
        try:
            num = int(user_input)
            break
        except ValueError:
            print("Invalid input. Please try again.")


def roulette():
    set_up_board()


def main():
    print("Welcome to the casino!") 
    while True:
        user_input = input("Please enter a balance: ")
        try:
            num = int(user_input)
            break
        except ValueError:
            print("Invalid input. Please try again.")
    balance = num 
    print(balance)
    roulette()
if __name__ == "__main__":
     main()
