#!/bin/bash

kill -9 $(lsof -ti :5001)
python app.py