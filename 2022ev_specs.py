from bs4 import BeautifulSoup
import requests, openpyxl


excel = openpyxl.load_workbook('Affordable EV 2022.xlsx')
excel.create_sheet('Sheet 2')
sheet2 = excel['Sheet 2']
print(sheet2)

try:
    source = requests.get('https://insideevs.com/reviews/344001/compare-evs/')
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')
    cars = soup.find_all('tbody')[1].find_all('tr')

    for car in cars:
      car_ = car.find_all('td')
      title = car_[0].text
      drive = car_[1].text
      battery_kwh = car_[2].text
      epa_range = car_[3].text
      mph_0_60 = car_[4].text
      top_speed = car_[5].text

      sheet2.append([title,drive,battery_kwh,epa_range,mph_0_60,top_speed])

      print(title, drive,battery_kwh,epa_range,mph_0_60,top_speed)

except Exception as e:
    print(e)

excel.save('Affordable EV 2022.xlsx')