# Program to help figure this bullshit class out

# inverse the equation to get things in price 
# find out new equation by adding to price directly 
import numpy as np
import matplotlib.pyplot as plt 

def demand_change():
    pass

def supply_change():
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


def main():
    print("------ Quantity DEMANDED ------")
    quantity_demanded_constant = float(input("Enter constant "))

    quantity_demanded_coffp = float(input("Enter coefficient of P with sign "))
    # Why is sign reversed here? 
    # quantity_demanded_coffp_sign = input("Enter sign of P ")
    print(f"Equation looks like:\nQ.D={quantity_demanded_constant} {quantity_demanded_coffp}P")
    quantity_demanded_coffp = -quantity_demanded_coffp

    print("------ Quantity SUUPLIED ------")
    # quantity_supplied = int(input("Enter Quantity supplied or Q.S "))
    quantity_supplied_constant = float(input("Enter constant "))
    quantity_supplied_coffp = float(input("Enter coefficient of P with sign "))
    # quantity_supplied_coffp_sign = input("Enter sign of P ")
    print(f"Equation looks like:\nQ.D={quantity_supplied_constant} {quantity_supplied_coffp}P")
    quantity_supplied_coffp = -quantity_supplied_coffp

    A = np.array(
        [
            [1, quantity_demanded_coffp],
            [1, quantity_supplied_coffp]
        ]
    )
    b = np.array(
        [quantity_demanded_constant, quantity_supplied_constant]
    )
     
    z = np.linalg.solve(A,b)
    print(z)
    print(f'{z[0]}: is Q or L')
    print(f'{z[1]}: is P or W')

    print('----------------------------\n')
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
    y_intercpt_demand = find_y_intercept(quantity_demanded_constant, -quantity_demanded_coffp)
    y_intercpt_quantity = find_y_intercept(quantity_supplied_constant, -quantity_supplied_coffp)
    print('Y-intercept of Demand Curve is: ', y_intercpt_demand)
    print('Y-intercept of Supply Curve is: ', y_intercpt_quantity)

    total_surplus = find_total_surplus(y_intercpt_demand, y_intercpt_quantity, z[0])
    print('Total Surplus iss: ', total_surplus)
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
        type_change = input ('Demand or Supply\t')
        if type_change == 'D' or type_change == 'd':
            demand_change()
        elif type_change == 's' or type_change == 'S':
            supply_change()


main()