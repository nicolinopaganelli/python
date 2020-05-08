#find wpm 
import time, random

TESTS = ['copy this text and hit enter to find your typing speed',
         'type me to find out how many words per minute you can type',
         'the quick brown fox jumps over the lazy dog while she sells sea shells by the sea shore'
]
TEST = random.choice(TESTS)

def main():
    WPM()

def WPM():
    print()
    print(TEST)
    input('(press enter to begin)\n')
    ORIG_TIME = time.time()
    ANSWER = input('>> ')
    FINAL_TIME = time.time()

    if ANSWER != TEST:
        fail()
        WPM()
    else:
        calculate(FINAL_TIME - ORIG_TIME)

def calculate(TIME):
    WORDS = (len(TEST.split(' ')))
    WPM = (WORDS * 60) / TIME
    print('you can type %s words per minute!' % (WPM))

def fail():
    print('\n\nthe string you entered was not the same as the one given ya goofball\ntry again\n')
    time.sleep(2)

if __name__ == '__main__':
    main()
