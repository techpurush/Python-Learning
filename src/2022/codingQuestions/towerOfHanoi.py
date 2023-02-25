def towerOfHanoi(noOfDisk,source,helper,destination):

    if noOfDisk ==1:
        print("transfer disk ", noOfDisk, " from ", source, " to ", destination)
        return

    towerOfHanoi(noOfDisk-1,source,destination,helper)
    print("transfer disk ",noOfDisk," from ",source," to ",destination)
    towerOfHanoi(noOfDisk-1,helper,source,destination)



towerOfHanoi(3,"S","H","D")