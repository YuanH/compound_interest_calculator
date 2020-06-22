import math
# FV   =   P (1  +  r / n)Yn
# FV = Future Value
# P = Principle
# r = annual interest rate
# n = number of compound per year (12 is monthly)
# Y = year

# Rule of 72: A rough estimate of how many years it takes for your investment to double:
# For example, if interest rate is 8%, it would take roughly 72/8 = 9 years for your investment to double

def fv(P, r_n, counter):
    #r2  = r/n
    #counter = installments left
    FV = P * (1+r_n) ** counter
    return FV

if __name__ == "__main__":
    r = float(input("What's your compound interest rate? (use 0.07 for 7%): "))
    Y = int(input("How many years are you expecting to invest?: "))
    n = int(input("How many installments per year? (i.e. if you invest monthly, use 12): "))
    P = float(input("How much are you putting down as your princple?: "))
    I = float(input("Investment per installment: "))
    # Y = 20
    # r = 0.07
    # n = 12
    # P = 71488 + 52988 + 50000 #without 401k
    # P = 71488 + 52988 + 50000 + 163000 # with 401k
    # P = 200000
    #p2 = annual injections
    # p2 = 2000 * 12 #without 401k
    # p2 = (2000 + 3000) * 12 # with 401k

    counter = Y * n
    r_n = r / n
    FV = fv(P, r_n, counter)
    
    while counter > 0:
        
        FV += fv(I,r_n,counter)
        counter -= 1
    
    print('${:,.2f}'.format(FV))
