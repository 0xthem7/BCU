# Get function iter 
#variables

coordinate = () #This is the varaible which stores the cordinates
cooStore = [] # It stores all the coordinates for further processing 
distance = [] # It stores data provided by 


def get_next_point(step):
    '''This is the function which takes step and returns the cordinates for further works.'''
    x = int(input(f"\nInput x{step} coordinates: "))
    y = int(input(f"\nInput y{step} coordinates: "))
    return(x,y) # Sending back x and y 
 
def cal_distance(p1,p2):
    '''THis is the function which calculates the distance'''
    distance = (int(pow((p2[0] - p1[0]),2)) + int(pow((p2[1] - p1[1]),2)))
    distance = pow(distance,0.5)
    return distance

def printer():
    total = 0
    print("-"*10)
    for i,item in enumerate(distance):
        print(f"Step {i+1}: {item:.2f} units")
        total += item
    print("-"*10)
    print(f"Total distance trallveld by the robot: {total:.2f}")
        
def main():
    global coordinate, cooStore, distance
    print("------Robot Program------") 
    step = 0 
    
    while coordinate!=(999,999):
        coordinate = get_next_point(step)
        cooStore.append(coordinate)
        step += 1 
    else:
        len_of_cal = len(cooStore) # Function to find out the length of the step list which has stored co-ordinates
        # Storing the calculated distance
        for i in range(((int(len_of_cal/2)))):
            distance.append(cal_distance(cooStore[i], cooStore[i+1]))
        printer() 
 
if __name__ == "__main__":
    main()
