abbrv_map = {
    'th': 'thou',
    'in': 'inch',
    'ft': 'foot',
    'yd': 'yard',
    'ch': 'chain',
    'fur': 'furlong',
    'mi': 'mile',
    'lea': 'league'
}

val_map = {
    'thou': 1,
    'inch': 1000,
    'foot': 12,
    'yard': 3,
    'chain': 22,
    'furlong': 10,
    'mile': 8,
    'league': 3
}

unit_order = ['thou','inch','foot','yard','chain','furlong','mile','league']
inv_unit_order = dict(zip(unit_order, range(len(unit_order))))

x, u, _, v = input().split()
x = int(x)

if u in abbrv_map:
    u = abbrv_map[u]
if v in abbrv_map:
    v = abbrv_map[v]

ui = inv_unit_order[u]
vi = inv_unit_order[v]

start = min((ui,vi))+1
end = max((ui,vi))+1

amnt = 1
for unit in unit_order[start:end]:
    amnt *= val_map[unit]

if ui < vi:
    print(x / amnt)
else:
    print(x * amnt)

