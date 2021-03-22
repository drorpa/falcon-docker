import falcon


class HelloWorldResource:

    def on_get(self, request, response):

        response.media = ('Hello World from Falcon Python with' +
                          ' Gunicorn running in an Alpine Linux container.' +
                          ' this is SERVICE1')

        p = request.params.get('write')
        if p is None:
            p = 'no input'

        with open('container_data/myfile.txt', 'a') as txtfile:
            txtfile.write(p + '\n')


app = falcon.API()
app.add_route('/', HelloWorldResource())
