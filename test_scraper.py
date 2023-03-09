from scraper import lambda_handler


def get_bucket():
    return 'test-bucket-html'
    
def get_url():
    return 'https://casas.mitula.com.co/searchRE/nivel2-Medell%C3%ADn/nivel1-Antioquia/q-Medell%C3%ADn'
    
def test_lambda_handler1():
    response1 = lambda_handler()
    assert response1['statusCode'] == 200
    assert 'Contenido HTML guardado como' in response1['body']


def test_lambda_handler2():
    response2 = lambda_handler()
    assert response2['statusCode'] == 200
    assert 'Contenido HTML guardado como' in response2['body']
    

def test_lambda_handler3():
    response3 = lambda_handler()
    assert response3['statusCode'] == 200
    assert 'Contenido HTML guardado como' in response3['body']
