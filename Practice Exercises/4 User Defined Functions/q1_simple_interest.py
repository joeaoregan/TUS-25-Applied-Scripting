def calc_final_amount(interest_rate, years, principal=100):
    final_amount = principal * (1 + (interest_rate * years / 100))
    return final_amount