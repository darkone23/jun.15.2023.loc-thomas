from starlette.applications import Starlette
from starlette.responses import JSONResponse, HTMLResponse
from starlette.routing import Route


import app

async def api(request):
    return JSONResponse({"hello": "world"})

async def index(request):
    return HTMLResponse(""""
        <html5>
        <head>
            <title>FlightTracker Stats5000</title>
            <!-- CDN include JS urls -->
        </head>
        <body>
            <header>
                <h1>Track your flight...</h1>
            </header>
            <form method="POST">
                <input type="number" name="year" />
                <button id="click-me">FlightStats!</button>
            </form>
        </body>            
        """)

class App:
    routes = [
        Route("/index.html", endpoint=index),
        Route("/api.json", endpoint=api)
    ]


app = Starlette(debug=True, routes=App.routes)
