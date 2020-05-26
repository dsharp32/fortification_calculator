def return_v_x(v_1, p_1, p_2, p_f):
    """Computes v_x using percentage equation.  
    All arguments should be positive floats. p_1, p_2 & p_f are percentages.
    v_1 and v_x are volumes in millilitres.
    """
    v_x = 0
    while((((((p_1/100) * v_1) + ((p_2/100) * v_x))/(v_1 + v_x)) * 100) < p_f): 
        v_x += .1
        v_x = round(v_x,1)
        continue
    return v_x

def test_v_x(v_1, p_1, p_2, v_x, p_f):
    """Tests v_x value with percentage equation and compares with desired final percentage. 
    """
    a = (((((p_1/100) * v_1) + ((p_2/100) * v_x)))/(v_1 + v_x)) * 100
    a = round(a,1)
    if a == p_f:
        print('For a final abv of %.1f percent add %.0f millilitres of the fortifying spirit for a total volume of %.0f millilitres.' % (a, v_x, v_x + v_1))
    else:
        print('Test failed, please review your inputs')