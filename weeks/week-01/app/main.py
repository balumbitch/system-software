from fastapi import FastAPI, HTTPException
from coursekit.variant import load_variant

_cfg = load_variant("01")
RESOURCE = _cfg["resource"]

app = FastAPI()
_store: dict[int, dict] = {}
_next_id = 1


@app.post(f"/{RESOURCE}", status_code=201)
def create_item(body: dict):
    global _next_id
    item_id = _next_id
    _next_id += 1
    item = {"id": item_id, **body}
    _store[item_id] = item
    return item


@app.get(f"/{RESOURCE}/{{item_id}}")
def get_item(item_id: int):
    if item_id not in _store:
        raise HTTPException(status_code=404, detail="Not found")
    return _store[item_id]
