import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, MappedAsDataclass
from sqlalchemy import Integer, String, Boolean

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(MappedAsDataclass, DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, init=False)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    # def to_dict(self):
        # dictionary = {}
        # for column in self.__table__.columns:
        #     dictionary[column.name] = getattr(self, column.name)
        # return dictionary
        # return {column.name: getattr(self, column.name) for column in self.__table__.columns}

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

# HTTP GET - Read Record

@app.route("/random")
def rand():
    result = db.session.execute(db.select(Cafe))
    cafes = result.scalars().all()
    choice = random.choice(cafes)
    # cafe = jsonify(cafe={
    #     "id": choice.id,
    #     "name": choice.name,
    #     "map_url": choice.map_url,
    #     "img_url": choice.img_url,
    #     "location": choice.location,
    #     "seats": choice.seats,
    #     "has_toilet": choice.has_toilet,
    #     "has_wifi": choice.has_wifi,
    #     "has_sockets": choice.has_sockets,
    #     "can_take_calls": choice.can_take_calls,
    #     "coffee_price": choice.coffee_price,
    # })
    return jsonify(cafe=choice)

@app.route("/all")
def all():
    result = db.session.execute(db.select(Cafe))
    return jsonify(cafes=[cafe for cafe in result.scalars().all()])

@app.route("/search")
def search():
    loc = request.args.get("loc")
    result = db.session.execute(db.select(Cafe).where(Cafe.location == loc))
    cafes = [cafe for cafe in result.scalars().all()]
    if not cafes:
        return jsonify(error={"Not found" : "No cafe at location"}), 404
    else:
        return jsonify(cafes=cafes)


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add():
    new_cafe = Cafe(
        name = request.form.get("name"),
        map_url = request.form.get("map_url"),
        img_url = request.form.get("img_url"),
        location = request.form.get("location"),
        has_sockets = bool(request.form.get("has_sockets")),
        has_toilet = bool(request.form.get("has_toilet")),
        has_wifi = bool(request.form.get("has_wifi")),
        can_take_calls = bool(request.form.get("can_take_calls")),
        seats = request.form.get("seats"),
        coffee_price = request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Added cafe"}), 201


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    if not new_price:
        return jsonify(error={"Bad Request" : "Missing coffee price"}), 400
    cafe = db.get_or_404(Cafe, cafe_id, description="Cafe id not found")
    cafe.coffee_price = new_price
    db.session.commit()
    return jsonify(response={"success": "Updated cafe coffee price"}), 200

@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error={"Not found": str(e)}), 404


# HTTP DELETE - Delete Record

@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def report_closed(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "testing123":
        cafe = db.get_or_404(Cafe, cafe_id, description="Cafe id not found")
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(response={"success": "Report closed cafe"}), 200
    else:
        return jsonify(error={"Unauthorized" : "Incorrect api-key"}), 401


if __name__ == '__main__':
    app.run(debug=True)
