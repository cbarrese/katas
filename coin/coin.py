amount_and_denominations = input("Enter map of amount and denoms:")


def find_ways_to_change_amount(amount, denominations):
    ways_to_make_change = []
    for current_index, denomination in enumerate(denominations):
        for number_of_coins in range(1, (amount // denomination) + 1):
            coins = [denomination] * number_of_coins
            if sum(coins) == amount:
                ways_to_make_change.append(coins)
            else:
                remaining_change_options = find_ways_to_change_amount(amount - (denomination * number_of_coins),
                                                                      denominations[0:current_index])

                for remaining_change_option in remaining_change_options:
                    change_option = coins + remaining_change_option
                    if sum(change_option) == amount:
                        ways_to_make_change.append(change_option)

    return ways_to_make_change

change = find_ways_to_change_amount(amount_and_denominations["amount"],
                                    amount_and_denominations["denoms"])

print change
