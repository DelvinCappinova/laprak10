def count_domain_emails(file_name):
    domain_counts = {}
    with open(file_name, 'r') as f:
        for line in f:
            if line.startswith('From '):
                words = line.split()
                email = words[1]
                domain = email.split('@')[1]
                if domain not in domain_counts:
                    domain_counts[domain] = 1
                else:
                    domain_counts[domain] += 1
    return domain_counts

file_name = 'mbox-short.txt'
print(count_domain_emails(file_name))