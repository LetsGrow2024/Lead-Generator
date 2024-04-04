from flask import Blueprint, render_template, request, jsonify
views = Blueprint (__name__, "views")


@views.route("/")
def home():
    return render_template("index.html",name="I am Tiffany and I am so glad you are hear"
                           ,about="For just one dollar per call we strive to generate new leads to help grow your business. Rather then spending time making cold calls allow us to take this burnden off of your shoulders. Simply provide the zip code in which you are trying to grow your business in and we will establish a list of businesses for us to cold call and sell them on your wonderful growing business")
@views.route("/profile")
def profile():
    args = request.args
    name = args.get('name')
    return render_template("index.html", name=name)

@views.route("/json")
def get_json():
    return jsonify({'name': 'Lets Grow Together', 'Leader in Business Growth': 10})