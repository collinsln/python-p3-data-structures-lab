spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    
    names = [food['name'] for food in spicy_foods]
    return names
print(get_names(spicy_foods))

def get_spiciest_foods(spicy_foods):
    heat_greater_than5 = [food for food in spicy_foods if food.get('heat_level')>5]
    return heat_greater_than5
print (get_spiciest_foods(spicy_foods))

def print_spicy_foods(spicy_foods):
    formatted_foods = [
        f"{food.get('name', 'Unknown Food')} ({food.get('cuisine', 'Unknown Cuisine')}) | Heat Level: {'🌶' * food.get('heat_level', 0)}"
        for food in spicy_foods
    ]
    
    for formatted_food in formatted_foods:
        print(formatted_food)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    matching_foods = [food for food in spicy_foods if food.get('cuisine')== cuisine]
    if matching_foods:
        return matching_foods[0]
    else:
        return None
def print_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food.get('heat_level',0)>5]
    for food in spiciest_foods:
        name = food.get('name')
        cuisine = food.get('cuisine')
        heat_level = food.get('heat_level')
        emoji_heat = '🌶' * heat_level
        print(f'{name} ({cuisine}) | Heat Level: {emoji_heat}')
print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    heat_levels = [food.get('heat_level', 0) for food in spicy_foods]
    
    if heat_levels:
        return sum(heat_levels) // len(heat_levels)
    else:
        return 0 
print(get_average_heat_level(spicy_foods))

def create_spicy_food(spicy_foods, spicy_food):
    modified_spicy_foods = spicy_foods.copy()
    modified_spicy_foods.append(spicy_food)
    return modified_spicy_foods

