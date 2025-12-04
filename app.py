from flask import Flask, render_template, request, redirect, send_file
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import csv
import os

app = Flask(__name__)

# ============= DATABASE CONFIG =============
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(BASE_DIR, "waste.db")

app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ============= MODEL =============
class WasteEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# ============= BADGE SYSTEM =============
def get_badge(category, amount):
    if amount >= 5:
        return f"{category} Ustası 🏅"
    elif amount >= 2:
        return f"{category} Destekçisi ⭐"
    else:
        return f"{category} Başlangıç Rozeti 🎉"


# ============= ROUTES =============

@app.route("/")
def index():
    return render_template("index.html", title="Ana Sayfa")


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form["name"]
        date = request.form["date"]
        category = request.form["category"]
        amount = float(request.form["amount"])

        badge = get_badge(category, amount)

        new_entry = WasteEntry(
            name=name,
            date=date,
            category=category,
            amount=amount
        )

        db.session.add(new_entry)
        db.session.commit()

        return render_template("success.html", badge=badge)

    return render_template("add.html", title="Atık Ekle")


@app.route("/records")
def records():
    all_records = WasteEntry.query.order_by(WasteEntry.id.desc()).all()
    return render_template("records.html", records=all_records, title="Kayıtlar")


@app.route("/delete/<int:id>")
def delete(id):
    record = WasteEntry.query.get(id)
    db.session.delete(record)
    db.session.commit()
    return redirect("/records")


@app.route("/stats")
def stats():
    entries = WasteEntry.query.all()

    categories = ["Plastik", "Kağıt", "Cam", "Metal", "Organik"]
    amounts = []

    for cat in categories:
        total = sum(e.amount for e in entries if e.category == cat)
        amounts.append(total)

    return render_template("stats.html", categories=categories, amounts=amounts)


@app.route("/export")
def export():
    entries = WasteEntry.query.all()
    file_path = "waste_export.csv"

    with open(file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "İsim", "Tarih", "Kategori", "Miktar(kg)"])

        for e in entries:
            writer.writerow([e.id, e.name, e.date, e.category, e.amount])

    return send_file(file_path, as_attachment=True)


@app.route("/admin")
def admin():
    all_records = WasteEntry.query.order_by(WasteEntry.id.desc()).all()
    return render_template("admin.html", records=all_records)


@app.route("/about")
def about():
    return render_template("about.html", title="Hakkında")


# ============= RUN APP =============
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5001)
