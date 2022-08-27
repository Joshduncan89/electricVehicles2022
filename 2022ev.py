from bs4 import BeautifulSoup
import requests, openpyxl

excel = openpyxl.Workbook()
print(excel.sheetnames)
sheet = excel.active

try:
    source = requests.get('https://insideevs.com/reviews/344001/compare-evs/')
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')
    cars = soup.find('tbody').find_all('tr')

    for car in cars:
      car_ = car.find_all('td')
      title = car_[0].text
      basePrice = car_[1].text
      destCharge = car_[2].text
      taxCredit = car_[3].text
      effPrice = car_[4].text
      print(title, basePrice,destCharge,taxCredit,effPrice)
      sheet.append([title,basePrice,destCharge,taxCredit,effPrice])

except Exception as e:
    print(e)

excel.save('Affordable EV 2022.xlsx')