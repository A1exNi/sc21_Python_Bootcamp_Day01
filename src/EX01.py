import EX00 as lib

def add_ingot_by_value(purse: dict[str, int], value: int):
    new_purse = purse.copy()
    new_purse.setdefault('gold_ingots', 0)
    new_purse['gold_ingots'] += value
    return new_purse

def fill_purses(sum_ingots: int):
    ingots_for_add = sum_ingots // 3
    purse1 = add_ingot_by_value(dict(), ingots_for_add)
    purse2 = add_ingot_by_value(dict(), ingots_for_add)
    purse3 = add_ingot_by_value(dict(), ingots_for_add)
    rest_of_ingots = sum_ingots % 3
    if rest_of_ingots == 1:
        purse1 = lib.add_ingot(purse1)
    elif rest_of_ingots == 2:
        purse1 = lib.add_ingot(purse1)
        purse2 = lib.add_ingot(purse2)
    return purse1, purse2, purse3
    

def split_booty(*purses):
    sum_ingots = 0
    for purse in purses:
        if (type(purse) == type(dict())):
            number_ingots = purse.get('gold_ingots', 0)
            if number_ingots > -1:
                sum_ingots += number_ingots
    purse1, purse2, purse3 = fill_purses(sum_ingots)
    return purse1, purse2, purse3

def print_result(purse1: dict[str, int], purse2: dict[str, int],
                 purse3: dict[str, int], purses):
    print(f'    Кошельки троллей: {purse1} {purse2} {purse3}')
    print(f'    Кошельки жертв  : {purses}')

def main():
    print('========================')
    print('  Всего 6:')
    purses = [{'gold_ingots': 5, 'apple': 3}, {'gold_ingots': 1}, 3,
              {'carot': 6}, {}, {'gold_ingots', 0}, {'gold_ingots', -4}]
    purse1, purse2, purse3 = split_booty(
        purses[0], purses[1], 1, purses[2],
        purses[3], purses[4], purses[5], purses[6])
    print_result(purse1, purse2, purse3, purses)
    print('------------------------')

    print('  Всего 7:')
    purses = [{'gold_ingots': 5, 'apple': 3}, {'gold_ingots': 2}, 3,
              {'carot': 6}, {}, {'gold_ingots', 0}, {'gold_ingots', -4}]
    purse1, purse2, purse3 = split_booty(
        purses[0], purses[1], 1, purses[2],
        purses[3], purses[4], purses[5], purses[6])
    print_result(purse1, purse2, purse3, purses)
    print('------------------------')

    print('  Всего 8:')
    purses = [{'gold_ingots': 5, 'apple': 3}, {'gold_ingots': 3}, 3,
              {'carot': 6}, {}, {'gold_ingots', 0}, {'gold_ingots', -4}]
    purse1, purse2, purse3 = split_booty(
        purses[0], purses[1], 1, purses[2],
        purses[3], purses[4], purses[5], purses[6])
    print_result(purse1, purse2, purse3, purses)
    print('------------------------')

    print('  Всего 9:')
    purses = [{'gold_ingots': 5, 'apple': 3}, {'gold_ingots': 4}, 3,
              {'carot': 6}, {}, {'gold_ingots', 0}, {'gold_ingots', -4}]
    purse1, purse2, purse3 = split_booty(
        purses[0], purses[1], 1, purses[2],
        purses[3], purses[4], purses[5], purses[6])
    print_result(purse1, purse2, purse3, purses)
    print('------------------------')
    
    print('  Пример из задания:')
    purses = [{"gold_ingots":3}, {"gold_ingots":2}, {"apples":10}]
    purse1, purse2, purse3 = split_booty(purses[0], purses[1], purses[2])
    print_result(purse1, purse2, purse3, purses)
    print('------------------------')

if __name__ == '__main__':
    main()