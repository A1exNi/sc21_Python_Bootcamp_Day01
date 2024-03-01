def add_ingot(purse: dict[str, int]) -> dict[str, int]:
    new_purse = purse.copy()
    new_purse.setdefault('gold_ingots', 0)
    new_purse['gold_ingots'] += 1
    return new_purse

def get_ingot(purse: dict[str, int]) -> dict[str, int]:
    new_purse = purse.copy()
    if len(purse) > 0:
        new_purse['gold_ingots'] = purse.get('gold_ingots', 0)
        if (new_purse['gold_ingots'] > 0):
            new_purse['gold_ingots'] -= 1
    return new_purse

def empty(purse: dict[str, int]) -> dict[str, int]:
    return dict()

def print_result(purse1: dict[str, int], purse2: dict[str, int]):
    print(f'    Первый словарь: {purse1}')
    print(f'    Второй словарь: {purse2}')

def test_empty():
    print('Test empty:')

    print('  Передали не пустой словарь:')
    purse = {'gold_ingots': 1, 'asdf': 4}
    purse2 = empty(purse)
    print_result(purse, purse2)

    print('  Передали пустой словарь:')
    purse = dict()
    purse2 = empty(purse)
    print_result(purse, purse2)

def test_add():
    print('Test add:')
    print('  Добавили в пустой словарь:')
    purse = dict()
    purse2 = add_ingot(purse)
    print_result(purse, purse2)

    print('  Увеличить имеющееся:')
    purse = {'gold_ingots': 4, 'asdf': 2}
    purse2 = add_ingot(purse)
    print_result(purse, purse2)

    print('  Там что то другое:')
    purse = {'asdf': 4}
    purse2 = add_ingot(purse)
    print_result(purse, purse2)

def test_get():
    print('Test get:')
    print('  Пустой:')
    purse = dict()
    purse2 = get_ingot(purse)
    print_result(purse, purse2)

    print('  Не пустой:')
    purse = {'gold_ingots': 4, 'sdf': 5}
    purse2 = get_ingot(purse)
    print_result(purse, purse2)

    print('  Нет слитка:')
    purse = {'sdf': 5}
    purse2 = get_ingot(purse)
    print_result(purse, purse2)
    

def main():
    print('========================')
    test_empty()
    print('------------------------')
    test_add()
    print('------------------------')
    test_get()
    print('------------------------')
    print('Пример из задания:')
    purse = {'gold_ingots': 4}
    purse2 = add_ingot(get_ingot(add_ingot(empty(purse))))
    print_result(purse, purse2)

if __name__ == '__main__':
    main()