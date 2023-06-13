def roll_call_dwarves(list):
    num = 1
    for item in list:
        print(f'{num}. {item}')
        num += 1

def summon_captain_planet(list):
    lis = [f'{name.title()}!' for name in list]
    return lis
print(summon_captain_planet(["Dopey", "Grumpy", "Bashful"]))
def long_planeteer_calls(list):
    for name in list:
        if(len(name) > 4):
            return True
    return False

def find_the_cheese(list):
    cheeses = ["cheddar", "gouda", "camembert"]
    for cheese in cheeses:
        if(cheese in list):
            return cheese
        else:
            return None
