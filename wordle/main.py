import random, pygame, pygame.freetype

pygame.init()
words = open("words.txt").read()
words2 = open("words2.txt").read()
''''
words3=open("word3.txt").read()
words4=open("word4.txt").read()

'''
word_list = words.split("\n")
word2_list = words2.split("\n")
"""
word3_list=words3.split("\n")
word4_list=words4.split("\n")
"""
window = pygame.display.set_mode((250, 300))
pygame.display.set_caption("Wordle")
font = pygame.freetype.Font("Archivo-Regular.ttf", 45)
font.fgcolor = (255, 255, 255)
green = (76, 153, 0)
yellow = (220, 193, 17)
grey = (118, 118, 118)

running = True
while running:

    tier = 0
    correct_word = random.choice(word_list)
    correct_word_str = str(correct_word)
    correct_word_str = correct_word_str.lower()

    letter = list(correct_word_str)
    window.fill((235, 235, 235))
    while running:
        '''
        pygame.draw.line(window,(0,0,0),(0,0),(1000,0),15) 
        pygame.draw.line(window,(0,0,0),(0,0),(0,1200),15)
        pygame.draw.line(window,(0,0,0),(0,1200),(250,1200),15) 
        pygame.draw.line(window,(0,0,0),(250,0),(250,1200),15) 
        '''
        pygame.draw.line(window, (0, 0, 0), (50, 0), (50, 300), 5)
        pygame.draw.line(window, (0, 0, 0), (100, 0), (100, 300), 5)
        pygame.draw.line(window, (0, 0, 0), (150, 0), (150, 300), 5)
        pygame.draw.line(window, (0, 0, 0), (200, 0), (200, 300), 5)

        pygame.draw.line(window, (0, 0, 0), (0, 50), (250, 50), 5)
        pygame.draw.line(window, (0, 0, 0), (0, 100), (250, 100), 5)
        pygame.draw.line(window, (0, 0, 0), (0, 150), (250, 150), 5)
        pygame.draw.line(window, (0, 0, 0), (0, 200), (250, 200), 5)
        pygame.draw.line(window, (0, 0, 0), (0, 250), (250, 250), 5)
        '''
        pygame.draw.line(window,(0,0,0),(0,0),(250,0),15) 
        pygame.draw.line(window,(0,0,0),(0,0),(0,1200),15)
        pygame.draw.line(window,(0,0,0),(0,1200),(250,1200),15) 
        pygame.draw.line(window,(0,0,0),(250,0),(250,1200),15) 
        '''
        pygame.draw.line(window, (235, 235, 235), (50, 0), (50, 300), 3)
        pygame.draw.line(window, (235, 235, 235), (100, 0), (100, 300), 3)
        pygame.draw.line(window, (235, 235, 235), (150, 0), (150, 300), 3)
        pygame.draw.line(window, (235, 235, 235), (200, 0), (200, 300), 3)

        pygame.draw.line(window, (235, 235, 235), (0, 50), (250, 50), 3)
        pygame.draw.line(window, (235, 235, 235), (0, 100), (250, 100), 3)
        pygame.draw.line(window, (235, 235, 235), (0, 150), (250, 150), 3)
        pygame.draw.line(window, (235, 235, 235), (0, 200), (250, 200), 3)
        pygame.draw.line(window, (235, 235, 235), (0, 250), (250, 250), 3)

        # pygame.draw.line(window,(0,0,0),(250,0),(250,1000),10)

        pygame.display.flip()
        guess_str = input()
        guess = guess_str.lower()
        guess = list(guess_str)
        if guess_str == "exit":
            print("The word was " + correct_word_str + "!")
            break
        while len(guess) != 5:
            print("Word not 5 letters")
            guess_str = input()
            guess = guess_str.lower()
            guess = list(guess_str)
        while word_list.count(
                str(guess[0].upper()) + str(guess[1]) + str(guess[2]) +
                str(guess[3]) + str(guess[4])) < 1 and word_list.count(
                    guess_str) < 1 and word2_list.count(guess_str) < 1:
            print("Word not in list")
            guess_str = input()
            guess = guess_str.lower()
            guess = list(guess_str)

            while len(guess) != 5:
                print("Word not 5 letters")
                guess_str = input()
                guess = guess_str.lower()
                guess = list(guess_str)

        #print(str(guess[0].upper())+str(guess[1])+str(guess[2])+str(guess[3])+str(guess[4]))
        if guess[0] == letter[0]:
            letter1 = green
        elif guess[0] == letter[2] or guess[0] == letter[3] or guess[
                0] == letter[4] or guess[0] == letter[1]:
            letter1 = yellow

        else:
            letter1 = grey

        if guess[1] == letter[1]:
            letter2 = green
        elif guess[1] == letter[2] or guess[1] == letter[3] or guess[
                1] == letter[4] or guess[1] == letter[0]:
            letter2 = yellow

        else:
            letter2 = grey

        if guess[2] == letter[2]:
            letter3 = green
        elif guess[2] == letter[1] or guess[2] == letter[3] or guess[
                2] == letter[4] or guess[2] == letter[0]:
            letter3 = yellow

        else:
            letter3 = grey

        if guess[3] == letter[3]:
            letter4 = green
        elif guess[3] == letter[2] or guess[3] == letter[1] or guess[
                3] == letter[4] or guess[3] == letter[0]:
            letter4 = yellow

        else:
            letter4 = grey

        if guess[4] == letter[4]:
            letter5 = green
        elif guess[4] == letter[2] or guess[4] == letter[3] or guess[
                4] == letter[1] or guess[4] == letter[0]:
            letter5 = yellow

        else:
            letter5 = grey

        letter1_rect = pygame.Rect(0, tier, 50, 50)
        pygame.draw.rect(window, letter1, letter1_rect)

        letter2_rect = pygame.Rect(50, tier, 50, 50)
        pygame.draw.rect(window, letter2, letter2_rect)

        letter3_rect = pygame.Rect(100, tier, 50, 50)
        pygame.draw.rect(window, letter3, letter3_rect)

        letter4_rect = pygame.Rect(150, tier, 50, 50)
        pygame.draw.rect(window, letter4, letter4_rect)

        letter5_rect = pygame.Rect(200, tier, 50, 50)
        pygame.draw.rect(window, letter5, letter5_rect)

        font.render_to(window, (10, tier + 10), guess[0].upper())
        font.render_to(window, (60, tier + 10), guess[1].upper())
        font.render_to(window, (110, tier + 10), guess[2].upper())
        font.render_to(window, (160, tier + 10), guess[3].upper())
        font.render_to(window, (210, tier + 10), guess[4].upper())
        tier_for_lower = tier + 50
        tier += 50
        pygame.display.flip()

        if letter1 == green and letter2 == green and letter3 == green and letter4 == green and letter5 == green:

            print("Congratulations")
            input()
            break
        if tier == 300:
            print("The word was " + correct_word_str + "!")
            input()
            break











