from typing import Literal

import aiohttp
import re


wikipage_pattern = re.compile(r"https:\/\/en\.wikipedia\.org\/wiki\/[A-Za-z-_]{7,999}")

async def get_wikipage(ClientSession: aiohttp.ClientSession, airport_code: str) -> str:
    "Takes in an ICAO airport code and returns the wikipedia page for that airport"
    response = await ClientSession.get(f"https://ourairports.com/airports/{airport_code}")
    response_html = await response.text()

    try:
        wikipage = wikipage_pattern.findall(response_html)[0]
    except IndexError:
        return None
    except Exception as exc:
        return exc

    return wikipage


async def scrape_flights(ClientSession: aiohttp.ClientSession, airport_code: str, flight_type: Literal["arrivals", "departures"]) -> str:
    "Takes in an IATA airport code and arrival/departure, and returns flights in the current day"
    response = await ClientSession.get(f"https://www.avionio.com/widget/en/{airport_code}/{flight_type}")
    response_html = await response.text()

    if "No Flights" in response_html:
        return None

