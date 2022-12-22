from model import db, User, Recipe, Ingredient, connect_to_db


def create_user(name, email, password):
    """Create and return a new user."""
    user = User(name=name, email=email, password=password)
    return user


def get_user():
    """Return all users."""
    return User.query.all()


def get_user_by_id(user_id):
    """Return a user by primary key."""
    return User.query.get(user_id)


def get_user_by_email(email):
    """Return a user by email."""
    return User.query.filter(User.email == email).first()


def get_user_by_name(name):
    """Return a user by name."""
    return User.query.filter(User.name == name).first()


def create_recipe(title, summary, instructions, ingredients, image_url):
    """Create and return a new recipe."""
    recipe = Recipe(
        recipe_name=title,
        description=summary,
        direction=instructions,
        ingredients=ingredients,
        image_url=image_url,
    )

    return recipe


def get_all_recipes():
    """Return all recipes."""
    return Recipe.query.all()


def get_recipe_by_name(recipe_name):
    """Return all recipe by name."""
    return Recipe.query.filter(Recipe.recipe_name).all()


def get_recipe_by_id(recipe_id):
    """Return a recipe by primary key."""
    return Recipe.query.get(recipe_id)


def get_recipe_by_direction(direction):
    """Return all recipes by instructions."""
    return Recipe.query.get(direction)


if __name__ == "__main__":
    from server import app

    connect_to_db(app)