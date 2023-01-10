
def format_duration(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)

def countdown(formatted_duration):
    formatted_duration = "00:25:00"
    print("counting down: " + formatted_duration)

def pomodoro_timer():
    duration = 1500
    formatted_duration = format_duration(duration)
    print(countdown(formatted_duration))


    #return formatted_duration


print(pomodoro_timer(

