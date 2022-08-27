
# $WIPE_BEGIN
from datetime import datetime
import pytz

import pandas as pd

#from taxifare.interface.main import pred

# $WIPE_END

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# http://0.0.0.0:8000/send?word1=bon&word2=jour #en local avec la commande docker run -e PORT=8000 -p 8000:8000 --env-file .env $IMAGE
# https://project-zero-service-cis7jmkfja-ew.a.run.app/send?word1=bon&word2=jour # sur GCR

# $IMPLODE_BEGIN
@app.get("/send")
def send(word1: str, word2: str):
    return word1+'_'+word2
# $IMPLODE_END

# http://0.0.0.0:8000 #en local avec la commande docker run -e PORT=8000 -p 8000:8000 --env-file .env $IMAGE

@app.get("/")
def root():
    # $CHA_BEGIN
    return dict(greeting="Hello")
    # $CHA_END
