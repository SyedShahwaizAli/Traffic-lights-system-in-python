for i in range(3):
    light = input("Enter traffic light color (red/yellow/green): ")
    
    if light == "red":
        print("Stop")
    elif light == "yellow":
        print("Slow down")
    elif light == "green":
        print("Go")
    else:
        print("Invalid color!")