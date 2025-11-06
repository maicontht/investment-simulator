from main import get_aliquota

def renda_fixa(value: float, month_rate: float, month_period: int):
    """
    value : float : initial amount invested
    month_rate : float : monthly interest rate
    month_period : int : time period in months

    return: float: final amount after the period
    """
    future_value = value
    for _ in range(month_period):
        future_value *= (1 + month_rate / 100)


    gross_gain = future_value - value
    ir_amount = gross_gain * get_aliquota(month_period)
    net_value = future_value - ir_amount
    
    print(f'You will have R$ {future_value:,.2f} gross')
    print(f'You will have R$ {net_value:,.2f} net')
