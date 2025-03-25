def main():
    spacecraft={"name": "voyager 1", "distance":"163"}
    print(f"{create_report(spacecraft)}")

def create_report(spacecraft):
    return f"""
    =========REPORT=========

    Name: {spacecraft["name"]}
    Distance: {spacecraft["distance"]} AU

    =========================
    """
main()

def main_2():
    spacecraft={"name": "James webb"}
    spacecraft.update({"distance":"0.01", "orbit":"Sun"})
    print(f"{create_report_2(spacecraft)}")

def create_report_2(spacecraft):
    return f"""
    =========REPORT=========

    Name: {spacecraft.get("name","Unknown")}
    Distance: {spacecraft.get("distance","Unknown")} AU
    Orbit:{spacecraft.get("orbit", "Unknown")}
    Speed:{spacecraft.get("speed", "Unknown")}
    
    =========================
    """
main_2()