from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import os

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")


# Route to render index.html template using data from Mongo
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars = mars)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    
    mars = mongo.db.mars
    
    # Run the scrape function
    mars_collection = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.mars.update({}, mars_collection, upsert=True)

    # Redirect back to home page
    return redirect("/")
#     return redirect("http://localhost:5000/", code=302)


if __name__ == "__main__":
    
#     app.run(host=os.getenv('IP', '0.0.0.0'), 
#             port=int(os.getenv('PORT', 4444)))
    app.run(debug=True)


  


