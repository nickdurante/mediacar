import obd
from colorama import Fore, Back, Style
from subprocess import call
import RPi.GPIO as GPIO
import fancy_output

# pip install obd
# pip install colorama
#obd.logger.setLevel(obd.logging.DEBUG)

def main():
    #connection = obd.OBD()
    connection = obd.Async()

    text_status = '---------------- ' + connection.status() + ' ----------------'

    if connection.status() == 'Not Connected':
        print_red(text_status)
        connection.stop()
        return
    else:
        print_green(text_status)

    ecu = connection.query(obd.commands.GET_DTC)
    print_green(ecu.value)

    fuel = obd.commands['FUEL_STATUS']
    coolant = obd.commands['COOLANT_TEMP']
    ethanol = obd.commands['ETHANOL_PERCENT']

    print_green('\nFuel: ' + str(fuel) +'\n' + 'Coolant: ' + str(coolant) + '\n' + 'Ethanol percentage: ' + str(ethanol) +'%\n\n')


    #rpm = connection.watch(obd.commands.RPM, callback=new_value)

    #rpm = str(connection.watch(obd.commands.RPM))
    #engine_load = str(connection.watch(obd.commands.ENGINE_LOAD))
    #fuel_injection = str(connection.watch(obd.commands.FUEL_INJECT_TIMING))

    connection.start()
    switch_handler()

    return

    #   1 - RPM     2 - ENGINE_LOAD     3 - FUEL_INJECT_TIMING  4 - INTAKE_TEMP     5 - AIR FLOW RATE (MAF)    
    #   6 - FUEL_RATE   7 - INTAKE_PRESSURE

def mode_helper():
    text = '1) RPM\n2) ENGINE LOAD\n3) FUEL INJECTION\n4) INTAKE TEMPERATURE\n5) AIR FLOW RATE\n6) FUEL\n7) INTAKE PRESSURE\n8) EXIT'
    print(text)

def switch_handler():
    mode_helper()
    switch_init()

    while True:
        s1 = GPIO.input(16)
        s2 = GPIO.input(12)
        s3 = GPIO.input(13)
        s4 = GPIO.input(20)
        s5 = GPIO.input(6)
        s6 = GPIO.input(21)
        s7 = GPIO.input(26)
        s8 = GPIO.input(19)

        if s1 == False:
            show_value(RPM)
        if s2 == False:
            show_value(ENGINE_LOAD)
        if s3 == False:
            show_value(FUEL_INJECT_TIMING)
        if s4 == False:
            show_value(INTAKE_TEMP)
        if s5 == False:
            show_value(MAF)
        if s6 == False:
            show_value(FUEL_RATE)
        if s7 == False:
            show_value(INTAKE_PRESSURE)
        if s8 == False:
            print('Exiting....')
            return

def show_value(name):
    value = str(connection.watch(obd.commands[name]))
    fancy_output.print_fancy(name + ': ' + value)
    time.sleep(0.75)

def print_value(value_name, value):
    print(Fore.RED + Style.BRIGHT + value_name + ': ' + Style.RESET_ALL + Fore.RED + value + '\n')
    print(Style.RESET_ALL)


def new_value(v):
        print(v.value)
        return

def print_red(text):
        print(Fore.RED + Style.BRIGHT+ text + Style.RESET_ALL + '\n')
        return

def print_green(text):
        print(Fore.GREEN + Style.BRIGHT+ text + Style.RESET_ALL + '\n')
        return

def switch_init():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)



if __name__ == "__main__":
    main()

