def car_info(manufacturer, model,**car_info):
    car_info['Manufacturer'] = manufacturer
    car_info['Model Name'] = model
    return car_info

car_profile = car_info('Mercedes','Benz',
                        year='2024',
                        color='black')
print(car_profile)