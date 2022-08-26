
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

# http://127.0.0.1:8000/send?word1=bon&word2=jour


# $IMPLODE_BEGIN
@app.get("/send")
def send(word1: str, word2: str):
    return word1+'_'+word2
# $IMPLODE_END


@app.get("/")
def root():
    # $CHA_BEGIN
    return dict(greeting="Hello")
    # $CHA_END
