import json

values = []
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield tuple(lst[i:i + n])

with open("data.txt") as fd:
    for line in fd:
        if line.strip():
            v = int(line.strip())
            values.append(v)

assert len(values) % 10 == 0

values = chunks(values, 10)
results = []

for (index, fee_direction, pool_x, pool_y, pool_admin_fee, pool_connect_fee, pool_lp_fee, pool_incentive_fee, x, y) in values:
    results.append({
        "fee_direction": 'X' if (fee_direction == 200) else 'Y',
        "direction": 'x-to-y' if (index == 111) else 'y-to-x', 
        "pool_x": str(pool_x), 
        "pool_y": str(pool_y), 
        "pool_admin_fee": str(pool_admin_fee), 
        "pool_connect_fee": str(pool_connect_fee), 
        "pool_lp_fee": str(pool_lp_fee), 
        "pool_incentive_fee": str(pool_incentive_fee), 
        "x": str(x), 
        "y": str(y)
    })

with open("data-out.json", "w") as fd:
    json.dump(results, fd)