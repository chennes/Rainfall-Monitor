# Rainfall Monitor: A simple app for learning Python
#
# This program downloads the latest rainfall data for Norman, OK and displays the seven-day 
# total accumulation.
#
# Copyright 2021 Pioneer Library System
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

import tempfile
from html.parser import HTMLParser
import urllib.request
from urllib.error import URLError, HTTPError
from typing import List

MESONET_URL = "http://climate.ok.gov/index.php/climate/rainfall_table/local_data"

class RainfallDataExtractor(HTMLParser):
    """ A class to extract the rainfall data for a city """

    def __init__ (self, city:str):
        super().__init__()
        self.city = city

        self.in_table = False
        self.in_tbody = False
        self.in_tr = False
        self.in_td = False
        self.found_city = False
        self.rainfall_data = []

    def get_rainfall(self) -> List[float]:
        return self.rainfall_data

    def handle_starttag(self, tag, attrs):
        if tag == "table":
            self.in_table = True
        elif tag == "tbody":
            self.in_tbody = True
        elif tag == "tr":
            self.in_tr = True
        elif tag == "td":
            self.in_td = True

    def handle_endtag(self, tag):
        if tag == "table":
            self.in_table = False
        elif tag == "tbody":
            self.in_tbody = False
        elif tag == "tr":
            self.in_tr = False
        elif tag == "td":
            self.in_td = False

    def handle_data(self, data):
        if self.in_table and self.in_tbody and self.in_tr and self.in_td:
            if self.found_city:
                try:
                    data_as_float = float(data)
                    self.rainfall_data.append(data_as_float)
                except Exception:
                    # If the conversion failed, the station probably didn't report data that day, so assume zero rainfall
                    self.rainfall_data.append(0.0)
            else:
                if data == self.city:
                    self.found_city = True

webpage = ""
try:
    response = urllib.request.urlopen(MESONET_URL)
    webpage = response.read()
    webpage = webpage.decode()
except URLError as e:
    print (f"Failed to read {MESONET_URL}: {e.reason}")
except HTTPError as e:
    print (f"HTTP {e.code} error reading {MESONET_URL}: {e.reason}")
except Exception as e:
    print (f"Error reading from {MESONET_URL}: {e.reason}")

if webpage:
    parser = RainfallDataExtractor("Norman")
    parser.feed(webpage)

    rainfall = parser.get_rainfall()
    weekly_rainfall = rainfall[0]
    # Rainfall data is: 7 Day, 10 Day, 14 Day, 30 Day, 60 Day, 90 Day, Current Month, YTD, Previous Year

    print (f"This week we got {weekly_rainfall} inches of rain.")