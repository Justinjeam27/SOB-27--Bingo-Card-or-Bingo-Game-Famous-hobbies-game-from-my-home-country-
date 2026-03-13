#Name:Justin Crisostomo
#MISIS:M00909415
#PDE1130-Programming paradigms of computing and IOT
#Programme name:(BEng)Electronic Engineering
#lecturer name:Dr.Engie Bashir

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
import random

random_number_list = random.sample(range(1,79),78)

def print_a_card(bingo_card):
    #the card needs to print.
    #argument:card should be printed out.

    for letter in bingo_card:
        print(letter, end="\t")
        for num in bingo_card[letter]:
            print(num, end="\t")
        print("\n")
        print("\n")

def draw_a_card():
    #drawing a bingo card and storing random numbers

    bingo_card ={"B":[],"I":[],"N":[],"G":[],"O":[],}
    min = 1
    max = 15
    for letter in bingo_card:
        bingo_card[letter] = random.sample(range(min, max),5)
        min += 15
        max += 15
        if letter == "N":
            bingo_card[letter][1] = "Z"
    return bingo_card

def win_check(bingo_card):
    #if the numbers is in horizontal,diagonal or even vertical in the card,then the player is the winner.
    #argument:the card needs to be check in order to win

    you_win = False
    if bingo_card["B"][0] == "Z" and bingo_card["I"][1] == "Z" and bingo_card["N"][2] == "Z" and bingo_card["G"][3] == "Z" and bingo_card["O"][4] == "Z":
        you_win = True
    elif bingo_card["O"][0] == "Z" and bingo_card["G"][1] == "Z" and bingo_card["N"][2] == "Z" and bingo_card["I"][3] == "Z" and bingo_card["B"][4] == "Z":
        you_win = True
    elif bingo_card["B"][0] == "Z" and bingo_card["O"][4] == "Z" and bingo_card["B"][4] == "Z" and bingo_card["O"][0] == "Z":
        you_win = True  
    for letter in bingo_card:
        if(len(set(bingo_card[letter]))==1):
            you_win = True
    for j in range(5):
        cntnum = 0
        for letter in bingo_card:
            if bingo_card[letter][j] == "Z":
                cntnum +=1
        print(cntnum)
        if cntnum == 5:
            you_win = True
            break
    return you_win

def pop(bingo_card, randnumlist):
    #pops a random numbers in the list and can easily detects any duplicates numbers when the card is drawn.
    #Arguments:card:card will whether check if the number on the list is drawn or not.
    #list:random numbers to be drawn from the list.

    Drawn_num = random_number_list.pop()
    for letter in bingo_card:
        l = 0
        for num in bingo_card[letter]:
            if num == Drawn_num:
                bingo_card[letter][l] = 'Z'
            l += 1
        return Drawn_num

def main_menu():
    """
    main menu on a program.
    Draw a bingo card,print a number, and the program will goes on a loop through drawing and printing a number,
    for process and to the wincheck step that tells the user that the win is true or enters 'Exit bingo'.
    """

    print("Play/open BINGO")
    bingo_card = draw_a_card()

    print("\n Here is your bingo card: \n")
    print_a_card(bingo_card)

    print("\nTry to continously press enter to keep playing or else type Exit bingo.")
    input_user = input()
    you_win = win_check(bingo_card)
    tokens_to_win = 0

    while you_win == False and input_user != 'Exit bingo':
        Drawn_num = pop(bingo_card, random_number_list)
        tokens_to_win += 1

        print(f"\ndrawn number: {Drawn_num}.")
        print(f"drawn tokens total: {tokens_to_win}.\n")
        print_a_card(bingo_card)

        you_win = win_check(bingo_card)
        input_user = input()

    if you_win == True:
        print(f"\n\nBingo! You win of total tokens: {tokens_to_win}.")
    else:
        print("Thank you for playing Bingo!")

main_menu()
