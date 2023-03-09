from scraper import lambda_handler, get_bucket, get_url


def test_lambda_handler1():
    response1 = lambda_handler()
    assert response1['statusCode'] == 200
    assert 'Contenido HTML guardado como' in response1['body']