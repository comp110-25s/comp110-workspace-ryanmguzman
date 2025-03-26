def pack(degrees_fahrenheit: float) -> str:
    """Tells me what to pack"""
    if degrees_fahrenheit == 0.0:
        return "Really Warm Jacket"
    else:
        if degrees_fahrenheit >= 32.0:
            return "Long Sleeve Shirt"
