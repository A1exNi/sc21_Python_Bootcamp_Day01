import EX00 as lib

def decorator(func):
    def wrapper(*args, **kwargs):
        print('SQUEAK')
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper


def print_result(purse1: dict[str, int], purse2: dict[str, int]):
    print(f'    Первый словарь: {purse1}')
    print(f'    Второй словарь: {purse2}')

def test_empty(empty):    
    print('Test empty:')
    print('  Передали не пустой словарь:')
    purse = {'gold_ingots': 1, 'asdf': 4}
    purse2 = empty(purse)
    print_result(purse, purse2)

    print('  Передали пустой словарь:')
    purse = dict()
    purse2 = empty(purse)
    print_result(purse, purse2)

def test_add(add_ingot):
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

def test_get(get_ingot):
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
    empty = decorator(lib.empty)
    add_ingot = decorator(lib.add_ingot)
    get_ingot = decorator(lib.get_ingot)
    print('========================')
    test_empty(empty)
    print('------------------------')
    test_add(add_ingot)
    print('------------------------')
    test_get(get_ingot)
    print('------------------------')
    print('Пример из задания:')
    purse = {'gold_ingots': 4}
    purse2 = add_ingot(get_ingot(add_ingot(empty(purse))))
    print_result(purse, purse2)

if __name__ == '__main__':
    main()