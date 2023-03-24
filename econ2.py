# Program to help figure this bullshit class out

# inverse the equation to get things in price 
# find out new equation by adding to price directly 
import numpy as np
import matplotlib.pyplot as plt 




"""
    3x - 9y = -42
    2x + 4y = 2

    [3 -9] [x] = [-42]
    [2  4] [y] = [ 2 ]
       A    z  =   b
    
       z = A` (inverse) b
"""

# What all do you need? 
# Quantity Demanded Constant        QDC
# Quantity Demanded Coefficient     QDF
# Quantity Supplied Constant        QSD
# Quantity Supplied Coefficient     QSF

def find_eqilibirum(QDC, QDF, QSC, QSF):
    # Step 1: Change the signs of Coefficients or 'Send them to the other side'
    QDF = -QDF
    QSF = -QSF

    A = np.array(
        [
            [1, QDF],
            [1, QSF]
        ]
    )
    b = np.array(
        [QDC, QSC]
    )
     
    z = np.linalg.solve(A,b)
    # print(z)
    # Z[0] is X  AKA Q AKA Equilbirum 
    # Z[1] is Y 
    return z[0], z[1]
    

def demand_change(CHANGE):
    pass

def supply_change(CHANGE):
    pass

def inverse_demand_change(CHANGE, QDC, QDF):
    # Remember that the equations we get are in terms of QD = QDC + QDF x P
    
    # QD = QDC + QDF x P
    
    # Step 1 
    # Send coefficient to other side

    # QD - QDC = QDF x P

    # Step 2: Divide both side (or just the QD and QDC with QDF)

    # QD/QDF - QDC/QDF = P

    # QD/QDF - QDC/QDF + CHANGE = P

    # QD/QDF = P - CHANGE + QDC/QDF

    # QD =    QDF(P - CHANGE + QDC/QDF)

    # FINAL EQUATION 
    # QD = -CHANGE x QDF + QDC + P x QDF
    
    # We can just send back the updated values of QDC, QDF
    QDC = -CHANGE*QDF + QDC 

    return QDC

    pass

def inverse_supply_change(CHANGE):
    pass



def find_y_intercept(constant, coffp):
    # Assume that our Q AKA x is always 1 
    '''
    x = b + yM
    x - b / m = y
    y = x/m - b/m 
    making y intercept to be reverse sign of b over m 
    '''
    return -constant/coffp

def find_total_surplus(y_intercpt_demand, y_intercpt_quantity, base):
    return 0.5*(y_intercpt_demand - y_intercpt_quantity) * (base)


def find_consumer_surplus(y_intercpt_demand, eq_y, base):
    return 0.5*(y_intercpt_demand - eq_y) * (base)



def main():
    print("------ Quantity DEMANDED ------")
    QDC = float(input("Enter constant "))
    QDF = float(input("Enter coefficient of P with sign "))
    print(f"Equation looks like:\tQ.D={QDC} {QDF}P")


    print("\n------ Quantity SUPPLIED ------")
    QSC = float(input("Enter constant "))
    QSF = float(input("Enter coefficient of P with sign "))
    print(f"Equation looks like:\tQ.D={QSC} {QSF}P\n")
    print('\n----------------------------\n')

    """
    3x - 9y = -42
    2x + 4y = 2

    [3 -9] [x] = [-42]
    [2  4] [y] = [ 2 ]
       A    z  =   b
    
       z = A` (inverse) b
    """

    Equilibrium_quantity, Equilibirum_price = find_eqilibirum(QDC, QDF, QSC, QSF)

    print(f'\nEquilibirum Quantity is\t{Equilibrium_quantity} \t or L')
    print(f'\nEquilibirum Price is\t{Equilibirum_price} \t or W')

    print('\n----------------------------\n')
    print('Calculating Total Surplus Now')
    '''
    height = y intercept of demand - y intercept of supply
    base = x point of intersection which is z[0]
    x = b + yM
    x - b / m = y
    y = x/m - b/m 
    making y intercept to be reverse sign of b over m 
    Where x =
    '''
    y_intercpt_demand = find_y_intercept(QDC, QDF)
    y_intercpt_quantity = find_y_intercept(QSC, QSF)
    print('Y-intercept of Demand Curve is: ', y_intercpt_demand)
    print('Y-intercept of Supply Curve is: ', y_intercpt_quantity)

    total_surplus = find_total_surplus(y_intercpt_demand, y_intercpt_quantity, Equilibrium_quantity)
    print('Total Surplus is: ', total_surplus)

    consumer_surplus = find_consumer_surplus(y_intercpt_demand, Equilibirum_price, Equilibrium_quantity)
    print('Total Consumer is: ', consumer_surplus)

    print('Producer surplus: ', total_surplus - consumer_surplus)

    #############
    # Area under graph for total surplus
    # 1/2 * (DC - SC) ( Quantity bc it is the x value AKA z[0])
    """
    y = mx + b
    p = (q - constant) coffp
    y intercept is 
    """
    # Now to plot the demand and supply curve we have to inverse the equation

    change = input('Is there a change in Demand or Supply at any price P?\t')
    if change == 'Y' or 'y':
        type_change = int(input ('1.Supply\tReduce Quantity at any price\n2.Inverse Supply\tRaised the cost for any quantity supplied\n3.Demand\tReduced Quantity demanded at any price\n4.Inverse Demand\tIncrease WTP for any quantity demanded. \n\nTip: * A shift to the supply or demand function will be given in units of the good (e.g. demand for onions increases by 5 onions at any price).\nA shift to the inverse supply or demand function will be given in dollars (e.g. willingness-to-pay for onions increases by $2 at any quantity)\n'))
        change = int(input('Enter change with sign\t'))
        if type_change == 1:
            pass
        elif type_change == 2:
            pass
        elif type_change == 3:
            pass
        elif type_change == 4:
            new_QDC = inverse_demand_change(change, QDC, QDF)
            new_Equilibrium_quantity, new_Equilibirum_price = find_eqilibirum(new_QDC, QDF, QSC, QSF)

            print(f'\nEquilibirum Quantity is\t{new_Equilibrium_quantity} \t or L')
            print(f'\nEquilibirum Price is\t{new_Equilibirum_price} \t or W')

    # Need to add a function that lets me change the equations
    # There can be 4 options to do so. 
    # Add to Qs
    # Add to Inverse Qs
    # Add to Qd
    # Add to Inverse Qd


main()