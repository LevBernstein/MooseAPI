# Moose API

A simple API that serves pictures of Moose, a very good dog.
Written in Python 3 with FastAPI.
Pulls pictures from the Beardless Bot repository, which also
serves Moose pictures, but in a different context.

## Installation

1. Download the repository.

2. Download [Python 3](https://python.org/downloads), and then
run `pip3 install -r resources/requirements.txt`.

## Running the API

1. Run `python3 -m uvicorn main:app --reload`

2. The API will run on localhost:8000. To get a random Moose picture,
go to localhost:8000/moose/random. To get a specific Moose picture
based on ID, go to localhost:8000/moose/ID, where ID is the ID of the
Moose picture you want to see.