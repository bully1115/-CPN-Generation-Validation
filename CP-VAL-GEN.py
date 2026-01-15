import random
import re

def validate_ssn(ssn):
    ssn = re.sub(r'[^0-9]', '', ssn)
    if len(ssn) != 9 or int(ssn[0:3]) == 666 or int(ssn[0:3]) > 899:
        return False
    # Group 2 NJ validation (0 or 6)
    if int(ssn[3:5]) not in [0, 6]: return False
    return True

def generate_nj_cpn_batch(count=10):
    batch = []
    while len(batch) < count:
        aaa = random.randint(1, 65)  # NJ common range
        gg = random.choice([0, 6])
        sss = random.randint(0, 999)
        ssn = f"{aaa:03}-{gg}-{sss:04}"
        if validate_ssn(ssn): batch.append(ssn)
    return batch

print(generate_nj_cpn_batch(10))
