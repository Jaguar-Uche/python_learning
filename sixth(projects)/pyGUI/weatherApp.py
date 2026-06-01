
import sys
import requests
from PyQt5.QtWidgets import QWidget,QApplication, QLabel, QLineEdit, QPushButton,QVBoxLayout
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter City Name",self)
        self.city_input  = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather",self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        # Set stylesheet

        # The font for displaying emojis font-family: Segoe UI emoji;

        self.city_label.setObjectName('city_label')
        self.city_input.setObjectName('city_input')
        self.get_weather_button.setObjectName('get_weather_button')
        self.temperature_label.setObjectName('temperature_label')
        self.emoji_label.setObjectName('emoji_label')
        self.description_label.setObjectName('description_label')


        self.setStyleSheet("""
            QLabel{
                font-family: calibri;
                
            }
            QLabel#city_label{
                font-size:40px;
                font-style:italic;
                   
            }
            QLabel#temperature_label{
                font-size:75px;
            }
            QLabel#emoji_label{
                font-size:100px;
                font-family: Segoe UI emoji;
            }
            QLabel#description_label{
                font-size:50px;
            }
            QLineEdit#city_input{
                font-size: 40px;
            }
            QPushButton#get_weather_button{
                font-size: 30px;
                font-weight:bold;
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = '5e4646dc3f7b3ab314a7d6069d32acd5'
        city = self.city_input.text()
        self.city_input.setText("")
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            # try block does not raise exceptions if there is a status code error so we manually raise exceptions like this
            response.raise_for_status()
            data = response.json()

            if data['cod'] == 200:
                self.display_weather(data)
        except requests.exceptions.HTTPError as httperror:
            # httperror is when the status code is not 200
            match response.status_code:
                case 400:
                    self.display_error("Bad Request:\nPlease Check Your input")
                case 401:
                    self.display_error("Unauthorized:\nInvalid API Key")
                case 403:
                    self.display_error("Forbidden:\nAccess Denied")
                case 404:
                    self.display_error("Not Found:\nCity Not Found")
                case 500:
                    self.display_error("Internal Server Error:\nPlease Try Again Later")
                case 502:
                    self.display_error("Bad Gateway:\nnvalid response from the server")
                case 503:
                    self.display_error("Service Unavailable:\nServer is down")
                case 504:
                    self.display_error("Gateway Timeout:\nNo Response from the server")
                case _:
                    self.display_error(f"HTTP Error Occured:\n{httperror}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck Your Internet Connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe Request timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too Many Redirects:\nCheck the url")
        except requests.exceptions.RequestException as req_error:
            # Network problems or invalid url
            self.display_error(f"Request Error:\n{req_error}")

    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size:30px")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size:75px")
        temperature_k = data['main']['temp']
        temperature_c = temperature_k - 273.15
        temperature_f = (temperature_k * 9/5)-459.67
        weather_id = data['weather'][0]['id']
        weather_description = data['weather'][0]['description']

        self.temperature_label.setText(f"{temperature_c:.0f}degC")
        self.description_label.setText(weather_description)
        self.emoji_label.setText(self.get_weather_emoji(weather_id))

    @staticmethod
    def get_weather_emoji(weather_id):
        if  200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "🌥️"
        elif 500 <= weather_id <= 531:
            return "🌦️"
        elif 600 <= weather_id <= 622:
            return "❄️"
        elif 701 <= weather_id <= 741:
            return "🌫️"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id <= 804:
            return "☁️"
        else:
            return ""

if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())