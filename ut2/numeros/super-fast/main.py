def run(speed_km_h: float) -> float:
    _1cms_to_kmh = 0.036
    speed_cm_s = round(speed_km_h / _1cms_to_kmh)
    return speed_cm_s


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
