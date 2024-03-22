x=0
success = False
while (not success):
    left_hand_side = x+1
    right_hand_side = x+2
    success = (left_hand_side == right_hand_side)
    if (not success):
        print("The value ", x, " did not work!")
        x = x+1
    else:
        print("Wow!  The value of X is ",x)
