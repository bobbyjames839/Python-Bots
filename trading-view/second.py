'''from datetime import datetime
from sanic import Sanic 
from sanic import response 
from ib_insync import *

app = Sanic(__name__)
app.ctx.ib = None

@app.route('/')
async def root(request):
    return response.text('online')

async def checkIfReconnect():
    if not app.ctx.ib.isConnected() or not app.ctx.ib.client.isConnected():
        app.ctx.ib.disconnect()
        app.ctx.ib = IB()
        app.ctx.ib.connect('127.0.0.1', 7496, clientId=1)

if __name__ == '__main__':
    app.ctx.ib = IB()
    app.ctx.ib.connect('127.0.0.1', 7496, clientId=1)
    app.run(port=5000)'''