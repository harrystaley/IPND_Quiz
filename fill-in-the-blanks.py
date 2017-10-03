import random

# define lvls, questions, answers, lvls, responses, etc.

#QUESTIONS
question1 = '''Row, row, row your ___1___. Gently down the ___2___.
Merrily, merrily, merrily, merrily. ___3___ is but a ___4___.'''
question2 = '''When I find ___1___ in times of ___2___
Mother ___3___ comes to me
Speaking ___4___ of ___5___, let it be'''
question3 = '''Once upon a midnight ___1___, while I pondered, weak and ___2___,
Over many a ___3___ and curious volume of forgotten lore -
While I ___4___, nearly napping, suddenly there came a tapping,
As of some one gently rapping, rapping at my chamber door.
"'Tis some ___5___," I muttered, "tapping at my chamber door -
Only this and nothing more."'''
questions = [question1, question2, question3]

#ANSWERS
key1 = ['boat', 'stream', 'life', 'dream']
key2 = ['myself', 'trouble', 'Mary', 'words', 'wisdom']
key3 = ['dreary', 'weary', 'quaint', 'nodded', 'visitor']
keys = [key1, key2, key3]

lvls = ["Easy", "Medium", "Hard"]
lvl_desc = ["Nice and easy.",
              "This should be good for now.",
              "This should be interesting!"]

#INCORRECT RESPONSE
incorrect_resp = ["Try again.",
                  "That may be right in some other universe.",
                  "Fail less."]

#INTRO
intro = '''Choose your difficulty lvl:
1 - Easy
2 - Medium
3 - Hard'''


def failed_guess():
    '''When called it returns a response to the user wo entered an
    incorrectly.
    input: none
    ouput: wrong string'''
    output = incorrect_resp[random.randint(0, len(incorrect_resp)-1)]
    print output


def format(text):
    '''Produces x lines with a single '.' char preceding the
    string, seperating the most current string from previous output.
    input: string
    ouput: x printed lines of '.' followed by the string'''
    rows = 2
    for i in range(0, rows):
        print "\n"
    print text


def select_lvl():
    '''Prompts the user to select a difficulty, based on the index,
    count, and validates user input input. Any non-integer entry, or
    entries outside the range, returns a response and repropts the
    user until a valid input returned.
    input: none
    output: selected level'''
    lvl = 0
    lvl_min = 1
    lvl_max = len(lvls)
    lvls_str = "("+str(lvl_min)+"-"+str(lvl_max)+")"
    while True:
        try:
            lvl = raw_input("Choose your poison "+lvls_str+":")
            lvl = int(lvl)
        except ValueError:
            pass
        if lvl in range(lvl_min, lvl_max+1):
            break
        print "You have either picked a wrong number, or typed something else \
        altogether. Genius."
    return lvl


def play(ilvl):
    '''Take lvl passed in, plays the game given that lvl, pulling
    the string and answer key from the correct index in their respective
    sets. As each correct answer is given, replaces blank in string with
    the correct answer, and neatly displays the string again, asking for
    the next blank, until all have been filled.
    input: lvl selection
    output: nothing returned, interacts with user in terminal to play game'''
    print "Ok, let's play."
    print "You have selected: " + lvls[ilvl]
    print lvl_desc[ilvl]
    output_str = questions[ilvl]
    print output_str
    for answer in keys[ilvl]:
        answers = keys[ilvl]
        pos = answers.index(answer)+1
        input_query = "Fill in blank #"+str(pos)+"?"
        guess = raw_input(input_query)
        while guess != answer:
            failed_guess()
            print "Let's try again."
            guess = raw_input(input_query)
        output_str = output_str.replace('___'+str(pos)+'___', answer)
        format(output_str)

    print "******Good job!******"


def start():
    '''This will print the introduction to the game and get a difficulty
    selection from the user, then pass that selection over to the actual
    game play.
    input: none
    output: nothing returned, interacts with user to start game,
            call play()'''
    print "Shall we play a game?"
    rows = 2
    for i in range(0, rows):
        print "\n"
    print intro
    ilvl = select_lvl()-1
    play(ilvl)

start()