"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

# List squares up to 1000^2
# Then find triplets whose square roots add to 1000
# Then see if those triplets are pythagorean

def ListSquares(limit):
    squares = []
    for i in range(0, int(limit ** 0.5) + 1):
        squares.append(i **2)
    return squares
    
# print(ListSquares(100**2))
    
def FindTriplets(squarelist, total):
    roots = [int(x **0.5) for x in squarelist]
    triplets = []
    for i in range(1, len(roots)):
        for j in range(i, len(roots)):
            for k in range(j, len(roots)):
                if (roots[i]+roots[j]+roots[k]) == total and i < j < k:
                    triplets.append([int(roots[i]) **2 , int(roots[j]) ** 2 , int(roots[k]) **2])
    return triplets
    
    
    
# print(FindTriplets(ListSquares(100**2), 12))
        
def PythTrips(tripletList):
    squarelist = [trip for trip in tripletList if trip[0] + trip[1] == trip[2]]
    return squarelist

#print("Squares")
#print(ListSquares(1000**2))
#print("Square Triplets")
#print(FindTriplets(ListSquares(1000**2), 1000))   
#print("Pythag Square triplets")

Solution = PythTrips(FindTriplets(ListSquares(1000**2), 1000)) # Highly inefficient but it works!
print(Solution[0][0] ** 0.5 * Solution[0][1] ** 0.5 * Solution[0][2] ** 0.5)