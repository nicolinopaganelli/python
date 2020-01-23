# BMI Calculator
## BMI = (weight in lbs * 703) / (height in inches)^2
#### is this ugly code? yes. is the user interface even uglier? also yes. did I write this in 10 minutes because 
#### I didn't feel like using an online BMI calculator? absolutely.

def main():
    INCH = input('how tall are you?\n(in inches)')
    LBS = input('how much do you weigh? (in pounds)')
    print('your BMI is', calculate(INCH, LBS))

def calculate(INCH, LBS):
    bmi = (int(LBS) * 703) / (int(INCH) ** 2)
    return round(bmi, 2)

if __name__ == '__main__':
    main()
