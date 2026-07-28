import tkinter as tk
from tkinter import messagebox
from weather_service import get_weather

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")
        self.root.geometry("380x400")
        self.root.configure(bg="#1e1e2e")

    # Header Title

        self.title_label = tk.Label(
            root,
            text="🌤️ Weather App",
            font=("PT Serif", 18, "bold"),
            bg="#1e1e2e",
            fg="#cdd6f4"
        )

        self.title_label.pack(pady=10)

        input_frame = tk.Frame(root, bg="#1e1e2e")
        input_frame.pack(pady=10)

        self.city_entry = tk.Entry(
            input_frame,
            font=("PT Serif", 14),
            width=18,
            bd=1,
            relief="solid",
            justify="center"
        )
        self.city_entry.grid(row=0, column=0, padx=5)
        self.city_entry.insert(0,"Asunción") # Default city name
        self.city_entry.bind("<Return>", lambda event: self.fetch_weather())

        self.search_btn = tk.Button(
            input_frame,
            text="🕵️ Search",
            font=("PT Serif", 12, "bold"),
            bg="#89b4fa",
            fg="#11111b",
            activebackground="#b4befe",
            cursor="hand2",
            command=self.fetch_weather
        )
        self.search_btn.grid(row=0, column=1, padx=5)

        #Output Card Frame
        
        self.card = tk.Frame(
            root,
            bg="#313244",
            bd=2,
            relief="groove"
        )
        self.card.pack(pady=15,padx=20, fill="both", expand=True)

        self.location_label = tk.Label(
            self.card, 
            text="", 
            font=("PT Serif", 16, "bold"),
            bg="#313244",
            fg="#cdd6f4"
        )
        self.location_label.pack(pady=(15, 5))

        self.temp_label = tk.Label(
            self.card,
            text="--°C",
            font =("PT Serif", 36, "bold"),
            bg="#313244",
            fg="#89b4fa"
        )
        self.temp_label.pack(pady=5)

        self.condition_label = tk.Label(
            self.card,
            text="--",
            font=("PT Serif", 14, "bold"),
            bg="#313244",
            fg="#a6adc8"
        )
        self.condition_label.pack(pady=5)

        self.details_label = tk.Label(
            self.card,
            text="Feels like: --°c\nHumidity: --%\nWind Speed: --m/s",
            font=("PT Serif", 12),
            bg="#313244",
            fg="#cdd6f4",
            justify="center"
        )
        self.details_label.pack(pady=(10, 15))

        # Status Label

        self.status_label = tk.Label(
            root, 
            text="Enter a city name to get weather info",
            font=("PT Serif", 10),
            bg="#1e1e2e",
            fg="#a6adc8"
        )
        self.status_label.pack(side="bottom", pady=10)

    def fetch_weather(self):
        city = self.city_entry.get().strip()

        if not city:
            messagebox.showarning("Warning:", "Please enter a city name.")
            return

        # Update status while fetching
        self.status_label.config(
            text="Fetching weather data...",
            fg="#f9e2af"
            )
        self.root.update_idletasks()
        weather_data = get_weather(city)

        if "error" in weather_data:
            self.status_label.config(
                text="Error fetching data.",
                fg="#f38ba8"
            )
            messagebox.showerror("Error", weather_data["error"])
        else:
            self.location_label.config(text=f"{weather_data['city']}, {weather_data['country']}")
            self.temp_label.config(text=f"{weather_data['temp']}°C")
            self.condition_label.config(text=weather_data['description'])

            details_text = (
                f" Feels like: {weather_data['feels_like']}°C\n"
                f" Humidity: {weather_data['humidity']}%\n"
                f" Wind Speed: {weather_data['wind_speed']} m/s"
            )
            self.details_label.config(text=details_text)
            self.status_label.config(
                text="Updated successfully.",
                fg="#a6e3a1"
                )

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()