def trap(heights):
    n=len(heights)
    
    leftmax=[0]*n 
    rightmax=[0]*n
    water=[0]*n 
     

    
    leftmax[0] = heights[0]
    for i in range(1,n):
      leftmax[i]=max(leftmax[i-1],heights[i])

    rightmax[n-1]=heights[n-1]
    for i in range(n-2,-1,-1):
      rightmax[i]=max(rightmax[i+1],heights[i])

     for i in range(n):
     water[i]=max(0,min(leftmax[i],rightmax[i])-heights[i])

     


     sum_water=0
     for i in water: 
        sum_water+=i

    return sum_water,water




}
