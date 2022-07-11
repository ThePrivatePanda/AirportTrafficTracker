import requests


data = {
    "qtype": "cpi",
    "sfw": "/FV/Home/Main",
    "namdep": "PNQ Pune, India - Pune Airport",
    "depap": "PNQ",
    "namarr": "DEL New Delhi, India - Indira Gandhi International",
    "arrap": "DEL",
    "namal2": "Enter name or code",
    "al": "",
    "whenArrDep": "dep",
    "whenHour": "all",
    "whenDate": "20230606",
    "input": "Track Flight",
}

r = requests.post("https://www.flightview.com/TravelTools/FlightTrackerQueryResults.asp", params=data)
print(r.content)