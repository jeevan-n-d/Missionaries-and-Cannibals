# Unicode emojis
MISSIONARY = '\U0001f482'
CANNIBAL = '\U0001f479'
WATER = '\U0001f30a'
BOAT = '\U0001f6A2'

# Game state
boat_side = 'Right'
missionaries_on_right = 3
cannibals_on_right = 3 
missionaries_on_left = 0
cannibals_on_left = 0 

def display():
    # Build left side
    left = MISSIONARY * missionaries_on_left + CANNIBAL * cannibals_on_left
    # Build water and boat
    water = WATER * 5  # adjust the number as you like

    # Build right side
    right = MISSIONARY * missionaries_on_right + CANNIBAL * cannibals_on_right

    if boat_side == 'Right':
        print(left + "|" + water + water  + BOAT + "|" + right)
    else:
        print(left + "|" + BOAT + water + water  + "|" + right)

# Initial display
display()

while True:
    missionaries = int(input('No of missionaries or enter 10 to quit : '))
    if missionaries == 10:
        print('You Quit. Game Over!')
        break
    cannibals = int(input('No of cannibals : '))

    if (missionaries + cannibals) != 1 and (missionaries + cannibals) != 2:
        print('Invalid Move')
        continue
    #Adding more than 2 into boat

    if boat_side == 'Right':
        if missionaries_on_right < missionaries or cannibals_on_right < cannibals:
            print('Invalid Move')
            continue
        #⚠️ If you are trying to put more missionaries or cannibals in the boat than actually exist on the right side → it’s an invalid move!

        missionaries_on_right -= missionaries
        cannibals_on_right -= cannibals
        missionaries_on_left += missionaries
        cannibals_on_left += cannibals
        boat_side = 'Left'
    else:
        if missionaries_on_left < missionaries or cannibals_on_left < cannibals:
            print('Invalid Move')
            continue

        missionaries_on_left -= missionaries
        cannibals_on_left -= cannibals
        missionaries_on_right += missionaries
        cannibals_on_right += cannibals
        boat_side = 'Right'

    display()

    if (missionaries_on_right < cannibals_on_right and missionaries_on_right > 0) or \
       (missionaries_on_left < cannibals_on_left and missionaries_on_left > 0):
        print('You Lose!')
        break

    if missionaries_on_left == 3 and cannibals_on_left == 3:
        print('You Win!')
        break