import datetime

counterClick = 0
startTime = datetime.datetime.now()

def command_switch_response(command):
    print("switching the command:{}".format(command))
    
    helpText = "Commands available:{}".format(
            "\n/Help - returns the available commands." +
            "\n/Time - returns the current time." +
            "\n/Counter - Counter of this command." +
            "\n/Uptime - how long am i up." +
            "\n/Hash - get a hashed string.")

    commands = {'/start': "Welcome to Eitan's first Bot!\n" + helpText,
                '/help': helpText,
                '/time': datetime.datetime.utcnow,
                '/counter': using_Counter_Up,
                '/uptime': get_up_time,
                '/hash': getHashVal}

    response = commands.get(command, "no such command")
    if callable(response):
        return response()
    return response
    
def using_Counter_Up():
    print("starting countering up")
    global counterClick
    print("counterClick before:{}".format(counterClick))
    counterClick += 1
    print("counterClick after:{}".format(counterClick))
    return counterClick

def get_up_time():
    print("uptime is about to calc")
    global startTime
    return (datetime.datetime.now() - startTime)

def getHashVal():
    return hash(datetime.datetime.now())