from flask import Flask, render_template, redirect, request
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

# --- Testing Tools ----------------------------------
from flask_debugtoolbar import DebugToolbarExtension
# ----------------------------------------------------

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# --- Testing Configs that can be removed ------------
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'IAHHETINihaie837472'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)
# ----------------------------------------------------

connect_db(app)
db.drop_all()
db.create_all()


# ======= Routes ================
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


@app.route('/')
def display_pets_home():
    '''Landing page for pets adoption app'''

    pets = Pet.query.all()

    return render_template('index.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    '''Add a pet to database'''

    form = AddPetForm()

    if request.method == "POST":
        name = request.form['name']
        species = request.form['species']
        photo = request.form['photo_url']
        if not photo:
            photo = None
        age = request.form['age']
        notes = request.form['notes']

        new_pet = Pet(name=name, species=species, photo_url=photo, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()

        return redirect('/')

    else:
        return render_template('add_pet.html', form=form)


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit pet."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        return redirect('/')

    else:
        return render_template("edit_pet.html", form=form, pet=pet)





# ======================================================
# ---------------Seeds ----------------------------
# ======================================================

p1 = Pet(name='Roofus', species='German Shepard')
p2 = Pet(name='Henry', species='Cat', photo_url='https://upload.wikimedia.org/wikipedia/commons/7/76/TapetumLucidum.JPG')
p3 = Pet(name='Darla', species='Tabby Cat', age=3, notes='She was surrendered with her brother Steven')
p4 = Pet(name='Steven', species='Black Cat', age=3, available=False)
p5 = Pet(name='Daisy', species='Beagle', age=1, available=False)
p6 = Pet(name='Harold', species='Chocolate Lab', age=9, notes='Needs a home where he can be the only pet')

db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.add(p4)
db.session.add(p5)
db.session.add(p6)
db.session.commit()
