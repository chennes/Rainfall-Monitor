
# Weather API: A simple app for learning Python
#
# This program downloads the latest forecast for Norman, OK and stores it in a couple
# of lists suitable for processing with matplotlib
#
# Copyright 2022 Pioneer Library System
#
# LICENSE: BSD 3-Clause
#
# Redistribution and use in source and binary forms, with or without modification, are 
# permitted provided that the following conditions are met:
#
#   1. Redistributions of source code must retain the above copyright notice, this list 
#      of conditions and the following disclaimer.
#   2. Redistributions in binary form must reproduce the above copyright notice, this 
#      list of conditions and the following disclaimer in the documentation and/or other 
#      materials provided with the distribution.
#   3. Neither the name of the copyright holder nor the names of its contributors may be 
#      used to endorse or promote products derived from this software without specific 
#      prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY 
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF 
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL 
# THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, 
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, 
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, 
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF 
# THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import requests
import json

import matplotlib.pyplot as plt
import numpy as np

LATITUDE = 35.22
LONGITUDE = -97.44
WEATHER_API_START_URL = f"https://api.weather.gov/points/{LATITUDE},{LONGITUDE}"

if __name__ == "__main__":
    r = requests.get(WEATHER_API_START_URL)
    results = json.loads(r.text)
    forecast_url = results["properties"]["forecast"]
    r = requests.get(forecast_url)
    results = json.loads(r.text)
    forecast = results["properties"]["periods"]

    labels = []
    temperatures = []
    for entry in forecast:
        labels.append(entry["name"])
        temperatures.append(entry["temperature"])

