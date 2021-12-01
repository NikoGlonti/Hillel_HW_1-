def parse(query: str) -> dict:
    response = dict()
    my_query = query.split('?', 1)  # сплитим входящую строку по ? знак
    try:
        temp_str = ''.join(my_query[1])  # создаем новую строку и отбрасываемы все что было до ?
    except IndexError:
        return {}

    temp_query = temp_str.split('&')  # и снова сплитим нашу новую строку по &
    for i in temp_query:  # в цикле перебираем наш результат сплитим и записывем в словарь ключ значения
        temp = i.split('=')
        try:
            response[temp[0]] = temp[1]
        except IndexError:
            continue
    res = {k: v for k, v in response.items() if k}  # исключаем возможность записи пустого ключа
    return res


print(parse('https://example.com/path/to/page?name=ferret&color=purple'))

if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('http://example.com/?&&&') == {}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}


def parse_cookie(query: str) -> dict:
    my_dict = dict()
    my_query = query.split(';')  # сплитим входную строку по ;
    for i in my_query:  # перебираем и сплитим по первому вхождению = записывая в словарь ключ значения
        temp = i.split('=', 1)
        try:
            my_dict[temp[0]] = temp[1]
        except IndexError:
            continue
    res = {k: v for k, v in my_dict.items() if k}  # исключаем возможность пустых ключей
    return res


print(parse_cookie('name=Dima;age=28;'))


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=Dima=User;;age=28;;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('dfvdfsdsds') == {}

