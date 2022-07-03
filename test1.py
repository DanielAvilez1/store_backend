

def run_test():
    print("Test 1 - dictionaries")

    me = {
        "first": "Daniel",
        "last": "Avilez",
        "age": 27,
        "hobbies": [],
        "address": {
            "street": "dark",
            "number": "802",
            "city": "Tucson",
            "state": "Arizona",
            "zip": "85756"
        }
    }

    print(me)

    print(me["first"])

    print(me["first"] + " " + me["last"])

    # change values
    me["age"] = me["age"] + 1
    me["age"] = 99

    # add new keys
    me["preferred_color"] = "black"
    print(me)

    if "middle_name" in me:
        print(me["middle_name"])
    address = me["address"]
    print("------------address------------")
    print(address)
    print(type(address))

    print(
        f'{address["street"]} #{address["number"]},{address["city"]}, {address["state"]},{address["zip"]}')


run_test()
