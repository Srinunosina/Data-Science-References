import numpy as np

def gradient_descent(x, y):
    
    m_current = b_current = 0
    learing_rate = 0.08
    iterations = 10000
    n = len(x)   
    
    cost_check_iterations = 5
    cost_iter_count = 0
    costs = []
    
    for i in range(iterations):
        y_predicted = m_current * x + b_current

        cost = (1/n) * sum([val ** 2 for val in (y-y_predicted)])
        
        costs.append(cost)
        
        if i > 1 and  costs[i] == costs[i-1] :
            cost_iter_count += 1            
            
        if cost_iter_count == cost_check_iterations:
            return           
                    
        
        md = - (2/n) * sum( x * (y - y_predicted))
        bd = - (2/n) * sum(y - y_predicted)

        m_current = m_current - learing_rate * md
        b_current = b_current - learing_rate * bd

        print(f"m_current : {m_current}  b_current : {b_current}  iteration: {i}   cost: {cost}  current_cost : {costs[i]}")

x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13])

gradient_descent(x , y)