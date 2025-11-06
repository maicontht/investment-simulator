from renda_fixa import renda_fixa


tax_ir = {
    '180': 22.5,
    '360': 20.0,
    '720': 17.5,
    'above_720': 15.0
}

def get_aliquota(months: int) -> float:
    """Returns the income tax rate according to the time period in months."""
    days = months * 30  
    
    if days <= 180:
        return tax_ir['180'] / 100
    if days <= 360:
        return tax_ir['360'] / 100
    if days <= 720:
        return tax_ir['720'] / 100
    else:
        return tax_ir['above_720'] / 100
    







