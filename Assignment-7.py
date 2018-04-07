# By Ravikiran
# Numpy- 2 Assignment


mylist = [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]
# Window = 3
N = 3

cumsum, moving_aves = [0], []

for i, x in enumerate(mylist, 1):
    cumsum.append(cumsum[i-1] + x)
    if i>=N:
        moving_ave = (cumsum[i] - cumsum[i-N])/N
        print (moving_ave)
        moving_aves.append(moving_ave)
    
print (moving_aves)