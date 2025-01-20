def run(stock: dict, merch: str, amount: int) -> bool:
    available = True
    for _ in stock:
        if merch in stock and stock.get(merch) >= amount:
            available = True
        else:
            available = False
            break
        if stock.get(merch) < amount:
            available = False
    return available


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
