# importing the required module t
from tkinter import *
from PIL import Image, ImageTk
import requests

# weather api
API_KEY='place your own api key here'
BASE_URL='https://api.openweathermap.org/data/2.5/weather'
# url = 'https://api.openweathermap.org/data/2.5/weather?q=city name&appid={api_key}'


# creating the main window
root=Tk()

# setting the title of the main window
root.title("Weather App")

# adding an favicon to the main window 
root.iconbitmap('favicon.ico')

# setting the minimum size of the main window
root.minsize(500,500)

# setting the background color of the main window
root.configure(background='lightblue')

# now firstly we will need to add an image on the weather app
# loading the image using PIL
img = Image.open('weather.png')

# now resizing the image
resized_img= img.resize((70,70))

# converting the image to a tkinter compatible photo image
img= ImageTk.PhotoImage(resized_img)

# creating a label to add the image
img_label = Label(root,image=img)

# now we have to place the image on the main window
img_label.pack(pady=(20,20))

# adding a label to the logo image
text_label = Label(root,text="Weather App",font=("Arial",20),bg='lightblue',fg='black')
text_label.pack()

# adding a label to take city name as input
city_label = Label(root,text="Enter City Name",font=("Arial",12),bg='lightblue',fg='black')
city_label.pack(pady=(30,10))

# adding an entry box to enter the city name
city_name = Entry(root,width=30)
city_name.pack()

# # adding a button for searching the weather
# enter_btn = Button(root,text='Enter',font=("Arial",12),bg='black',fg='white')
# enter_btn.pack(pady=(20,10))


# label to display results
result_label = Label(root, text="", font=("Arial", 14), bg='lightblue', fg='black')
result_label.pack(pady=(20, 10))


# for searching the weather
def search():
    city = city_name.get()
    if city == "":
        result_label.config(text="Please enter a city name")
        return

    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]

        # Showing result
        result_label.config(text=f"{city}\nTemperature: {temp}°C\n{desc.title()}")


enter_btn = Button(root, text='Enter', font=("Arial", 12), bg='black', fg='white', command=search)
enter_btn.pack(pady=(20, 10))

# stopping the main window 
root.mainloop()