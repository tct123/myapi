import fastapi as fa
import pydantic

mylist = [
    {"name": "Computer 1", "price_in_euro": 100, "typ": "hardware"},
    {"name": "Computer 2", "price_in_euro": 100, "typ": "hardware"},
    {"name": "Computer 3", "price_in_euro": 100, "typ": "hardware"},
    {"name": "Computer 4", "price_in_euro": 100, "typ": "hardware"},
]

app = fa.FastAPI()


@app.get("/items")
async def all_items():
    return mylist


@app.get("/itemslength")
async def all_items():
    return [{"length": len(mylist)}]


@app.get("/items/{item_id}")
async def get_item(item_id: int):
    if item_id >= len(mylist):
        return [{"name": "toolong", "price_in_euro": 0, "typ": "toolong"}]
    if item_id <= 0:
        return[{"name": "Wrong value", "price_in_euro": 0, "typ": "Wrong value"}]
    else:
        return mylist[item_id]


@app.get("/test/{myinput}")
def test(myinput):
    return {"input": myinput}
