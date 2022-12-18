import requests
import smtplib
import time
from datetime import datetime
# from pprint import pprint


URL = "http://api.open-notify.org/iss-now.json"

vallila = 60.194290, 24.956970  # from latlong.net

MY_LAT = vallila[0]  # Your latitude
MY_LONG = vallila[1]  # Your longitude

MY_EMAIL = "victorgrinan@gmail.com"
MY_PASSWORD = "ElMismisimo84"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

text = f"""
Dear myself:
The position of the ISS sattelite is close too your position and is dark outside, you might see it in the sky.
myself
"""


# find the position of the satelite and return true if close
def iss_position():
    response = requests.get(url=URL)
    response.raise_for_status()
    data = response.json()
    # pprint(data)

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


# find the sunrise and sunset of your position, return true if is dark now
def is_night():  # in my location, the API doesnt returns results anymore
    response = requests.get(URL, params=parameters)
    response.raise_for_status()
    data = response.json()

    # pprint(data)

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # print(sunrise)
    # print(sunset)

    time_now = datetime.now().hour

    if time_now >= sunset <= sunrise:
        return True


while True:
    time.sleep(300)  # 5 mins, time in seconds
    if iss_position() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_LAT,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Look up!\n\n{text}"
        )
