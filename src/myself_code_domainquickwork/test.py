record_types = [
    ('A', 'query'),
    ('AAAA', 'query'),
    ('CNAME', 'query'),
    ('MX', 'query'),
    ('NS', 'query'),
    ('TXT', 'query'),
    ('PTR', 'query'),
    ('SOA', 'query')
]

for record_type, method in record_types:
    print(record_type,method)

    