# Input Section
dblTotalTaxableAmount = 1500000
strTaxRegimeType = "NEW" # Choices:- "OLD", "NEW"

intBalanceMonth = 12
dblNewRegimeTotalTaxableAmount = 2092000

# OLD REGIME Fn
def calculate_old_regime_tax(dblTaxableAmount):

    dblTaxAmount = 0

    if dblTaxableAmount <= 500000:
        pass
    else:
        dblTaxAmount = 12500 # Slab 1 (5%)
    
    if dblTaxableAmount >= 500001:
        if dblTaxableAmount >= 1000000:
            dblTaxAmount += 100000
        else:
            dblSlabAmount = dblTaxableAmount - 500000
            dblTaxAmount += (dblSlabAmount * 20) / 100  # Slab 2 (20%)
        pass

    if dblTaxableAmount >= 1000001:
        dblSlabAmount = dblTaxableAmount - 1000000
        dblTaxAmount += (dblSlabAmount * 30) / 100 # Slab 3 (30%)
        pass

    # Cess (4% of total tax)
    dblTaxAmount += (dblTaxAmount * 4) / 100

    return dblTaxAmount

# NEW REGIME Fn
def calculate_new_regime_tax(dblTaxableAmount):

    dblTaxAmount = 0

    # Slab 1 (5%)
    if dblTaxableAmount >= 250001:
        if dblTaxableAmount >= 500000:
            dblTaxAmount += 12500
        else:
            dblSlabAmount = dblTaxableAmount - 250000
            dblTaxAmount += (dblSlabAmount * 5) / 100
        pass
    print("1 :",dblTaxAmount)
    # Slab 2 (10%)
    if dblTaxableAmount >= 500001:
        if dblTaxableAmount >= 750000:
            dblTaxAmount += 25000
        else:
            dblSlabAmount = dblTaxableAmount - 500000
            dblTaxAmount += (dblSlabAmount * 10) / 100
        pass
    print("2 :", dblTaxAmount)
    # Slab 3 (15%)
    if dblTaxableAmount >= 750001:
        if dblTaxableAmount >= 1000000:
            dblTaxAmount += 37500
        else:
            dblSlabAmount = dblTaxableAmount - 750000
            dblTaxAmount += (dblSlabAmount * 15) / 100
        pass
    print("3 :", dblTaxAmount)
    # Slab 4 (20%)
    if dblTaxableAmount >= 1000001:
        if dblTaxableAmount >= 1250000:
            dblTaxAmount += 50000
        else:
            dblSlabAmount = dblTaxableAmount - 1000000
            dblTaxAmount += (dblSlabAmount * 20) / 100
        pass
    print("4 :", dblTaxAmount)
    # Slab 5 (25%)
    if dblTaxableAmount >= 1250001:
        if dblTaxableAmount >= 1500000:
            dblTaxAmount += 62500
        else:
            dblSlabAmount = dblTaxableAmount - 1250000
            dblTaxAmount += (dblSlabAmount * 25) / 100
        pass
    print("5 :", dblTaxAmount)
    # Slab 6 (30%)
    if dblTaxableAmount >= 1500001:
        dblSlabAmount = dblTaxableAmount - 1500000
        dblTaxAmount += (dblSlabAmount * 30) / 100
        pass
    print("6 :", dblTaxAmount)
    # Cess (4% of total tax)
    dblTaxAmount += ((dblTaxAmount * 4) / 100)

    return dblTaxAmount

dblMonthlyTaxAmount, dblYearlyTaxAmount = 0.0, 0.0

# OLD REGIME
if strTaxRegimeType.upper() == "OLD":
    dblYearlyTaxAmount = calculate_old_regime_tax(dblTotalTaxableAmount)
    dblMonthlyTaxAmount = dblYearlyTaxAmount / (intBalanceMonth)


# NEW REGIME
if strTaxRegimeType.upper() == "NEW":
    dblYearlyTaxAmount = calculate_new_regime_tax(dblNewRegimeTotalTaxableAmount)
    dblMonthlyTaxAmount = dblYearlyTaxAmount / (intBalanceMonth)

print(f"""
::: START :::
    
    Total Taxable Amount = {dblTotalTaxableAmount}
    Balance Month = {intBalanceMonth}
    Tax Type = {strTaxRegimeType.capitalize()} Regime

    Yearly Tax = {dblYearlyTaxAmount}
    Monthly Tax ({intBalanceMonth} M) = {dblMonthlyTaxAmount}


::: END :::
""")
