# Moose API

from random import choice

import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse

app = FastAPI()

BASEURL = "https://{}.com/LevBernstein/moosePictures/"

@app.exception_handler(RequestValidationError)
async def validation_error_handler(*args):
	return PlainTextResponse("Invalid Moose ID!", status_code=400)


@app.get("/")
async def root():
	return {"Message": "Moose pictures here!"}


@app.get("/moose/random")
async def random_moose_picture():
	r = requests.get(BASEURL.format("github"))
	soup = BeautifulSoup(r.content.decode("utf-8"), "html.parser")
	moose = choice(
		tuple(
			m for m in soup.stripped_strings
			if m.startswith("moose") and m.endswith(".jpg")
		)
	)
	url = BASEURL.format("raw.githubusercontent") + "main/" + moose
	return {"Random Moose Picture": url}

@app.get("/moose/{mooseID}")
async def moose_picture_from_ID(mooseID: int):
	url = BASEURL.format("raw.githubusercontent") + f"main/moose{mooseID}.jpg"
	r = requests.get(url)
	if r.status_code == 404:
		raise RequestValidationError(400)
	elif r.status_code != 200:
		return PlainTextResponse("Error!", status_code=r.status_code)
	return {f"Moose picture #{mooseID}": url}
