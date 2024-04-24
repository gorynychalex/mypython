import re

s = 'По всем вопросам пишите на gorynychalex@gmail.com, или на popovich.alexey@yandex.ru, отвечу сразу. Или пишите моему ассистенту secretary@eshift.ru!'

# Электронная почта
emails = re.findall(r'[\w\.-]+@[\w\.-]+', s)

for email in emails: print(email)

# Домены 2-го уровня
domains = re.findall(r'@(\w+.\w+)', s)

for domain in domains: print(domain)

# Домены 1-го уровня
domains1 = re.findall(r'@\w+.(\w+)', s)

for domain in domains1: print(domain)