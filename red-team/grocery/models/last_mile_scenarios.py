# per-order models, AUD
def onDemand(basket, merchants, takeRate=0.15, delFee=9.99, svc=0.05, rate=32.0):
    mins = 5 + merchants*5 + (merchants-1)*5 + 8 + 4   # position, dwell, inter-merchant, line-haul, drop
    courier = mins/60*rate*1.15   # +15% platform margin/insurance/idle leakage if via 3PL or own contractor pool
    rev = basket*takeRate + delFee + basket*svc
    pay = (basket+delFee)*0.017
    refunds = basket*0.03 + 1.0     # OOS/mispick credits + CS handling
    pack = 1.0 + 0.5*merchants
    support = 1.5
    cac = 57/10
    contrib = rev - courier - pay - refunds - pack - support
    return mins, round(courier,2), round(rev,2), round(contrib,2), round(contrib-cac,2)
def consolidated(basket, takeRate=0.15, delFee=9.99, svc=0.05, dropsPerHr=5, vanHr=72, inbound=2.5, hub=3.5):
    deliver = vanHr/dropsPerHr
    rev = basket*takeRate + delFee + basket*svc
    pay=(basket+delFee)*0.017; refunds=basket*0.025+0.8; pack=1.5; support=1.2; cac=57/10
    contrib = rev-deliver-inbound-hub-pay-refunds-pack-support
    return round(deliver+inbound+hub,2), round(rev,2), round(contrib,2), round(contrib-cac,2)
for b in (60,90,130):
    for m in (1,2,3):
        print('OD basket',b,'merchants',m, onDemand(b,m))
for b in (60,90,130):
    for d in (4,5,7):
        print('CONS basket',b,'drops/hr',d, consolidated(b,dropsPerHr=d))
# merchant view
for gm,items in ((0.26,18),(0.35,3),(0.40,4)):
    pass
def merchant(sales, gm, lines, secPerLine=50, fixedMin=3, wage=38, take=0.15, idle=False):
    labour = 0 if idle else (lines*secPerLine/60+fixedMin)/60*wage
    return round(sales*gm - sales*take - labour,2), round(labour,2)
print('grocer $60,18 lines,GM26%', merchant(60,0.26,18), merchant(60,0.26,18,idle=True))
print('butcher $25,3 lines,GM35%', merchant(25,0.35,3))
print('deli $20,4 lines,GM40%', merchant(20,0.40,4))
