from sanic import Sanic
from api.endpoints import luna_v1, luna_v2


app = Sanic(__name__)
app.blueprint(luna_v1)
app.blueprint(luna_v2)

if __name__ == '__main__':
    app.run()
