"""
Feladat:
http://www.geoplugin.net/json.gp?ip=xxx.xxx.xxx.xxx
Írjon python kliens lib-et az API-hoz.
Input: IP cím
Output: Python dict, amely tarltalmazza a következő információkat
-	Város
-	Ország
-	Régió
-	Időzóna
-	Koordináták
Szempontok:
-	Kód szervezés
-	Tesztelés
-	Error handling
-	Loggolás
"""

import configparser
import os
import logging
import re
import requests


class TestAPI:
    """
    This class handles the API calls.
    """

    def __init__(self, api):
        # Read the URL and the requested responses from the config file.
        config = configparser.ConfigParser()
        config.read(os.path.dirname(__file__) + "/conf.ini")
        self.url = config.get(api, "url")
        self.attribute = config.get(api, "response")
        self.header = {"content-type": "application/json"}

    def get_ip(self):
        """
        Read the IP address from console.
        """
        while True:
            os.system("cls")
            ip_addr = input("Please, provide a valid IP address: ")
            if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip_addr):
                input("Invalid IP format! Press enter to retype the IP...")
            else:
                break

        return ip_addr

    def get(self):
        """
        This method handles the get request
        """
        resp = {}
        try:
            response = requests.get(
                self.url + self.get_ip(), headers=self.header)

        except requests.exceptions.RequestException as error:
            raise SystemExit(error) from error

        response = response.json()

        # Browse the response to fetch only the attributes we want
        self.attribute = self.attribute.split(",")
        depth = len(self.attribute)
        for i in range(depth):
            resp.update({self.attribute[i]: response[self.attribute[i]]})

        return resp


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, filename="app.log", filemode="w")
    result = TestAPI("GEOPLUGIN").get()
    print(result)
