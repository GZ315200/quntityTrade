# priceSequence
# 导入pmath

import investment.stock.pmath as pmath

def OpenPrice(priceSeq):
    Open=priceSeq[0]
    return(Open)

def ClosePrice(priceSeq):
    Close=priceSeq[-1]
    return(Close)

def HighPrice(priceSeq):
    High=pmath.findMax(priceSeq)
    return(High)

def LowPrice(priceSeq):
    Low=pmath.findMin(priceSeq)
    return(Low)
