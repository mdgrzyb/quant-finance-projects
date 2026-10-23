import numpy as np
import matplotlib as pyplot
from scipy.stats import norm

def options_pricing(SP_0, strike, interest_rate, volatility, maturity, option_type):
    n_d1 = (np.log(SP_0/strike) + (interest_rate + 0.5*volatility**2)*maturity)/(volatility * np.sqrt(maturity))
    n_d2 = n_d1 - volatility * np.sqrt(maturity)

    if option_type == "Call":
        call_price = SP_0*norm.cdf(n_d1)- strike * np.exp(-interest_rate*maturity)*norm.cdf(n_d2)
        return call_price
    elif option_type == "Put":
        put_price = strike * np.exp(-interest_rate*maturity)*norm.cdf(-n_d2) - SP_0*norm.cdf(-n_d1)
        return put_price
    else:
        raise ValueError

print(options_pricing(100,110, 0.03, .15, 2, "Call"))