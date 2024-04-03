from flask import Flask, request, jsonify
import requests

if __name__ == '__main__':
    # выполняем POST-запрос на сервер по эндпоинту add с параметром json
    """r = requests.post('http://localhost:5000/add', json={'propertyType':'others',
                                                         'state':'FL',
                                                         'status':'Active',
                                                         'bath_new':2,
                                                         'beds_new':3,
                                                         'sqft_new':2203,
                                                         'Total Population':178587,
                                                         'year_new':2008,
                                                         'sc_ra':4,
                                                         'sc_di':0.5})
    r = requests.post('http://localhost:5000/add', json={'propertyType':'Single home',
                                                         'state':'TX',
                                                         'status':'others',
                                                         'bath_new':3,
                                                         'beds_new':4,
                                                         'sqft_new':2454,
                                                         'Total Population':2298628,
                                                         'year_new':1982,
                                                         'sc_ra':4,
                                                         'sc_di':0.5})"""
    r = requests.post('http://localhost:5000/add', json={'propertyType':'others',
                                                         'state':'FL',
                                                         'status':'Active',
                                                         'bath_new':2,
                                                         'beds_new':3,
                                                         'sqft_new':3158,
                                                         'Total Population':69947,
                                                         'year_new':1998,
                                                         'sc_ra':10,
                                                         'sc_di':2.2})
    #others	FL	Active	2.0	3.0	3158.0	69947.0	1998.0	10.0	2.2   - 699000
    #Single home	TX	others	3.0	4.0	2454.0	2298628.0	1982.0	4.0	0.70 - 	168800
    # выводим статус запроса
    print(r.status_code)
    # реализуем обработку результата
    if r.status_code == 200:
        # если запрос выполнен успешно (код обработки=200),
        # выводим предсказание цены на экран
        print(r.json())
    else:
        # если запрос завершён с кодом, отличным от 200, выводим содержимое ответа
        print(r.text)
        
