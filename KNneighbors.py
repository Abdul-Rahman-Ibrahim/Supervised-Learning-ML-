import numpy as np
from math import sqrt
from collections import Counter

def euclideanDistance(arr1, arr2):
    
    return sqrt( sum( (np.array(arr1)-np.array(arr2) )**2) )

def kNearestNeighbor(data, prediction, k=5):
    
    distances = []
    for group in data:
        for features in data[group]:
            euclidean_distance = euclideanDistance(features, prediction)
            distances.append([euclidean_distance, group])
    
    votes = []
    for i in sorted(distances)[:k]:
        votes.append(i[1])
    
    confidence = Counter(votes).most_common()[0][1]/k
    
    vote_result = Counter(votes).most_common(1)[0][0]
    
    return vote_result, confidence

def checkAccuracy(data):
    
    correct = 0
    total = 0
    for group in data:
        for features in data[group]:
            vote, confidence = kNearestNeighbor(data, features, k=5)
            if vote == group:
                correct += 1
            total += 1
    
    return correct/total
