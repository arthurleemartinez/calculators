# I need to calculate the amount of money I need to spend to cancel out the $39 Quicksilver annual fee
# The life-time cash back bonus is 1.5%

# "x over y equals o over b" , find b
# only need to specify 2 variables,
# x = 0.015
#card_annual_fee: int = 39
card_annual_fee = float(input("What is your prospective card's annual fee (USD)?"))

user_cash_back_bonus_string = input("What is your prospective card's life-time cash back-bonus (or similar bonus) as a percentage?")
# convert bonus percentage to float/decimal
user_cash_back_bonus = float(user_cash_back_bonus_string)/100
# cross multiplication calculator if you're comparing to percentage value represented as decimal
def cross_percentage(x, o):
    # represents cross multiplication as the expression "x over 1 equals o over b" , find b"!
    # basically represents the components of cross multiplication problem as quadrants as quadrants
    right = (o * 1)
    left_numerator = right
    assert isinstance(x, float)
    answer1 = (left_numerator/x)
    spending_target = str(answer1)
    spending_target_string = "You would need to spend at least $%s a year for this card to be worth the annual fee." %spending_target
    return spending_target_string
# function call using previously specified variables
print(cross_percentage(user_cash_back_bonus, card_annual_fee))
