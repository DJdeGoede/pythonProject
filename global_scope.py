high_score = 600


def score():    
    global high_score
    new_score = 645
    if new_score > high_score:
        print ('New high score')
        high_score = new_score


score()
print (high_score)









