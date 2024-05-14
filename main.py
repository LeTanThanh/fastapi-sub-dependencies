from fastapi import FastAPI
from fastapi import Depends
from fastapi import Cookie
from fastapi import Query

from typing import Annotated

app = FastAPI()

# Sub-dependencies
def query_extractor(query: Annotated[str | None, Query()] = None):
  return query

def query_or_cookie_extractor(
  query: Annotated[str, Depends(query_extractor)],
  last_query: Annotated[str | None, Cookie()] = None
):
  if not query:
    return last_query

  return query

@app.get("/query")
async def read_query(query_or_cookie: Annotated[str, Depends(query_or_cookie_extractor)]):
  return {"query_or_cookie": query_or_cookie}
