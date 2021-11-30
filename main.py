# Moose API

from random import randint

import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse

app = FastAPI()

BASEURL = "https://{}.com/LevBernstein/BeardlessBot/{}/resources/images/{}"


def meeseFinder(meese: list):
	for moose in meese:
		if moose.startswith("moose") and moose.endswith(".jpg"):
			yield int(moose[5:-4])


@app.exception_handler(RequestValidationError)
async def validation_error_handler(*args):
	return PlainTextResponse("Invalid Moose ID!", status_code=400)


@app.get("/")
async def root():
	return {"Message": "Moose pictures here!"}


@app.get("/moose/random")
async def random_moose_picture():
	r = requests.get(BASEURL.format("github", "tree/main", "moose"))
	soup = BeautifulSoup(r.content.decode("utf-8", "html.parser"))
	meese = meeseFinder(soup.stripped_strings)
	url = BASEURL.format(
		"raw.githubusercontent",
		"main",
		f"moose/moose{randint(1, max(meese))}.jpg"
	)
	return {"Random Moose Picture": url}


@app.get("/moose/{mooseID}")
async def moose_picture_from_ID(mooseID: int):
	url = BASEURL.format(
		"raw.githubusercontent", "main", f"moose/moose{mooseID}.jpg"
	)
	r = requests.get(url)
	if r.status_code == 404:
		raise RequestValidationError(400)
	elif r.status_code != 200:
		return PlainTextResponse("Error!", status_code=r.status_code)
	return {f"Moose picture #{mooseID}": url}
