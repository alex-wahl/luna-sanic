from sanic.response import json
from sanic.response import text
from sanic import Blueprint
# from app.luna.supply import main

luna_v1 = Blueprint("luna_v1", url_prefix="/supply", version=1)
luna_v2 = Blueprint("luna_v2", url_prefix="/supply", version=2)


@luna_v1.route("/")
async def luna_root(request):
    return json({"my": "blueprint"})


@luna_v1.route("/test")
async def test(request):
    # main()
    return text("OK")


@luna_v2.route("/test")
async def test(request):
    # main()
    return text("OK")
