def complete_square(b, c):

    if (-c + (b/2)**2) >= 0:
        std = ('(x + {:.2f})^2 = {:.2f}'.format(b/2, -c + ((b/2)**2)))
        roots = 'Roots: {:.2f} and {:.2f}'.format(-b/2 + (-c + ((b/2)**2))**0.5, -b/2 - (-c + ((b/2)**2))**0.5)
        return roots
    
    else:
        root1 = -b/2 + (c + ((b/2)**2))**0.5
        roots = 'Roots: {} +- {:.2f}i'.format(-b/2, (c + ((b/2)**2))**0.5)
        return roots