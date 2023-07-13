def submit_order(instrument, quantity):
    try:
        sup = inventory[instrument]
        if sup < quantity:
            raise OutOfStockError(quantity) # ! Не создан класс ошибки
        inventory[instrument] -= quantity
        print('Successfully placed order! Remaining supply: ' + str(inventory[instrument]))
    except OutOfStockError as err:
        print(err)


instrument = 'Guitar'
quantity = 5
submit_order(instrument, quantity)