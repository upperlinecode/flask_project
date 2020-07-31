
def user_course(course):
    if course.lower() == "breakfast":
        return "You chose breakfast."
    elif course.lower() == "lunch":
        return "You chose lunch."
    elif course.lower() == "dinner":
        return "You chose dinner."
    else:
        return "That wasn't an option..."
        
def user_meat(meat):
    if meat:
        return "Do you want breakfast, lunch or dinner?"
    else:
        return "you are not in the mood for meat."

def user_recipe(recipe):
    if recipe:
        return "Do you want breakfast, lunch or dinner?"
    else:
        return "you are not in the mood for meat."

def user_health(health):
    if health.lower() == "savory":
        return "Savory it is!"
    elif health.lower() == "sweet":
        return "Sweet it is!"
    else:
        return "That wasn't an option..."

def user_recipe(user_meat, user_course, user_health):
    if user_meat == "yes":
        if user_course == "breakfast":
            if user_health == "savory":
                return "https://www.foodnetwork.com/recipes/food-network-kitchen/breakfast-burritos-with-chorizo-3677254"
            elif user_health == "sweet":
                return "https://www.seriouseats.com/recipes/2017/12/bravetart-homemade-cinnamon-rolls-recipe.html"
        elif user_course == "dinner":
            if user_health == "savory":
                return "https://www.foodandwine.com/recipes/bacon-and-kimchi-burgers"
            elif user_health == "sweet":
                return "https://ohsweetbasil.com/cookies-and-cream-red-velvet-molten-lava-cakes-recipe/"
        elif user_course == "lunch":
            if user_health == "savory":
                return "https://natashaskitchen.com/fish-tacos-recipe/"
            elif user_health == "sweet":
                return "https://www.allrecipes.com/recipe/49943/grilled-peanut-butter-and-jelly-sandwich/"
    elif user_meat == "no":
        if user_course == "breakfast":
            if user_health == "savory":
                return "https://www.foodnetwork.com/recipes/food-network-kitchen/avocado-toasts-3364588"
            elif user_health == "sweet":
                return "https://cookieandkate.com/whole-wheat-banana-pancakes-recipe/"
        elif user_course == "dinner":
            if user_health == "savory":
                return "https://www.feastingathome.com/orecchiette-pasta-with-broccoli-sauce/"
            elif user_health == "sweet":
                return "https://minimalistbaker.com/banana-cream-pie-vegan-gf/"
        elif user_course == "lunch":
            if user_health == "savory":
                return "https://www.acouplecooks.com/coleslaw-swiss-cheese-melt-sandwich/"
            elif user_health == "sweet":
                return "https://cookieandkate.com/vegan-mac-and-cheese-recipe/"
