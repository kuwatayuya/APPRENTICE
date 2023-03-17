def train_fare(age):
    
    if age >= 12:
        train_fare = 10000
    elif 6 <= age < 12:
        train_fare = 5000
    else:
        train_fare = 0
    
    return print(train_fare)

train_fare(10)