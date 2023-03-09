import requests
import datetime
import boto3


def get_url():
    return ('https://casas.mitula.com.co/'
            'searchRE/nivel3-Chapinero/'
            'nivel2-Bogot%C3%A1/'
            'nivel1-Cundinamarca/'
            'q-Bogot%C3%A1-Chapinero')


def get_bucket():
    return 'landing-casas-salazar-bermudez'


def lambda_handler():

    s3 = boto3.resource('s3')
    url = get_url()
    bucket = get_bucket()
    response = requests.get(url)
    scraped_html = response.content
    today = datetime.date.today()
    file_name = today.strftime("%Y-%m-%d") + ".html"
    s3.Bucket(bucket).put_object(
        Key=file_name, Body=scraped_html)
    return {
        'statusCode': 200,
        'body': 'Contenido HTML guardado como ' + file_name
    }
