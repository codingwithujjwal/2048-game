# importing the logic.py file 
# where we have written all the logic functions used
import logic 

# Driver code
if __name__ == '__main__':
    # calling start_game function
    # to initialize the matrix
    mat = logic.start_game()

while(True):
    # taking the user input 
    # for next step
    x = input("Press the command (W, A, S, D) : ")
    
    # we have to move up
    if x.lower() == 'w':
        # call the move up function
        mat, flag = logic.move_up(mat)
        
    # to move down
    elif x.lower() == 's':
        mat, flag = logic.move_down(mat)
    
    # to move left
    elif x.lower() == 'a':
        mat, flag = logic.move_left(mat)
    
    # to move right
    elif x.lower() == 'd':
        mat, flag = logic.move_right(mat)
        
    else:
        print("INVALID KEY PRESSED")
        continue

    # get the current state and print it
    status = logic.get_current_state(mat)
    print(status)
    
    # if game not over, continue and add new two
    if status == 'GAME NOT OVER':
        logic.add_new_2(mat)
    else:
        break

    # print the matrix after each move
    for row in mat:
        print(row)
