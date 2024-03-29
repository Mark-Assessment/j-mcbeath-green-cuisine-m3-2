# Import of modules
import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
# Check that env.py file exists
if os.path.exists("env.py"):
    import env


# Create a Flask instance & set MongoDB variables
app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
# Create a PyMongo instance 
mongo = PyMongo(app)


# Define routes
@app.route("/")
def home():
    return render_template('home.html')


@app.route("/all_recipes", methods=["GET", "POST"])
def all_recipes():
    if request.method == "POST":
        recipe_type = request.form.get("recipe_type")
        if recipe_type == "all":
            recipes = list(mongo.db.recipes.find())
        else:
            recipes = list(mongo.db.recipes.find({"recipe_type": recipe_type}))
    else:
        recipes = list(mongo.db.recipes.find())

    return render_template("all_recipes.html", recipes=recipes)


@app.route("/submit_recipe", methods=["GET", "POST"])
def submit_recipe():
    if request.method == "POST":
        recipe_type = request.form.get("recipe_type")
        if recipe_type == "all Recipe Types":
            recipes = list(mongo.db.recipes.find())
        else:
            recipes = list(mongo.db.recipes.find({"recipe_type": recipe_type}))
    else:
        recipes = list(mongo.db.recipes.find())

    return render_template("all_recipes.html", recipes=recipes)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({
            "$text": {"$search": query}}))
    return render_template("all_recipes.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # Check username is in database
        if existing_user:
            flash("Username already exists - Please use a different username!")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # Put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user", None)
    return redirect(url_for("login"))


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe_type = request.form.get("recipe_type")
        if not recipe_type:
            recipe_type = 'All'
        recipe = {
            "recipe_title": request.form.get("recipe_title"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "cooking_instructions": request.form.get("cooking_instructions"),
            "cooking_time": request.form.get("cooking_time"),
            "recipe_type": request.form.get("recipe_type")
        }
        mongo.db.recipes.insert_one(recipe)
        print(request.form)
        flash("Recipe added successfully")
        # Fetch all recipes again, including the newly added one
        recipes = list(mongo.db.recipes.find())
        return render_template("all_recipes.html", recipes=recipes)
    return render_template("add_recipe.html")


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        submit = {
            "recipe_title": request.form.get("recipe_title"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "cooking_instructions": request.form.get("cooking_instructions"),
            "cooking_time": request.form.get("cooking_time"),
            "recipe_type": request.form.get("recipe_type")
        }
        mongo.db.recipes.update_one(
            {"_id": ObjectId(recipe_id)}, {"$set": submit})
        flash("Recipe edited successfully")

        # Fetch all recipes again, including the newly added one
        recipes = list(mongo.db.recipes.find())

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("edit_recipe.html", recipe=recipe)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
    flash("Recipe deleted successfully")
    return redirect(url_for("all_recipes"))


# Run the app
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
