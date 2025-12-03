def convert_euro_to_gbp(amount_eur, rate):
    """
    Convert an amount in euros to pounds using a given exchange rate.

    Parameters
    ----------
    amount_eur : float
        Amount in euros to convert.
    rate : float
        Exchange rate from euros to pounds.

    Returns
    -------
    amount_gbp : float
        Equivalent amount in pounds.

    Examples
    --------
    # These examples demonstrate floating-point precision issues with doctest:

    >>> convert_euro_to_gbp(1.0, 0.91)
    0.91
    >>> convert_euro_to_gbp(0.1, 0.87)
    0.087

    # Note: these doctests can fail, which is why in practice we use pytest.approx()
    # when testing floating-point numbers in pytest.
    """
    return amount_eur * rate

if __name__ == "__main__":
    amount = float(input("Enter the amount in Euros: "))
    rate = float(input("Enter the exchange rate (Euro to GBP): "))
    print(f"Converting {amount} in Euros to GBP: {convert_euro_to_gbp(amount, rate)}")
    # import doctest
    # doctest.testmod()