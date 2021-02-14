from datetime import datetime

horas = int(datetime.now().strftime('%H'))

horario = ''
fim_horario = ''

if horas < 12:
    horario += 'bom dia'
    fim_horario += 'Tenha um ótimo dia.\n'
elif horas < 18:
    horario += 'boa tarde'
    fim_horario += 'Tenha uma ótima tarde.\n'
elif horas < 24:
    horario += 'boa noite'
    fim_horario += 'Tenha uma ótima noite.\n'
