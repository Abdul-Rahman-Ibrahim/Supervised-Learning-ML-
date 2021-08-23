import numpy as np

def SquareError(arr1, arr2):
    return sum( (np.array(arr1)-np.array(arr2))**2 )
    
def Mean(arr):
    return sum(arr)/len(arr)
    
def BestFitLine(np.array(xs), np.array(ys)):
    m = ( (Mean(xs)*Mean(ys) - Mean(xs*ys))/
        (Mean(xs)**2 - Mean(xs**2)) )
    b = Mean(ys) - m*Mean(xs)
    
    ys_line = [m*x+b for x in xs]
    return ys_line
    
def CoeffiecientOfDetermination(ys, ys_line):
    ys_mean = [Mean(ys) for _ in ys]
    ys_mean_error = SquareError(ys, ys_mean)
    ys_line_error = SquareError(ys, ys_line)
    
    return 1 - ys_line_error/ys_mean_error