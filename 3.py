email = {}
with open('mbox-short.txt', 'r') as file:
    for line in file:
        if line.startswith('From:'):
            emails = line.split()[1]
            email[emails] = email.get(emails, 0) + 1
print(email)