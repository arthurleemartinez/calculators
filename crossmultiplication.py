# I need to calculate the amount of money I need to spend to cancel out the $39 Quicksilver annual fee
# The life-time cash back bonus is 1.5%

# "x over y equals o over b" , find b
# only need to specify 2 variables, 
# x = 0.015 
# o = 39

# represent cross multiplication as quadrants!
# cross multiplication calulcator if you're comparing to percentage value represented as decimal
y = 1
def crossPercentage(x, o):
    right = (o * y) 
    left = right
    answer1 = (left/x)
    answer2 = str(answer1)
    return answer2
# function call using previously specified variables    
print crossPercentage(0.015, 39)
