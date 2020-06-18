import requests
def calc_age(uid):
    import requests
    import datetime
    now_date = datetime.datetime.now().year
    token = 'f8f9d7d5f8f9d7d5f8f9d7d517f88b70d4ff8f9f8f9d7d5a613c4f7641c6eb643203720'
    V = '5.71'
    id = uid

    r = requests.get('https://api.vk.com/method/users.get', params = {
        'access_token': token,
        'user_ids': id,
        'v': V
    })

    id = r.json()['response'][0]['id']

    f = requests.get('https://api.vk.com/method/friends.get', params = {
        'user_id': id,
        'v': V,
        'access_token': token,
        'fields': 'bdate'
    })

    otvet = d = {a: 0 for a in range(110)}
    dic_json_frienfs = f.json()['response']['items']
    for item in dic_json_frienfs:
        date = item.get('bdate')
        if date:
            a = date.split(".")
            if len(a) == 3:
                age = now_date - int(a[2])
                otvet[age] = otvet[age] + 1
    my_list = []
    for item in otvet:
        if otvet[item] > 0:
            my_list.append((item, otvet[item]))

    print(my_list)
    sort = sorted(my_list, key = lambda a: a[1], reverse=True )
    return sort


if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)
