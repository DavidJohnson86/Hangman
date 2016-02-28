# -*- coding: utf-8 -*-
'''
Created on 2016. febr. 24.
This gonna be a Hangman game

Implementation: 
random_word()
know_secretword()
check_if_guessed()
print_table()

Issues : 

Not English Characters (UTF-8) problem in stand alone mode.

Need to fix:
finish_game
tell_secret_word

History : 2016.02.24

Created method finish_game()
Check of correct data type
Addd method what draws the Gallows
Fixed to write the secret word if lost the game
Getting Capital letters now
Coding problems has been solved
Created method for secret topics

@author: David
'''

HANGMANPICS = ['''

 

    +---+

    |   |

        |

        |

        |

        |

  =========''', '''

  

    +---+

    |   |

    O   |

        |

        |

        |

  =========''', '''

  

    +---+

    |   |

    O   |

    |   |

        |

        |

  =========''', '''

  

    +---+

    |   |

    O   |

   /|   |

        |

        |

  =========''', '''

  

    +---+

    |   |

    O   |

   /|\  |

        |

        |

  =========''', '''

  

    +---+

    |   |

    O   |

   /|\  |

   /    |

        |

  =========''', '''

  

    +---+

    |   |

    O   |

   /|\  |

   / \  |

        |

  =========''']





from random import randrange
import random
import sys
reload(sys)
#secret_topic = u'''Állat Ország'''.split()
#secret_animal_words =  u'''ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule'''.split()
#secret_country_words =u'''magyarorszag orosz algeria'''.split()
guess_word = list ('example')

def finish_game():
    print 'Gratulalok megnyerted a jatekot.'
    while (1):
        user_input = raw_input('Akarsz meg egy jatekot ?')
        if user_input == 'i':
            main()
        elif user_input == 'n':
            sys.exit()
        else:
            print 'Rossz karaktert adtal meg kerlek valassz "i" vagy "n" karaktert'
        
# This function is return a random word


def safety_input(user_input,missed_letters):
   
    user_input = user_input.lower()   
    if len(user_input) != 1:
        return u'Kérlek egy betűt adj meg.'
    
    if user_input not in  u'aábcdeéfghiíjklmnoóöőprstuúüűvwyz':
        return  u'Érvényes karaktert adj meg' 
                            
    elif user_input == '':
        return u'Érvényes karaktert adj meg' 
                    
    elif user_input in missed_letters:
        return u'Ezt a betűt már megadtad egyszer'
        
    else:
        return True


def tell_secret_word():
    Dic = {u"Állatok":[u"hangya", u"pávián", u"borz" ,u"denevér" , u"medve", u"hód" ,u"teve" ,u"macska" ,u"kagyló", u"kobra",  u"puma", u"prérifarkas", u"szarvas" ,u"kutya", u"szamár" ,u"kacsa",u"sas", u"vadászgörény" , u"róka" ,u"béka" ,u"kecske" , u"liba" ,u"héja" ,u"oroszlán" , u"gyík" , u"láma", u"majom" ,u"jávorszarvas", u"egér", u"öszvér"], u"Országok": [u"görögország", u"olszország"]}
    r = [i for i in Dic][randrange(0, len(Dic))]
    #index = random.randint(0, len(Dic))
    #print Dic[u"Állatok"][1]
    return r, Dic[r][randrange(0, len(Dic[r])-1)]
        
    

        

def random_word(words):
    length = len(words)
    Number = random.randint(0,length-1)
    return words[Number]

# This section split the letters into a list
def know_secretword(word):
    secret_letters = []
    length = len(word)
    for i in range (0,length):
        secret_letters.append(word[i])
    return secret_letters    

#Check if the user guessed letter is good 
def check_if_guessed(user_input, secret_word):
    find_values = []
    length = len(secret_word)
    for i in range (0,length):
        if secret_word[i] == user_input:
            find_values.append(i)
        else:
            continue
    
    return find_values
        
def print_table(array, position, letter):
    length = len(position)
    for i in range (0, length):
        index= position[i]
        array[index] = letter
    return array

def display_board(number):
    print HANGMANPICS[number]
    

if __name__ == "__main__":
    
    def main():
        print '\nAkasztofa jatek '
        # Choose a random secret topic
        topic = tell_secret_word()
        if topic[1] == u'Állat':
            print u'Téma: Állat'
        elif topic[1 ]==u'Ország':
            print u'Téma: Ország'
        sw = random_word(tell_secret_word()[0])
        print tell_secret_word()[0]
        #print tell_secret_word()[1]
        print sw
        # Convert to list  the secret word
        guess_word= list(sw)
        
        # Print Blank Lines
        length_of_secretword = len(sw)
        #Draw Initial line '- - - - - - -'
        secret_word = list(length_of_secretword * '-')
        show_secret_word = ' '.join(secret_word)
        missed_words = 0
        missed_letters = ''
        # Begin game
        while (missed_words < 8):
            if missed_words == 7:
                 
                print 'Sajnos vege a jateknak a titkos szo : %s' %(sw.encode('utf-8'))
                break
            if guess_word == secret_word:
                print show_secret_word 
                finish_game()
            
            display_board(missed_words)
            print "Ennyi probalkozasod van meg : %s\n" %(6-missed_words)
            # User Guess a letter
            print show_secret_word 
            print 'T�vesztett bet�k: %s' %(missed_letters.encode('utf-8'))
            user_input = raw_input('\nAdd meg a tipped: ') 
            user_input = user_input.lower()            
            user_input = user_input.decode('utf-8')
            approved = safety_input(user_input, missed_letters)
            if approved != True:
                print approved
            else:   
           
                result =  check_if_guessed(user_input, guess_word)
                if result == [] :
                    missed_words += 1
                    missed_letters += user_input
                else:
                    show_secret_word = ' '.join (print_table(secret_word, result, user_input))
                    
    main()
               
             
            
    

