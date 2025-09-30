def solution(polynomial):
    terms = polynomial.split(" + ")
    coef = sum(int(t[:-1]) if t not in ["x"] and "x" in t else 1 for t in terms if "x" in t)
    const = sum(int(t) for t in terms if "x" not in t)
    return " + ".join([("x" if coef == 1 else f"{coef}x") if coef else "", str(const) if const else ""]).strip(" +")