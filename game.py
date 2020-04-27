# Write your code here
import random


class Game:

    def __init__(self):
        self.computer_action = ['rock', 'paper', 'scissors']
        self.user_name = ''
        self.rating = 0
        self.new_rating = 0

    def beat_player(self, option: str):
        c_option = random.choice(self.computer_action)
        p_option = option

        if c_option == p_option:
            print(f'There is a draw ({c_option})')
            self.new_rating += 50
        elif p_option == 'rock':
            if c_option == 'paper':
                print(f'Sorry, but computer chose {c_option}')
            else:
                print(f'Well done. Computer chose {c_option} and failed')
                self.new_rating += 50
        elif p_option == 'paper':
            if c_option == 'scissors':
                print(f'Sorry, but computer chose {c_option}')
            else:
                print(f'Well done. Computer chose {c_option} and failed')
                self.new_rating += 50
        elif p_option == 'scissors':
            if c_option == 'rock':
                print(f'Sorry, but computer chose {c_option}')
            else:
                print(f'Well done. Computer chose {c_option} and failed')
                self.new_rating += 50
        else:
            print('Invalid input')

    def player(self):
        user = input("Enter your name: ")
        user_read = user.lower()
        check = False
        with open("rating.txt", "r+") as f:
            datafile = f.readlines()

        for lines in datafile:
            if user_read in lines.lower():
                user_data = lines.splitlines()
                self.user_name = user_data[0].split(' ')[0]
                self.rating = int(user_data[0].split(' ')[1])
                check = True

        if not check:
            self.user_name = user_read
            self.rating = 0

        self.new_rating = self.rating
        print(f'Hello, {user}')

    def player_rating(self):
        print(f'Your rating: {self.new_rating}')

    def update(self):
        user_data = f'{self.user_name} {self.rating}'
        new_data = f'{self.user_name} {self.new_rating}\n'
        with open("rating.txt", "r") as f:
            lines = f.readlines()
        with open("rating.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != user_data:
                    f.write(line)
        with open("rating.txt", "a") as f:
            f.write(new_data)

    def main(self):
        self.player()
        while True:
            option = input()
            if option == '!exit':
                print('Bye!')
                break
            elif option == '!rating':
                self.player_rating()
            else:
                self.beat_player(option)
        self.update()


if __name__ == '__main__':
    Game().main()
