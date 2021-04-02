import sys

def game_chooser():
    print()
    print('What grid size are using for this Payoff Matrix?')
    print('Enter A for 2 x 2, or B for 3 x 3')
    print()
    grid_size = input('A or B: ')

    while grid_size not in ['a', 'A', 'b', 'B']:
        grid_size = input('Please Enter A Valid Input: ')

    if grid_size in ['a', 'A']:
        two_by_two()
        print()
        start_again()

    elif grid_size in ['b', 'B']:
        three_by_three()
        print()
        start_again()

def two_by_two():
    print()
    print('      |-Left-||-Right|')
    print(' Up   | A, B || C, D |')
    print('Down  | E, F || G, H |')
    print()
    print('Please Enter the Values for your Matrice That Correspond to the Above Letters ')

    up_left = []
    up_right = []
    down_left = []
    down_right = []
    up_left.append(float(input('Please Enter A Value for A: ')))
    up_left.append(float(input('Please Enter A Value for B: ')))
    up_right.append(float(input('Please Enter A Value for C: ')))
    up_right.append(float(input('Please Enter A Value for D: ')))
    down_left.append(float(input('Please Enter A Value for E: ')))
    down_left.append(float(input('Please Enter A Value for F: ')))
    down_right.append(float(input('Please Enter A Value for G: ')))
    down_right.append(float(input('Please Enter A Value for H: ')))

    if up_left[0] >= down_left[0] and up_left[1] >= up_right[1]:
        up_left_bool = 1
    else:
        up_left_bool = 0

    if down_left[0] >= up_left[0] and down_left[1] >= down_right[1]:
        down_left_bool = 1
    else:
        down_left_bool = 0

    if up_right[0] >= down_right[0] and up_right[1] >= up_left[1]:
        up_right_bool = 1
    else:
        up_right_bool = 0

    if down_right[0] >= up_right[0] and down_right[1] >= down_left[1]:
        down_right_bool = 1
    else:
        down_right_bool = 0

    bool_values = [up_left_bool, up_right_bool, down_left_bool, down_right_bool]

    print()
    if up_left_bool == 1:
        print('Up, Left is a Nash Equilibrium')
    else:
        pass

    if up_right_bool == 1:
        print('Up, Right is a Nash Equilibrium')
    else:
        pass

    if down_left_bool == 1:
        print('Down, Left is a Nash Equilibrium')
    else:
        pass

    if down_right_bool == 1:
        print('Down, Right is a Nash Equilibrium')
    else:
        pass

    if 1 not in bool_values:
        print('There are no Nash Equilibria')
    else:
        pass

def three_by_three():
    print()
    print('      |-Left-|-Middle-|-Right-|')
    print(' Up   | A, B |  C, D  |  E, F |')
    print(' Mid  | G, H |  I, J  |  K, L |')
    print(' Down | M, N |  O, P  |  Q, R |')
    print()
    print('Please Enter the Values for your Matrice That Correspond to the Above Letters ')

    up_left = []
    up_middle = []
    up_right = []
    mid_left = []
    mid_middle = []
    mid_right = []
    down_left = []
    down_middle = []
    down_right = []

    up_left.append(float(input('Please Enter a Value for A: ')))
    up_left.append(float(input('Please Enter a Value for B: ')))
    up_middle.append(float(input('Please Enter a Value for C: ')))
    up_middle.append(float(input('Please Enter a Value for D: ')))
    up_right.append(float(input('Please Enter a Value for E: ')))
    up_right.append(float(input('Please Enter a Value for F: ')))
    mid_left.append(float(input('Please Enter a Value for G: ')))
    mid_left.append(float(input('Please Enter A Value for H: ')))
    mid_middle.append(float(input('Please Enter a Value for I: ')))
    mid_middle.append(float(input('Please Enter a Value for J: ')))
    mid_right.append(float(input('Please Enter a Value for K: ')))
    mid_right.append(float(input('Please Enter a Value for L: ')))
    down_left.append(float(input('Please Enter a Value for M: ')))
    down_left.append(float(input('Please Enter a Value for N: ')))
    down_middle.append(float(input('Please Enter a Value for O: ')))
    down_middle.append(float(input('Please Enter a Value for P: ')))
    down_right.append(float(input('Please Enter a Value for Q: ')))
    down_right.append(float(input('Please Enter a Value for R: ')))

    if (up_left[0] >= mid_left[0] and up_left[0] >= down_left[0]) and (up_left[1] >= up_middle[1] and up_left[1] >= up_right[1]):
        up_left_bool = 1
    else:
        up_left_bool = 0

    if (mid_left[0] >= up_left[0] and mid_left[0] >= down_left[0]) and (mid_left[1] >= mid_middle[1] and mid_left[1] >= mid_right[1]):
        mid_left_bool = 1
    else:
        mid_left_bool = 0

    if (down_left[0] >= up_left[0] and down_left[0] >= mid_left[0]) and (down_left[1] >= down_middle[1] and down_left[1] >=down_right[1]):
        down_left_bool = 1
    else:
        down_left_bool = 0

    if (up_middle[0] >= mid_middle[0] and up_middle[0] >= down_middle[0]) and (up_middle[1] >= up_left[1] and up_middle[1] >= up_right[1]):
        up_middle_bool = 1
    else:
        up_middle_bool = 0

    if (mid_middle[0] >= up_middle[0] and mid_middle[0] >= down_middle[0]) and (mid_middle[1] >= mid_left[1] and mid_middle[1] >= mid_right[1]):
        mid_middle_bool = 1
    else:
        mid_middle_bool = 0

    if (down_middle[0] >= up_middle[0] and down_middle[0] >= mid_middle[0]) and (down_middle[1] >= down_left[1] and down_middle[1] >= down_right[1]):
        down_middle_bool = 1
    else:
        down_middle_bool = 0

    if (up_right[0] >= mid_right[0] and up_right[0] >= down_right[0]) and (up_right[1] >= up_middle[1] and up_right[1] >= up_left[1]):
        up_right_bool = 1
    else:
        up_right_bool = 0

    if (mid_right[0] >= up_right[0] and mid_right[0] >= down_right[0]) and (mid_right[1] >= mid_middle[1] and mid_right[1] >= mid_left[1]):
        mid_right_bool = 1
    else:
        mid_right_bool = 0

    if (down_right[0] >= mid_right[0] and down_right[0] >= up_right[0]) and (down_right[1] >= down_middle[1] and down_right[1] >= down_left[1]):
        down_right_bool = 1
    else:
        down_right_bool = 0

    bool_values = [up_left_bool, mid_left_bool, down_left_bool, up_middle_bool, mid_middle_bool, down_middle_bool, up_right_bool, mid_right_bool, down_right_bool]
    print()

    if up_left_bool == 1:
        print('Up, Left is a Nash Equilibrium')
    else:
        pass

    if mid_left_bool == 1:
        print('Mid, Left is a Nash Equilibrium')
    else:
        pass

    if down_left_bool == 1:
        print('Down, Left is a Nash Equilibrium')
    else:
        pass

    if up_middle_bool == 1:
        print('Up, Middle is a Nash Equilibrium')
    else:
        pass

    if mid_middle_bool == 1:
        print('Mid, Middle is a Nash Equilibrium')
    else:
        pass

    if down_middle_bool == 1:
        print('Down, Middle is a Nash Equilibrium')
    else:
        pass

    if up_right_bool == 1:
        print('Up, Right is a Nash Equilibrium')
    else:
        pass

    if mid_right_bool == 1:
        print('Mid, Right is a Nash Equilibrium')

    if down_right_bool == 1:
        print('Down, Right is a Nash Equilibrium')
    else:
        pass

    if 1 not in bool_values:
        print('There are no Nash Equilibria')
    else:
        pass


def start_again():
    start_again = input('Would You Like to Enter Another Matrix? (y/n): ')

    if start_again == 'y':
        game_chooser()

    elif start_again == 'n':
        print('Thanks for Playing')
        sys.exit()

    else:
        while start_again != 'y' or 'n':
            start_again = input('Please Enter a Valid Input: ')
            if start_again == 'y':
                game_chooser()

            elif start_again == 'n':
                sys.exit()

game_chooser()






