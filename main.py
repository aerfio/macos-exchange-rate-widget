import rumps
import requests

EXEC_TIMER = 60  # refresh every 60 seconds

url = 'https://api.exchangerate.host/latest'

def getEuroPLNRate():
        response = requests.get(url, params={'symbols': "PLN", "places": "3" })
        data = response.json()["rates"]["PLN"]
        return str(data)

class CurrencyTicker(rumps.App):
    @rumps.timer(EXEC_TIMER)
    def pull_data(self, _):
        self.title = getEuroPLNRate()

if __name__ == "__main__":
    CurrencyTicker(getEuroPLNRate()).run() #debug=True