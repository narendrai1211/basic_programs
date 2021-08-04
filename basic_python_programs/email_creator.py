import os
from datetime import date
today = date.today()
today_date = today.strftime("%d-%b-%Y")
mail_to = 'mail_reciever_name,' # edit this accordingly tailered to your email
ender_name = 'Narendra Inamdar'
greetings = 'Thanks, and Regards'
subject_name = f'Status Update'
file_name = f"{subject_name} {today_date.replace('-', '_')}"


def write_to_file(msg_body):
    dir_name_to_store_mails = 'drafted_mails'
    try:
        os.mkdir(dir_name_to_store_mails)
    except Exception:
        pass

    with open(f"{dir_name_to_store_mails}/{file_name}.txt", 'w') as f:
        f.write(msg_body)


while True:
    work_done = input('Enter Work Done today: ')
    print(work_done)
    sure_flag = input('Are you sure to finalize message? [Y/N]: ')
    body = f'''{file_name}\nDear {mail_to}

{work_done}

{greetings}
{sender_name}
'''
    print(body)
    if sure_flag.strip().lower() == 'y':
        write_to_file(body)
        break
