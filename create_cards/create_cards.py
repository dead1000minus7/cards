import os
from flask import Blueprint, render_template, flash, request, redirect, url_for, abort
from cards.models import Cards
import uuid

create_cards_bp = Blueprint("create_cards", __name__, template_folder="templates")

UPLOAD_FOLDER = os.path.join("img", "cards")


@create_cards_bp.route("/create_cards",methods=["GET", "POST"])
def create_cards():
    if request.method == "POST":

        print(request.form["title_card"])
        print(request.form["description_card"])
        print(request.form["class_card"])
        print(request.form["type_card"])
        print(request.form["rare_card"])
        print(request.form["attack_card"])
        print(request.form["mana_card"])
        print(request.form["life_card"])

        file = request.files["file"]

        file_extensions = file.filename

        print(file_extensions)

        file.filename = f'{uuid.uuid4()}.{file.filename.split(".")[-1].lower()}'

        file.save(os.path.join("static", UPLOAD_FOLDER, file.filename))

        create_cards = Cards(title_card=request.form["title_card"],description_card=request.form["description_card"],
                             class_card=request.form["class_card"],type_card=request.form["type_card"],rare_card=request.form["rare_card"],
                             attack_card=request.form["attack_card"],mana_card=request.form["mana_card"],life_card=request.form["life_card"]
                             )


        #create_cards = Cards()


    class_card = ["Strength", "Intelligence", "Willpower", "Agility", "Endurance", "Netural","Archer","Assassin",
                  "Battlemage","Crusader","Mage","Monk","Scout","Sorcerer","Spellsword","Warrior"]

    type_card = ["Creature", "Action", "Item", "Support"]

    rare_card = ["Legendary", "Epic", "Rare", "Common"]

    attack_card = [x for x in range(0, 16)]

    mana_card = [x for x in range(0, 16)]

    life_card = [x for x in range(0, 13)]

    return render_template("create_cards.html", class_card=class_card, type_card=type_card, rare_card=rare_card,
                           attack_card=attack_card, mana_card=mana_card, life_card=life_card)
