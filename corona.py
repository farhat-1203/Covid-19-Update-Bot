# import requests
# from win10toast import ToastNotifier
# from time import sleep

# # Replace the URL with a working endpoint
# r = requests.get('https://disease.sh/v3/covid-19/countries/france')   

# # for Country-specific data: https://disease.sh/v3/covid-19/countries/india
 

# if r.status_code == 200:  # Check if the response is successful
#     data = r.json()
#     text = f'Confirmed Cases : {data["cases"]} \nDeaths : {data["deaths"]} \nRecovered : {data["recovered"]}'

#     while True:
#         toast = ToastNotifier()
#         toast.show_toast("Covid-19 Notification", text, duration=20)
#         sleep(60)  # Notify every 60 seconds
# else:
#     print("Failed to fetch data. Please check the API or your internet connection.")


import requests
from tkinter import Tk, Label, Button, Entry, StringVar, messagebox

def fetch_covid_data():
    country = country_var.get().strip().lower()  # Get country from the input field
    url = f'https://disease.sh/v3/covid-19/countries/{country}'

    try:
        r = requests.get(url)
        r.raise_for_status()  # Raise an error for bad responses
        data = r.json()

        if "cases" in data:
            result = (f"Country: {data['country']}\n"
                      f"Confirmed Cases: {data['cases']}\n"
                      f"Today's Cases: {data['todayCases']}\n"
                      f"Deaths: {data['deaths']}\n"
                      f"Today's Deaths: {data['todayDeaths']}\n"
                      f"Recovered: {data['recovered']}\n"
                      f"Active Cases: {data['active']}")
            # Display results in a popup messagebox
            messagebox.showinfo(f"Covid-19 Update: {data['country']}", result)
        else:
            messagebox.showerror("Error", f"Data for {country} is unavailable.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch data: {e}")

# Create the main window
root = Tk()
root.title("Covid-19 Update Bot")
root.geometry("400x200")

# Input label
label = Label(root, text="Enter Country Name:", font=("Arial", 12))
label.pack(pady=10)

# Entry field for country name
country_var = StringVar()
entry = Entry(root, textvariable=country_var, font=("Arial", 12), width=30)
entry.pack(pady=5)

# Fetch button
fetch_button = Button(root, text="Get Update", font=("Arial", 12), bg="blue", fg="white", command=fetch_covid_data)
fetch_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
