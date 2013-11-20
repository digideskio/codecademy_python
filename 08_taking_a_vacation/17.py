def hotel_cost(nights):
    return nights * 140

bill = hotel_cost(5)

def add_monthly_interest(balance):
    return balance * (1 + (0.15 / 12))

def make_payment(payment, balance):
    new_balance = add_monthly_interest(balance - payment)
    print "You still owe: %s" % new_balance
    return new_balance

new_bill = make_payment(bill / 2, bill) # Pay half the bill
print make_payment(100, new_bill) # Pay $100 more.
