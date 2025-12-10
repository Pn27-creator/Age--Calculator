import wx
import wx.adv
import datetime
from datetime import date
app = wx.App()
frame = wx.Frame(None, title="Age Calculator", size=(300,400))
panel = wx.Panel(frame, style=wx.SIMPLE_BORDER)
#background
panel.SetBackgroundColour(wx.Colour(255,229,180))
#age calculator heading
heading=wx.StaticText(panel,label="AGE CALCULATOR",pos=(550,40))
heading.SetFont(wx.Font(36,wx.FONTFAMILY_DECORATIVE,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_BOLD,False,"bodoni mt black"))
#enter age
sub=wx.StaticText(panel,label="Enter your date of birth: ",pos=(40,150))
sub.SetFont(wx.Font(23,wx.FONTFAMILY_DECORATIVE,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_NORMAL,False,"TimesNewRoman"))
date_picker = wx.adv.DatePickerCtrl(panel, style=wx.adv.DP_DROPDOWN)
# Position it
date_picker.SetPosition((370,156))
# saving the date
# Add button
btn = wx.Button(panel, label="Saved Date", pos=(40,190))

# Bind button to function
btn.Bind(wx.EVT_BUTTON, lambda event: on_save(event, date_picker))


# Function to save date
def on_save(event, date_picker):
    dob = date_picker.GetValue()
    day = dob.GetDay()
    month = dob.GetMonth() + 1
    year = dob.GetYear()
    wx.MessageBox(f"You selected: {day}/{month}/{year}", "Date Saved")
#calculate age button
calc_btn=wx.Button(panel,label="Calculate Age",pos=(120,190))

#reult label(initially empty
result_label=wx.StaticText(panel,label="",pos=(40,250))
result_label.SetFont(wx.Font(16,wx.FONTFAMILY_SWISS,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_BOLD))

calc_btn.Bind(wx.EVT_BUTTON,lambda event: calculate_age(event,date_picker,result_label))

def calculate_age(event,date_picker,result_label):
    dob=date_picker.GetValue()
    day=dob.GetDay()
    month=dob.GetMonth()+1
    year=dob.GetYear()
    
    today = date.today()
    birth = datetime.date(year, month, day)
    
    age = today.year - birth.year
    if (age<0):
        result_label.SetLabel(f"you have given invalid input")
    else:
        result_label.SetLabel(f"Your age is: {age} years")
   

        

    
#date is stored in dob and age is stored in age

#printing date there beside
#calc=wx.StaticText(panel,label="age is {age} years",pos=(240,190))
#calc.SetFont(wx.Font(23,wx.FONTFAMILY_DECORATIVE,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_NORMAL,False,"TimesNewRoman"))
    
#buttons
btn1=wx.Button(panel, label="zodiac sign",pos=(100,320),size=(250,250))
btn1.SetBackgroundColour(wx.Colour(255,204,204)) #rose
btn2=wx.Button(panel, label="Next Bday countdown",pos=(400,320),size=(250,250))
btn2.SetBackgroundColour(wx.Colour(204,238,255)) #blue
btn3=wx.Button(panel,label="Birthflower and Birthstone",pos=(700,320),size=(250,250))
btn3.SetBackgroundColour(wx.Colour(255,250,205)) #orchid
btn4=wx.Button(panel,label="What will be my age in so and so year",pos=(1000,320),size=(250,250))
btn4.SetBackgroundColour(wx.Colour(230,210,255)) #lavendar

#zodiac sign code

def zodiac_sign(m, d):
    if (m == 3 and d >= 21 and d <= 31) or (m == 4 and d <= 19):
        return ("Aries", "Bold, energetic, and always ready to take the lead.")

    elif (m == 4 and d >= 20 and d <= 30) or (m == 5 and d <= 20):
        return ("Taurus", "Calm, loyal, and loves comfort and stability.")

    elif (m == 5 and d >= 21 and d <= 31) or (m == 6 and d <= 20):
        return ("Gemini", "Curious, talkative, and full of adaptable ideas.")

    elif (m == 6 and d >= 21 and d <= 30) or (m == 7 and d <= 22):
        return ("Cancer", "Emotional, caring, and deeply protective of loved ones.")

    elif (m == 7 and d >= 23 and d <= 31) or (m == 8 and d <= 22):
        return ("Leo", "Confident, warm-hearted, and loves being creatively expressive.")

    elif (m == 8 and d >= 23 and d <= 31) or (m == 9 and d <= 22):
        return ("Virgo", "Practical, detail-oriented, and always striving for improvement.")

    elif (m == 9 and d >= 23 and d <= 30) or (m == 10 and d <= 22):
        return ("Libra", "Balanced, charming, and focused on harmony and fairness.")

    elif (m == 10 and d >= 23 and d <= 31) or (m == 11 and d <= 21):
        return ("Scorpio", "Intense, intuitive, and deeply passionate.")

    elif (m == 11 and d >= 22 and d <= 30) or (m == 12 and d <= 21):
        return ("Sagittarius", "Adventurous, optimistic, and loves exploring big ideas.")

    elif (m == 12 and d >= 22 and d <= 31) or (m == 1 and d <= 19):
        return ("Capricorn", "Ambitious, disciplined, and determined to succeed.")

    elif (m == 1 and d >= 20 and d <= 31) or (m == 2 and d <= 18):
        return ("Aquarius", "Innovative, independent, and thinks in unique ways.")

    elif (m == 2 and d >= 19 and d <= 29) or (m == 3 and d <= 20):
        return ("Pisces", "Imaginative, empathetic, and deeply connected to emotions.")

def show_zodiac(event):
    dob=date_picker.GetValue()
    d=dob.GetDay()
    m=dob.GetMonth()+1
    z=zodiac_sign(m,d)
   

# Create a NEW WINDOW
    new_win = wx.Frame(None, title="Zodiac sign", size=(300,350))
    panel2 = wx.Panel(new_win)
    panel2.SetBackgroundColour(wx.Colour(246,209,193))

    # Add text to the new window
    output = wx.StaticText(panel2,
        label=f"Here is your zodiac sign: \n {z}",
        pos=(20, 20)
    )
    output.SetFont(wx.Font(14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))

    new_win.Show()

# button 2
def next_birthday(event, date_picker):
    dob = date_picker.GetValue()
    day = dob.GetDay()
    month = dob.GetMonth() + 1
    year = dob.GetYear()

    today = date.today()
    current_year = today.year

    # Next birthday this year
    next_bday = date(current_year, month, day)

    # If birthday passed for this year → use next year
    if next_bday < today:
        next_bday = date(current_year + 1, month, day)

    # Countdown
    remaining = next_bday - today
 

    # Create a NEW WINDOW
    new_win = wx.Frame(None, title="Days remaining", size=(600, 400))
    panel2 = wx.Panel(new_win)
    panel2.SetBackgroundColour(wx.Colour(204,238,255))

    # Add text to the new window
    output = wx.StaticText(panel2,
        label=f"Your next birthday is in {remaining.days} days 🎉",
        pos=(20, 20)
    )
    output.SetFont(wx.Font(14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))

    new_win.Show()


btn2.Bind(wx.EVT_BUTTON, lambda event: next_birthday(event,date_picker))



btn1.Bind(wx.EVT_BUTTON,show_zodiac)

# BUTTON 4 — AGE IN ANY YEAR
def calculate_age_in_year(event):
    dob = date_picker.GetValue()
    birth_day = dob.GetDay()
    birth_month = dob.GetMonth() + 1
    birth_year = dob.GetYear()

    dlg = wx.TextEntryDialog(frame, "Enter the year you want to know your age in:",
                             "Age In Future Year")

    if dlg.ShowModal() == wx.ID_OK:
        try:
            target_year = int(dlg.GetValue())
        except:
            wx.MessageBox("Please enter a valid numeric year!", "Error")
            return

        if target_year < birth_year:
            wx.MessageBox("The year you entered is before your birth!", "Invalid Year")
            return


        age = target_year - birth_year
        
        # Create a NEW WINDOW
    new_win = wx.Frame(None, title="Age in so and so year", size=(600, 400))
    panel2 = wx.Panel(new_win)
    panel2.SetBackgroundColour(wx.Colour(230,210,255))

    # Add text to the new window
    output = wx.StaticText(panel2,
        label=f"Your age in {target_year} will be: {age} years",
        pos=(20, 20)
    )
    output.SetFont(wx.Font(14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))

    new_win.Show()

    dlg.Destroy()

btn4.Bind(wx.EVT_BUTTON, calculate_age_in_year)




#button 3

def get_birth_details(month):
    month = month.lower()

    if month == "january":
        flower = "Carnation"
        stone = "Garnet"
        meaning = (
            "Carnation: love, admiration, determination.\n"
            "Garnet: confidence, strength, loyalty."
        )

    elif month == "february":
        flower = "Violet"
        stone = "Amethyst"
        meaning = (
            "Violet: loyalty, humility, intuition.\n"
            "Amethyst: calmness, wisdom, clarity."
        )

    elif month == "march":
        flower = "Daffodil"
        stone = "Aquamarine"
        meaning = (
            "Daffodil: hope, positivity, new beginnings.\n"
            "Aquamarine: peace, communication, courage."
        )

    elif month == "april":
        flower = "Daisy"
        stone = "Diamond"
        meaning = (
            "Daisy: purity, innocence, joy.\n"
            "Diamond: strength, resilience, honesty."
        )

    elif month == "may":
        flower = "Lily of the Valley"
        stone = "Emerald"
        meaning = (
            "Lily of the Valley: sweetness, empathy, renewal.\n"
            "Emerald: love, harmony, creativity."
        )

    elif month == "june":
        flower = "Rose"
        stone = "Pearl"
        meaning = (
            "Rose: love, beauty, grace.\n"
            "Pearl: innocence, truth, serenity."
        )

    elif month == "july":
        flower = "Larkspur"
        stone = "Ruby"
        meaning = (
            "Larkspur: positivity, open-heartedness.\n"
            "Ruby: passion, energy, courage."
        )

    elif month == "august":
        flower = "Gladiolus"
        stone = "Peridot"
        meaning = (
            "Gladiolus: strength, integrity, determination.\n"
            "Peridot: positivity, balance, healing."
        )

    elif month == "september":
        flower = "Aster"
        stone = "Sapphire"
        meaning = (
            "Aster: wisdom, elegance, patience.\n"
            "Sapphire: truth, loyalty, intelligence."
        )

    elif month == "october":
        flower = "Marigold"
        stone = "Opal"
        meaning = (
            "Marigold: creativity, confidence, passion.\n"
            "Opal: imagination, inspiration, expression."
        )

    elif month == "november":
        flower = "Chrysanthemum"
        stone = "Topaz"
        meaning = (
            "Chrysanthemum: joy, loyalty, energy.\n"
            "Topaz: strength, confidence, friendship."
        )

    elif month == "december":
        flower = "Poinsettia"
        stone = "Turquoise"
        meaning = (
            "Poinsettia: celebration, generosity, success.\n"
            "Turquoise: protection, intuition, adventure."
        )

    else:
        return "Invalid", "Invalid", "Invalid"

    return flower, stone, meaning

def show_birth_flower_stone(event):
    dob = date_picker.GetValue()
    month_num = dob.GetMonth() + 1

    months = ["january","february","march","april","may","june",
              "july","august","september","october","november","december"]

    month_name = months[month_num - 1]

    flower, stone, meaning = get_birth_details(month_name)

    # Create a NEW WINDOW
    new_win = wx.Frame(None, title="Birth Flower & Birth Stone", size=(600, 400))
    panel2 = wx.Panel(new_win)
    panel2.SetBackgroundColour(wx.Colour(255, 250, 205))

    # Add text to the new window
    output = wx.StaticText(panel2,
        label=f"Birth Flower: {flower}\n"
              f"Birth Stone: {stone}\n\n"
              f"Meaning:\n{meaning}",
        pos=(20, 20)
    )
    output.SetFont(wx.Font(14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))

    new_win.Show()


btn3.Bind(wx.EVT_BUTTON, show_birth_flower_stone)

frame.Show()
app.MainLoop()
