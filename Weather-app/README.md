# 🌤️ Weather Dashboard 
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![Licence:MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
---
A simple interactive dashboard that shows the current weather in different cities around the globle! 🌎🌏🌍

## 🌟 Features
* **Real-time Weather Metrics:** Live updates for temperature, humidity, wind speed and weather condition descriptions.
* **City Search:** Search weather metrics for any city globally.
* **Interactive GUI:** Built with Python's Tkinder framework, featuring dynamic status loading bars and clean visual indicators.
* **Error Handling:** Handles invalid city inputs, missing network connections, and API rate limits gracefully.
---
## 🏃⚡ Quick Start
### Prerequisites
* **Python 3.10** installed on your machine.
* A free **OpenWeatherMap API keys** (get one at [openweathermap.org](https://openweathermap.org/api)).

### Installation
1. Clone:
```bash
git clone https://github.com/ChavezCoder/Python-Proyects.git
cd Python-Proyects/Weather-app
```

2. **Create a virtual environment (recommended):**
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. **Install required dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set up your API Key:**
   - Create a `.env` file in the project root directory:
   ```
   OPENWEATHER_API_KEY=your_api_key_here
   ```
   - Replace `your_api_key_here` with your actual OpenWeatherMap API key

5. **Run the application:**
```bash
python weather_app.py
```

The Weather Dashboard will open in a new window. Enter a city name and click "Search" to view weather information!

---
## 📖 Usage
1. Launch the application
2. Enter a city name in the search field
3. Click the "Search" button or press Enter
4. View real-time weather data including:
   - Current temperature (°C/°F)
   - Humidity percentage
   - Wind speed
   - Weather condition description
5. Search for as many cities as you want!

---
## ⚙️ Configuration
- **Temperature Units:** Modify the API call in the code to switch between Celsius and Fahrenheit
- **API Timeout:** Adjust the request timeout in the settings for slow connections
- **Theme Colors:** Customize the GUI colors in the configuration section

---
## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| "API Key not found" | Ensure your `.env` file exists and contains your valid API key |
| "City not found" | Check spelling and try searching for a major city |
| "Network error" | Verify your internet connection and firewall settings |
| "API rate limit exceeded" | Wait a few minutes before making new requests |

---
## 📦 Dependencies
- `tkinter` - GUI framework (included with Python)
- `requests` - HTTP requests library
- `python-dotenv` - Environment variable management
- `pytz` - Timezone support

---
## 📄 License
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---
## 👨‍💻 Author
Created by **ChavezCoder**

---
## 🤝 Contributing
Contributions are welcome! Feel free to fork this repository and submit pull requests.

## ☎️ Support
If you encounter any issues or have suggestions, please open an issue on the [GitHub repository](https://github.com/ChavezCoder/Python-Proyects/issues).

Happy coding! 🚀
