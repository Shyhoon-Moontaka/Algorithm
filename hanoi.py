def towerOfHanoi(n,source,destination,auxiliary):
    if n==1:
        print("Move Disk 1 from Source:",source,"to Destination:",destination)
        return
    towerOfHanoi(n-1,source,auxiliary,destination)
    print("Move Disk:",n,"from Source:",source,"to Destination:",destination)
    towerOfHanoi(n-1,auxiliary,destination,source)
print(towerOfHanoi(4,"A","B","C"))