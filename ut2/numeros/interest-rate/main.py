def run(amount: float, rate: float, years: int) -> float:
    rate_operation = (1 + rate / 100) ** years
    future_amount = amount * rate_operation
    return future_amount


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
