# Get function iter 
def get_next_point(step):

    x = int(input(f"\nInput x{step} coordinates: "))
    y = int(input(f"\nInput y{step} coordinates: "))
    return(x,y) # Sending back x and y 
 
def cal_distance(p1,p2):
    distance = (int(pow((p2[0] - p1[0]),2)) + int(pow((p2[1] - p1[1]),2)))
    distance = pow(distance,0.5)
    return distance

def main():
    print("------Robot Program------")
 
    running = True # For inifite running code 
    step = [(0,0)] # stores co-ordinate
    total = 0
    iter = 1 
    printer = 1
    distance = [] # stores distance data 
 
    while running:
        p1 = get_next_point(iter)
        step.append(p1)
        iter += 1 
        if p1 == (999,999):
            running = False
            len_of_cal = len(step) # Function to find out the length of the step list which has stored co-ordinates
 
            for i in range(((int(len_of_cal/2))+1)):
                distance.append(cal_distance(step[i], step[i+1]))
            print("-"*10)
            for number in distance:
                print("Step {}: {:.2f} units".format(printer, number))
                printer += 1
                total += number
            print(f'Total distance trallveld by the robot: {total} units ') 
            print("-"*10)
 
if __name__ == "__main__":
    main()
