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
    return [{len(mylist)}]


@app.get("/items/{item_id}")
async def get_item(item_id: int):
    if item_id >= len(mylist):
        return [{"name": "toolong", "price_in_euro": 0, "typ": "toolong"}]
    else:
        return mylist[item_id]
