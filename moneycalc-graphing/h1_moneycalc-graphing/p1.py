# Problem 1
""" Input: hours, wage, bonus: (y or n). Output: totalpay, overtimepay"""
# String Constants
hours_prompt = 'Hours worked: '
wage_prompt = 'Rate per hour: '
has_bonus = 'Bonus (y/n): '
bonus_prompt = 'Bonus amount: '

def get_float(message):
    """Returns keyboard input as float"""
    return float(input(message))

def overtime(h, r):
    """Returns the amount of overtime pay earned"""
    return (h - 40) * r * 1.5

def reg_pay(h, r):
    """Returns pay amount before overtime"""
    if h <= 40:
        return h * r
    else:
        return 40 * r

def pay(h, r):
    """Calculates total pay without regard to bonus"""
    if h <= 40:
        return reg_pay(h, r)
    else:
        return reg_pay(h, r) + overtime(h, r)

def main():
    '''Main Function'''
    hours_worked = get_float(hours_prompt)
    rate_per_hour = get_float(wage_prompt)
    yes_no = input(has_bonus)
    if yes_no.lower() == 'y':
        bonus = get_float(bonus_prompt)
        print("Total Pay: $", pay(hours_worked, rate_per_hour) + bonus)
        print("Overtime Pay: $", overtime(hours_worked, rate_per_hour))
    else:
        print("Total Pay: $", pay(hours_worked, rate_per_hour))
        print("Overtime Pay: $", overtime(hours_worked, rate_per_hour))

main()
