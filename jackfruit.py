import wx
import wx.adv
import datetime
from datetime import date , datetime 
import os

app = wx.App()
frame = wx.Frame(None, title="Age Calculator", size=(300,400))
panel = wx.Panel(frame, style=wx.SIMPLE_BORDER)
panel.SetBackgroundColour(wx.Colour(255,229,180))
heading=wx.StaticText(panel,label="AGE CALCULATOR",pos=(550,40))
heading.SetFont(wx.Font(36,wx.FONTFAMILY_DECORATIVE,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_BOLD,False,"bodoni mt black"))
sub=wx.StaticText(panel,label="Enter your date of birth: ",pos=(40,150))
sub.SetFont(wx.Font(23,wx.FONTFAMILY_DECORATIVE,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_NORMAL,False,"TimesNewRoman"))
date_picker = wx.adv.DatePickerCtrl(panel, style=wx.adv.DP_DROPDOWN)
date_picker.SetPosition((370,156))

btn = wx.Button(panel, label="Saved Date", pos=(40,190))

btn.Bind(wx.EVT_BUTTON, lambda event: on_save(event, date_picker))


# Function to save date
def on_save(event, date_picker):
    dob = date_picker.GetValue()
    day = dob.GetDay()
    month = dob.GetMonth() + 1
    year = dob.GetYear()
    wx.MessageBox(f"You selected: {day}/{month}/{year}", "Date Saved")
calc_btn=wx.Button(panel,label="Calculate Age",pos=(120,190))

result_label=wx.StaticText(panel,label="",pos=(40,250))
result_label.SetFont(wx.Font(16,wx.FONTFAMILY_SWISS,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_BOLD))

calc_btn.Bind(wx.EVT_BUTTON,lambda event: calculate_age(event,date_picker,result_label))

def calculate_age(event,date_picker,result_label):
    dob=date_picker.GetValue()
    day=dob.GetDay()
    month=dob.GetMonth()+1
    year=dob.GetYear()
    
    today = date.today()
    birth = date(year, month, day)
    
    age = today.year - birth.year
    if (today.month, today.day) < (birth.month, birth.day):
        age -= 1 
    if (age<0):
        result_label.SetLabel(f"you have given invalid input")
    else:
        result_label.SetLabel(f"Your age is: {age} years")

    
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
    z="abcd"
    if (m == 3 and d >= 21 and d <= 31) or (m == 4 and d <= 19):
        z="aries"
        return ("Aries", "Bold, energetic, and always ready to take the lead.")

    elif (m == 4 and d >= 20 and d <= 30) or (m == 5 and d <= 20):
        z="taurus"
        return ("Taurus", "Calm, loyal, and loves comfort and stability.")

    elif (m == 5 and d >= 21 and d <= 31) or (m == 6 and d <= 20):
        z="gemini"
        return ("Gemini", "Curious, talkative, and full of adaptable ideas.")

    elif (m == 6 and d >= 21 and d <= 30) or (m == 7 and d <= 22):
        z="cancer"
        return ("Cancer", "Emotional, caring, and deeply protective of loved ones.")

    elif (m == 7 and d >= 23 and d <= 31) or (m == 8 and d <= 22):
        z="leo"
        return ("Leo", "Confident, warm-hearted, and loves being creatively expressive.")

    elif (m == 8 and d >= 23 and d <= 31) or (m == 9 and d <= 22):
        z="virgo"
        return ("Virgo", "Practical, detail-oriented, and always striving for improvement.")

    elif (m == 9 and d >= 23 and d <= 30) or (m == 10 and d <= 22):
        z="libra"
        return ("Libra", "Balanced, charming, and focused on harmony and fairness.")

    elif (m == 10 and d >= 23 and d <= 31) or (m == 11 and d <= 21):
        z="scorpio"
        return ("Scorpio", "Intense, intuitive, and deeply passionate.")

    elif (m == 11 and d >= 22 and d <= 30) or (m == 12 and d <= 21):
        z="sagittarius"
        return ("Sagittarius", "Adventurous, optimistic, and loves exploring big ideas.")

    elif (m == 12 and d >= 22 and d <= 31) or (m == 1 and d <= 19):
        z="capricorn"
        return ("Capricorn", "Ambitious, disciplined, and determined to succeed.")

    elif (m == 1 and d >= 20 and d <= 31) or (m == 2 and d <= 18):
        z="aquarius"
        return ("Aquarius", "Innovative, independent, and thinks in unique ways.")

    elif (m == 2 and d >= 19 and d <= 29) or (m == 3 and d <= 20):
        z="pisces"
        return ("Pisces", "Imaginative, empathetic, and deeply connected to emotions.")

def show_zodiac(event):
    dob=date_picker.GetValue()
    d=dob.GetDay()
    m=dob.GetMonth()+1
    z=zodiac_sign(m,d)

    new_win = wx.Frame(None, title="Zodiac sign", size=(300,350))
    panel2 = wx.Panel(new_win)
    panel2.SetBackgroundColour(wx.Colour(246,209,193))

    
    output = wx.StaticText(panel2,
        label=f"Here is your zodiac sign: \n {z}",
        pos=(20, 20)
    )
    output.SetFont(wx.Font(14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
    

    





    new_win.Show()

btn1.Bind(wx.EVT_BUTTON,show_zodiac)



# button 2
# button 2
timer = None
target_date = None
birthday_output = None 
def next_birthday(event, date_picker):
    global timer, target_date, birthday_output
    
    dob = date_picker.GetValue()
    day = dob.GetDay()
    month = dob.GetMonth() + 1
    

    today = date.today()
    current_year = today.year

    
    next_bday = date(current_year, month, day)

    if next_bday < today:
        next_bday = date(current_year + 1, month, day)

    target_date = datetime.combine(next_bday, datetime.min.time())

    new_win = wx.Frame(None, title="Birthday Countdown", size=(600, 400))
    panel2 = wx.Panel(new_win)
    panel2.SetBackgroundColour(wx.Colour(204,238,255))


    birthday_output = wx.StaticText(panel2,
        label="Calculating...",
        pos=(20, 20)
    )
    birthday_output.SetFont(wx.Font(14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))


    timer = wx.Timer(new_win)
    new_win.Bind(wx.EVT_TIMER,update_timer,timer)
    timer.Start(1000)
    new_win.Show()

def update_timer(event):
    now = datetime.now()
    remaining = target_date - now

    if remaining.total_seconds() <= 0:
        birthday_output.SetLabel("🎉 Happy Birthday! 🎉")
        event.GetEventObject().Stop()
        return

    days = remaining.days
    hours, rem = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(rem, 60)

    birthday_output.SetLabel(
        f"Next birthday in:\n"
        f"{days} days {hours} hrs {minutes} min {seconds} sec"
    )

btn2.Bind(wx.EVT_BUTTON, lambda event: next_birthday(event,date_picker))



btn1.Bind(wx.EVT_BUTTON,show_zodiac)


# BUTTON 4 — AGE IN ANY YEAR

def calculate_age_in_year(event):
    dob = date_picker.GetValue()
    birth_year = dob.GetYear()
    birth_month = dob.GetMonth() + 1

    new_win = wx.Frame(None, title="Age in Selected Year", size=(500,350))
    panel2 = wx.Panel(new_win)
    panel2.SetBackgroundColour(wx.Colour(230,210,255))

    wx.StaticText(panel2,
        label="Select a date (year) to know your age:",
        pos=(20,20)
    )

    year_picker = wx.adv.DatePickerCtrl(
        panel2,
        pos=(20,60),
        style=wx.adv.DP_DROPDOWN
    )

    result = wx.StaticText(panel2, label="", pos=(20,140))
    result.SetFont(wx.Font(14,wx.FONTFAMILY_SWISS,
                           wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_BOLD))

    def show_age(evt):
        selected = year_picker.GetValue()
        target_year = selected.GetYear()
        target_month = selected.GetMonth() + 1

        total_birth_months = birth_year * 12 + birth_month
        total_target_months = target_year * 12 + target_month

        if total_target_months < total_birth_months:
            result.SetLabel("Selected date is before your birth!")
        else:
            diff_months = total_target_months - total_birth_months
            years = diff_months // 12
            months = diff_months % 12
            month_name = selected.Format("%B")

            result.SetLabel(
                f"Your age in {month_name} {target_year} will be: "
                f"{years} years {months} months"
            )

    calc = wx.Button(panel2, label="Calculate Age", pos=(20,100))
    calc.Bind(wx.EVT_BUTTON, show_age)

    new_win.Show()

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
    month_num = dob.GetMonth() + 1   # 1–12

    months = ["january","february","march","april","may","june",
              "july","august","september","october","november","december"]

    month_name = months[month_num - 1]

    flower, stone, meaning = get_birth_details(month_name)


    new_win = wx.Frame(None, title="Birth Flower & Birth Stone", size=(300, 300))
    panel2 = wx.Panel(new_win)
    panel2.SetBackgroundColour(wx.Colour(255, 255, 255))


    output = wx.StaticText(
        panel2,
        label=f"Birth Flower: {flower}\n"
              f"Birth Stone: {stone}\n\n"
              f"Meaning:\n{meaning}",
        pos=(20, 20)
    )
    output.SetFont(wx.Font(14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))

    if(month_num==1):
        flower_img_path = f"images/birthflower/1.png"
        stone_img_path  = f"images/birthstone/1.jpg"
    elif(month_num==2):
        flower_img_path = f"images/birthflower/2.png"
        stone_img_path  = f"images/birthstone/2.jpg"
    elif(month_num==3):
        flower_img_path = f"images/birthflower/3.jpg"
        stone_img_path  = f"images/birthstone/3.png"
    elif(month_num==4):
        flower_img_path = f"images/birthflower/4.jpg"
        stone_img_path  = f"images/birthstone/4.png"
    elif(month_num==5):
        flower_img_path = f"images/birthflower/5.jpg"
        stone_img_path  = f"images/birthstone/5.jpg"
    elif(month_num==6):
        flower_img_path = f"images/birthflower/6.jpg"
        stone_img_path  = f"images/birthstone/6.png"
    elif(month_num==7):
        flower_img_path = f"images/birthflower/7.png"
        stone_img_path  = f"images/birthstone/7.png"
    elif(month_num==8):
        flower_img_path = f"images/birthflower/8.jpg"
        stone_img_path  = f"images/birthstone/8.png"
    elif(month_num==9):
        flower_img_path = f"images/birthflower/9.jpg"
        stone_img_path  = f"images/birthstone/9.png"
    elif(month_num==10):
        flower_img_path = f"images/birthflower/10.jpg"
        stone_img_path  = f"images/birthstone/10.png"
    elif(month_num==11):
        flower_img_path = f"images/birthflower/11.jpg"
        stone_img_path  = f"images/birthstone/11.png"
    elif(month_num==12):
        flower_img_path = f"images/birthflower/12.jpg"
        stone_img_path  = f"images/birthstone/12.png"



    flower_img = wx.Image(flower_img_path, wx.BITMAP_TYPE_ANY)
    flower_img = flower_img.Scale(50,50, wx.IMAGE_QUALITY_HIGH)

    flower_bitmap = wx.StaticBitmap(
        panel2,
        bitmap=wx.Bitmap(flower_img_path, wx.BITMAP_TYPE_ANY),
        pos=(20, 200)
    )



    stone_img = wx.Image(stone_img_path, wx.BITMAP_TYPE_ANY)
    stone_img = stone_img.Scale(100,100, wx.IMAGE_QUALITY_HIGH)

    stone_bitmap = wx.StaticBitmap(
        panel2,
        bitmap=wx.Bitmap(stone_img_path, wx.BITMAP_TYPE_ANY),
        pos=(900,400)
    )

    new_win.Show()


btn3.Bind(wx.EVT_BUTTON, show_birth_flower_stone)

frame.Show()
app.MainLoop()
