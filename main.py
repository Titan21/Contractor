from enum import Enum
import random
import pyautogui

from pyautogui import hotkey, click, locateCenterOnScreen, hold, sleep


typing_base_speed = 20


# Define enum classes for different actions and currencies
class Actions(Enum):
    BUY = 1
    SELL = 2


class Currencies(Enum):
    NCC = 0
    ICA = 1
    CIS = 2
    AIC = 3

def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling '{func.__name__}' with args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper


def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))

def write(content):
    content = str(content)
    for character in content:
        pyautogui.press(character)
        sleep(random.expovariate(typing_base_speed/2))

def press(content):
    pyautogui.press(content)
    sleep(random.expovariate(typing_base_speed / 10))


# Function to press tab key for a given amount of times
def multi_tab(amount):
    for _ in range(amount):
        press('tab')


# Function to dismiss the confirmation dialog
def dismiss_confirmation():
    # print("Looking for Dismiss.png")
    # locateCenterOnScreen('resources/dismiss.png', grayscale=True)
    sleep(clamp(random.expovariate(typing_base_speed / 100), 0.7214, 4.8392))
    click()
    print("Found and clicked")
    sleep(random.expovariate(typing_base_speed / 10))


# Function to write headers and save
@log_call
def write_header(name, preamble):
    hotkey('ctrl', 'a')
    write(name)
    press('tab')
    write(preamble)
    press(['tab', 'enter'])
    dismiss_confirmation()


# Function to generate Name
def _name_generator(location, material, action, partner):
    return str.upper(f"{location}-{material}-{action.name}-{partner}")


# Function to generate preamble
def _preamble_generator(amount, material, unitPrice):
    return f"{amount} {material} @{unitPrice}/u = {amount * unitPrice}"


# Function to select template and apply
@log_call
def select_template(action):
    multi_tab(4)
    for _ in range(action.value):
        press('down')
    press(['tab', 'enter'])


# Function to set buy conditions
@log_call
def buy_conditions(amount, currency):
    multi_tab(1)
    press('enter')
    with hold('shift'):
        multi_tab(8)
    write(amount)
    press('tab')
    for _ in range(currency.value):
        press('up')
    press(['tab', 'enter'])
    dismiss_confirmation()


# Function to set deadlines for the user
def self_deadlines():
    pass


# Function to set partner conditions
@log_call
def partner_conditions(amount, material, location):
    multi_tab(8)
    press('enter')
    with hold('shift'):
        multi_tab(2)
    write(amount)
    press('tab')
    write(material)
    sleep(clamp(random.expovariate(typing_base_speed), 0.928223, 3.27830))
    press('enter')
    press('tab')
    write(location)
    sleep(clamp(random.expovariate(typing_base_speed), 1.223, 4.21303))
    press('down')
    press('enter')
    press(['tab', 'enter'])
    dismiss_confirmation()


# Function to set partner deadlines
def partner_deadlines():
    pass


# Function to save conditions and dismiss confirmation
@log_call
def save_conditions():
    multi_tab(10)
    press('enter')
    dismiss_confirmation()


# Function to enter recipient of contract
@log_call
def enter_recipient(recipient):
    multi_tab(12)
    write(recipient)
    press('enter')
    press(['tab', 'enter'])


# Master function to automate the entire process
def master(action, material, amount, unit_price, location, partner, currency):
    print("STARTING COUNTDOWN")
    sleep(2)
    name = _name_generator(location, material, action, partner)
    preamble = _preamble_generator(amount, material, unit_price)
    total_price = amount * unit_price

    write_header(name, preamble)
    select_template(action)
    buy_conditions(total_price, currency)
    partner_conditions(amount, material, location)
    save_conditions()
    enter_recipient(partner)
    print("Done!")


if __name__ == "__main__":
    # print("Welcome to the Contract Automator CLI...")
    #
    # action_input = input("""Enter Action (BUY or SELL):
    # [1] BUY
    # [2] SELL
    # Your Choice: """)
    # action_input = Actions(int(action_input))
    #
    # material = input("Enter Material: ")
    #
    # amount = input("Enter Amount: ")
    # while not amount.isdigit():
    #     print("Invalid Input. Please enter a number.")
    #     amount = input("Enter Amount: ")
    # amount = int(amount)
    #
    # unitPrice = input("Enter Unit Price: ")
    # while not unitPrice.replace('.', '', 1).isdigit():
    #     print("Invalid Input. Please enter a number.")
    #     unitPrice = input("Enter Unit Price: ")
    # unitPrice = float(unitPrice)
    #
    # location = input("Enter Location: ")
    #
    # partner = input("Enter Partner: ")
    #
    # currency_input = input("""Enter Currency (AIC, NIS, ICA, NCC):
    # NCC = 0
    # ICA = 1
    # CIS = 2
    # AIC = 3
    # Your Choice: """)
    # currency_input = Currencies(int(currency_input))

    action_input = Actions.BUY
    material = "INS"
    amount = 5000
    unit_price = 120
    location = "MOR"
    partner = "Schaitr"
    currency_input = Currencies.NCC

    master(action=action_input, material=material, amount=amount, unit_price=unit_price,
           location=location, partner=partner, currency=currency_input)