class Gallows:
    def __init__(self):
        self.words = []
        self.game_over = False

    def play(self, word):
        if self.game_over == True:
            self.words = []
            self.game_over = False

        if len(self.words) != 0:
            if self.words[-1][-1] != word[0] or word in self.words:
                self.game_over = True
                return "game_over"
            else:
                self.words.append(word)
                return self.words
        else:
            self.words.append(word)
            return self.words

    def restart(self):
        self.words = []
        return "game_restart"

my_gallows = Gallows()


print(my_gallows.game_over)
print(my_gallows.play('apple'))
print(my_gallows.words)
print(my_gallows.play('ear'))
print(my_gallows.play('rhino'))
print(my_gallows.play('ocelot'))
print(my_gallows.game_over)
print(my_gallows.play('oops'))
print(my_gallows.game_over)
print(my_gallows.words)
print(my_gallows.restart())
print(my_gallows.words)
print(my_gallows.game_over)
print(my_gallows.play('hostess'))
print(my_gallows.game_over, False)
print(my_gallows.play('stash'))
print(my_gallows.play('hostess'))
print(my_gallows.words)