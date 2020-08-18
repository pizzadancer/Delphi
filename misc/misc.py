def get_boundaries(target, margin):
    low_limit = target - margin
    high_limit = margin + target
    return low_limit, high_limit


target = input("What's your target?: ")
margin = input("What's your margin")
