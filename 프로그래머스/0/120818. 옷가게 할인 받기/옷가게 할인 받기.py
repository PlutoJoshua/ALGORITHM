def solution(price):
    if 100000 <= price < 300000:
        return int(price - price * 0.05)
    elif 300000 <= price < 500000:
        return int(price - price * 0.1)
    elif 500000 <= price:
        return int(price - price * 0.2)
    else:
        return price
