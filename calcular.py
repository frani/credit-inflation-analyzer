import locale

def calculate_discounted_value_with_inflation(credit_price, inflation_rate, periods):
    # Calculate the present value discount of the price bought with credit, considering inflation and periods (installments)
    installment = credit_price / periods
    monthly_inflation_rate = ((1 + inflation_rate / 100) ** (1 / 12))
    discount = 0
    for period in range(periods):
        discount += installment / (monthly_inflation_rate ** period)
    return discount

def calculate_capital_yield(credit_price, annual_yield, periods):
    # Calculate the present value discount of the price bought with credit, considering inflation and periods (installments)
    installment = credit_price / periods
    monthly_yield = ((1 + annual_yield / 100) ** (1 / 12))
    remaining_capital = credit_price
    yield_amount = 0
    for _ in range(periods):
        yield_amount += remaining_capital * (monthly_yield - 1)
        remaining_capital *= monthly_yield
        remaining_capital -= installment 
    return yield_amount

def calculate_interest_rate(credit_price, cash_price, periods):
    # Calculate the credit interest rate
    interest_rate = ((credit_price / cash_price) ** (1 / periods) - 1) * 12 * 100
    return interest_rate

def main():
    # Set local configuration for currency format
    locale.setlocale(locale.LC_ALL, '')

    # Request user inputs
    annual_inflation = float(input("Enter the expected annual inflation rate (%): "))
    annual_yield = float(input("Enter the expected annual investment yield rate (%): "))
    cash_price = float(input("Enter the price of the product bought in cash: "))
    credit_price = float(input("Enter the final price of the product bought on credit: "))
    periods = int(input("Enter the number of periods for the credit: "))

    # Calculate monthly inflation
    monthly_inflation = ((1 + annual_inflation / 100) ** (1 / 12) - 1) * 100
    monthly_yield = ((1 + annual_yield / 100) ** (1 / 12) - 1) * 100

    # Calculate credit interest rate
    credit_interest_rate = calculate_interest_rate(credit_price, cash_price, periods)

    # Calculate discounted value with inflation
    discounted_value = calculate_discounted_value_with_inflation(credit_price, annual_inflation, periods)
    
    # Calculate potential yields from idle capital (not spent on credit)
    yield_amount = calculate_capital_yield(credit_price, annual_yield, periods)

    # Format monetary values
    cash_price_format = locale.currency(cash_price, grouping=True)
    credit_price_format = locale.currency(credit_price, grouping=True)
    installment_format = locale.currency(credit_price / periods, grouping=True)
    discounted_value_format = locale.currency(discounted_value, grouping=True)
    yield_amount_format = locale.currency(yield_amount, grouping=True)
    final_cost_format = locale.currency(discounted_value - yield_amount, grouping=True)

    # Print results
    print("\nInformation about the credit purchase:")
    print("")
    print("Annual Yield (%):", "{:.2f}%".format(annual_yield))
    print("Monthly Yield (%):", "{:.2f}%".format(monthly_yield))
    print("Annual Inflation (%):", "{:.2f}%".format(annual_inflation))
    print("Monthly Inflation (%):", "{:.2f}%".format(monthly_inflation))
    print("")
    print("Cash price:", cash_price_format)
    print("Final price with credit:", credit_price_format)
    print("Price per installment:", installment_format)
    print("Credit interest rate (%):", "{:.2f}%".format(credit_interest_rate))
    print("")
    print("The discounted present value of the purchase with credit, considering inflation is:", discounted_value_format)
    print("The total yield earned is:", yield_amount_format)
    print("Real final cost:", final_cost_format)

if __name__ == "__main__":
    main()
