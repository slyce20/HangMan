class HangMan:
    hangman = list(open('temps/default.txt', encoding="utf8"))
    word = 'XGBoost'
    word_temp = list(['❓ ' * len(word)][0][:-1])
    attempts = 3
    picked_words = []

    def show_temp(self):
        print(*[i for i in self.hangman])

    def start_game(self):
        print('WELLCOME TO THE GAME!')
        print('RULES ARE SIMPLE!')
        print('   *GUESS HIDDEN WORD AND SAVE THE HANGMAN!')
        print('   *DO NOT FORGET, YOU ONLY HAVE 3 CHANCES!')
        print('   *HAVE FUN!')
        print('HERE IS THE OUR HANGMAN:')
        self.show_temp()
        print('LET\'S START!')
        print('MAKE YOUR FIRST GUESS!')

    def make_choose(self, choose):
        if self.game_over():
            if '❓' in self.word_temp:
                print("GAME OVER\nYOU LOST!")
            else:
                print("GAME OVER\nYOU WON!")
        else:
            if (choose.lower() in self.picked_words) and (choose.lower() in self.word.lower()):
                print(f"You already find letter '{choose}', try another one!")
            elif (choose.lower() in self.picked_words) and (choose.lower() not in self.word.lower()):
                self.attempts -= 1
                if self.game_over():
                    print('OH NO! YOU ARE OUT OF ATTEMPTS!, AND THIS MEAN...')
                    self.update_temp()
                    self.show_temp()
                    print("GAME OVER\nYOU LOST!")
                else:
                    print(f"You once said letter '{choose}' and this is wrong!")
                    print(f'Number to guess: {self.attempts}')
                    self.update_temp()
                    self.show_temp()
            else:
                if choose.lower() in self.word.lower():
                    self.picked_words.append(choose.lower())
                    for i in range(len(self.word)):
                        if self.word[i].lower() == choose.lower():
                            self.word_temp[i * 2] = choose.upper()
                    print(f"Congrats! Letter '{choose}' is in \n{''.join(self.word_temp)}")
                    print(f'Number to guess: {self.attempts}')
                    self.show_temp()
                    if self.game_over():
                        print("GAME OVER\nYOU WON!")

                else:
                    self.picked_words.append(choose.lower())
                    self.attempts -= 1
                    print(f"Letter '{choose}' is not in \n{''.join(self.word_temp)}")
                    if self.game_over():
                        self.update_temp()
                        print('OH NO! YOU ARE OUT OF ATTEMPTS!, AND THIS MEAN...')
                        self.show_temp()
                        print("GAME OVER\nYOU LOST!")
                    else:
                        print(f'Number to guess: {self.attempts}')
                        self.update_temp()
                        self.show_temp()

    def get_attempts(self):
        print(f'{self.attempts} attempt(s) left')

    def create_seat(self):
        self.hangman = list(open('temps/temp1.txt', encoding="utf8"))

    def create_gallows(self):
        self.hangman = list(open('temps/temp2.txt', encoding="utf8"))

    def kill(self):
        self.hangman = list(open('temps/temp3.txt', encoding="utf8"))

    def game_over(self):
        if self.attempts == 0:
            return True
        else:
            if '❓' in self.word_temp:
                return False
            else:
                return True

    def restart_game(self):
        print("WANNA PLAY ONE MORE TIME?")
        print("COOL! HERE YOU GO!")
        self.hangman = list(open('temps/default.txt', encoding="utf8"))
        self.word = 'XGBoost'
        self.word_temp = list(['❓ ' * len(self.word)][0][:-1])
        self.attempts = 3
        self.picked_words = []

    def update_temp(self):
        if self.attempts == 2:
            self.create_seat()
        elif self.attempts == 1:
            self.create_gallows()
        elif self.attempts == 0:
            self.kill()
