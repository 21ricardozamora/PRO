def run(age: int, weight: int, heartbeat: int, platelets: int) -> bool:
    suitable_for_donation = False
    if age >= 18 and age <= 65:
        if weight >= 50:
            if heartbeat >= 50 and heartbeat <= 110:
                if platelets > 150_000:
                    suitable_for_donation = True
                else:
                    suitable_for_donation = False
    return suitable_for_donation


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
