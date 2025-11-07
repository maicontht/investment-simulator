from aliquota import get_aliquota

def renda_fixa(value: float, monthly_investment: float, 
               month_rate: float, month_period: int):
    """
    value : float : initial amount invested
    month_rate : float : monthly interest rate
    month_period : int : time period in months

    return: float: final amount after the period
    """
    investment_value = monthly_investment * month_period
    future_value = value
    month_gain = 0
    total_investiment = value + investment_value 
    
    for i in range(month_period):
        future_value *= ( month_rate / 100 + 1) 
        month_gain = (future_value - value) - (monthly_investment * i)
        future_value += monthly_investment
        print(f'R$ {future_value:,.2f} | gain until now: R$ {month_gain:,.2f}')


    gross_gain = future_value - total_investiment
    ir_amount = gross_gain * get_aliquota(month_period)
    net_value = future_value - ir_amount
    real_gain = net_value - total_investiment

    print(f'\nYou will have invested R$ {investment_value:,.2f} for you own pocket\n')
    print(f'You will have R$ {future_value:,.2f} gross\n')
    print(f'You will have R$ {net_value:,.2f} net\n')
    print(f'You will pay R$ {ir_amount:,.2f} in income tax\n')
    print(f'You will have R$ {real_gain:,.2f} for real gain\n')
    print(f'Income tax rate applied: {get_aliquota(month_period)*100:.2f}%\n')
    

teste = renda_fixa(1000, 100, 1, 12)