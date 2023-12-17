from fastapi import FastAPI

app = FastAPI(
    title="Trading App"
)

@app.get('/')
def hello():
  return 'hello world'
