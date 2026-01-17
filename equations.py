import math
import matplotlib.pyplot as plt

def linear(x, a, b):
    return [a * xi + b for xi in x]


def quadratic(x, a, b, c):
    return [a * xi**2 + b * xi + c for xi in x]


def power(x, a, b):
    return [a ** (b * xi) for xi in x]


def exponential(x, a, b):
    return [a * math.exp(b * xi) for xi in x]


def logarithmic(x, a, b):
    return [a * math.log(b * xi) for xi in x]


def compute_metrics(y, y_hat):
    E = [yi - yhi for yi, yhi in zip(y, y_hat)]
    SSE = sum(e**2 for e in E)
    R = math.sqrt(SSE) 
    return E, SSE, R



def fit_linear(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x2 = sum(xi**2 for xi in x)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))

    a = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
    b = (sum_y - a * sum_x) / n
    return a, b

def fit_quadratic(x, y):
    n = len(x)
    Sx = sum(x)
    Sx2 = sum(xi**2 for xi in x)
    Sx3 = sum(xi**3 for xi in x)
    Sx4 = sum(xi**4 for xi in x)

    Sy = sum(y)
    Sxy = sum(xi * yi for xi, yi in zip(x, y))
    Sx2y = sum(xi**2 * yi for xi, yi in zip(x, y))

    D = (
        Sx4*(Sx2*n - Sx*Sx) - Sx3*(Sx3*n - Sx*Sx2) + Sx2*(Sx3*Sx - Sx2*Sx2)
    )
    
 
    Da = (
        Sx2y*(Sx2*n - Sx*Sx) - Sxy*(Sx3*n - Sx*Sx2) + Sy*(Sx3*Sx - Sx2*Sx2)
    )
    Db = (
        Sx4*(Sxy*n - Sy*Sx) - Sx2y*(Sx3*n - Sx*Sx2) + Sx2*(Sx3*Sy - Sx2*Sxy)
    )
    Dc = (
        Sx4*(Sx2*Sy - Sx*Sxy) - Sx3*(Sx3*Sy - Sx*Sx2y) + Sx2*(Sx3*Sxy - Sx2*Sx2y)
    )

    a = Da / D
    b = Db / D
    c = Dc / D
    return a, b, c


def fit_exponential(x, y):
    n = len(x)

    Y = [math.log(yi) for yi in y]

    sum_x = sum(x)
    sum_Y = sum(Y)
    sum_x2 = sum(xi**2 for xi in x)
    sum_xY = sum(xi * Yi for xi, Yi in zip(x, Y))

    b = (n * sum_xY - sum_x * sum_Y) / (n * sum_x2 - sum_x**2)
    A = (sum_Y - b * sum_x) / n

    a = math.exp(A)
    return a, b


def fit_power(x, y):
    n = len(x)

    X = [math.log(xi) for xi in x]
    Y = [math.log(yi) for yi in y]

    sum_X = sum(X)
    sum_Y = sum(Y)
    sum_X2 = sum(Xi**2 for Xi in X)
    sum_XY = sum(Xi * Yi for Xi, Yi in zip(X, Y))

    b = (n * sum_XY - sum_X * sum_Y) / (n * sum_X2 - sum_X**2)
    A = (sum_Y - b * sum_X) / n

    a = math.exp(A)
    return a, b


def fit_logarithmic(x, y):
    X = [math.log(xi) for xi in x]
    return fit_linear(X, y)


x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 6]



def main():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 5, 4, 6]

    
    a_l, b_l = fit_linear(x, y)
    y_lin = linear(x, a_l, b_l)


    a_q, b_q, c_q = fit_quadratic(x, y)
    y_quad = quadratic(x, a_q, b_q, c_q)


    a_e, b_e = fit_exponential(x, y)
    y_exp = exponential(x, a_e, b_e)


    a_p, b_p = fit_power(x, y)
    y_pow = power(x, a_p, b_p)

    
    a_log, b_log = fit_logarithmic(x, y)
    y_log = logarithmic(x, a_log, b_log)

    
    plt.figure()
    

    plt.plot(x, y_lin, label="Linear: y = ax + b")
    plt.plot(x, y_quad, label="Quadratic: y = ax² + bx + c")
    plt.plot(x, y_exp, label="Exponential: y = a·e^(bx)")
    plt.plot(x, y_pow, label="Power: y = a·x^b")
    plt.plot(x, y_log, label="Logarithmic: y = a·ln(x) + b")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Comparison of Regression Models")
    plt.legend()   
    plt.show()


if __name__ == "__main__":
    main()
