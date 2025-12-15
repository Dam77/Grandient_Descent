import numpy as np

def gradiant_descent(f, theta, t, h=1e-5):
    """
    Perform gradient descent.
    f: function to minimize
    theta: initial parameters
    t: indice of theta (ex: 0 for theta_0, 1 for theta_1)
    h: Step to approximate the gradient (default 1e-5) (derivative step) (fundamental definition of derivative)
    """
    theta_plus = np.copy(theta)
    theta_plus[t] = theta[t] + h

    theta_minus = np.copy(theta)
    theta_minus[t] = theta[t] - h

    # Calculating the derivative
    # f'(x) = (f(x + h) - f(x - h)) / (2h)
    # So : f(theta_plus) - f(theta_minus)) / (2h)
    f_plus = f(theta_plus)
    f_minus = f(theta_minus)

    gradient_approx = (f_plus - f_minus) / (2*h)

    ## NOT FINISHED YET


    










if __name__ == "__main__":
