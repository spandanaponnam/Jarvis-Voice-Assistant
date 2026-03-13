import pyjokes
import random
valid_categories = ["all", "neutral", "chuck"]
category = input(f"Choose joke category {valid_categories}: ").strip().lower()
if category not in valid_categories:
    print(f"Invalid category! Using 'all' instead.")
    category = "all"
joke=pyjokes.get_jokes(language="en",category =category)
random_j=random.choice(joke)
print("Here is a joke for you:\n",random_j)
