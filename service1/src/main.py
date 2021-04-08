import falcon
import requests

class HelloWorldResource:

    def on_get(self, request, response):

        response.media = ('Hello World from Falcon Python with' +
                          ' Gunicorn running in an Alpine Linux container.' +
                          ' this is SERVICE1')

        p = requests.get('http://service2')

        with open('container_data/myfile.txt', 'a') as txtfile:
            txtfile.write(p.text + '\n')


app = falcon.API()
app.add_route('/', HelloWorldResource())
