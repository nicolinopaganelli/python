# BMI Calculator
## BMI = (weight in lbs * 703) / (height in inches)^2

def main():
    INCH = input('how tall are you?\n(in inches)')
    LBS = input('how much do you weigh?\(in pounds)')
    print(calculate(INCH, LBS))

def calculate(INCH, LBS):
    bmi = (int(LBS) * 703) / (int(INCH) ** 2)
    return round(bmi, 2)

if __name__ == '__main__':
    main()
