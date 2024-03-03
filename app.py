from flask import Flask, redirect, render_template, request, session, url_for
from flask import flash
from flask_session import Session
from cs50 import SQL
from flask import jsonify
from werkzeug.security import check_password_hash, generate_password_hash

# Configure app
app = Flask(__name__)

# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#  connection to my database
db = SQL("sqlite:///database.db")

@app.route('/')
def start_page():

    # render for home.html
    return render_template('index.html')


# Routes for home page
@app.route('/home')
def home():
    return render_template('index.html')


# route to the register


@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'admin' not  in session:
        return render_template("index.html")
    # mengecek register jika action dalam mode post
    elif request.method == 'POST':
        # mendapatkan username dan password serta email dati user
        username = request.form.get('username')
        password_before = request.form.get('password')
        email = request.form.get('email')

        if not username or username.strip() == '' :
            return render_template ("eror.html",  message="username cannot be empty or space")

        if not password_before or password_before.strip() == '' :
            return render_template ("eror.html", message="password cannot be empty or space")

        if not email or email.strip() == '' :
            return render_template ("eror.html", message="email cannot be empty or space")
        # mengecek apakah sudah ada user atau belum
        password = generate_password_hash(password_before)

        existing_user = db.execute("SELECT * FROM users WHERE username = :username",
                                   username=username)

        if existing_user:
            # User or email already exists
            return render_template ("eror.html", message="Username Has Used By Another User")
        else:
            # User and email are unique, perform registration
            db.execute("INSERT INTO users (username, password, email) VALUES (:username, :password, :email)",
                       username=username, password=password, email=email)
            user = db.execute("SELECT * FROM users WHERE username = ?", username)
            session['username'] = user
            return redirect("/success")
    # merender template
    return render_template('register.html')

# rute jika login sukses


@app.route("/success")
def success():
    if 'admin' not  in session:
        return render_template("index.html")
    return render_template("success.html", message="YOU SUCCESS REGISTER NEW USER")


# rute jika login tidak sukses


@app.route("/failed")
def failed():
    return render_template("eror.html",message="OOPS FAILED TO INPUT LETS TRY AGAIAN")

# rute untuk render login.html agar bisa di akses
@app.route("/vote_succes")
def vote_succes():
    return render_template("vote_succes.html",message="YOU SUCCES SEND YOUR CHOISE")

@app.route("/vote_failed")
def vote_failed():
    return render_template("vote_failed.html",message="OOPSS TRY AGAIN, OR YOU HAVE VOTED")

@app.route("/eror")
def eror ():
    return render_template("eror.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session.clear()
    # Handle login logic here
        username = request.form.get("username")
        password = request.form.get("password")
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)


    # Ensure username exists and password is correct
        if len(rows) == 1 and check_password_hash(rows[0]["password"], password):
            session['username'] = username  # Store the username in the session
            user_id = db.execute("SELECT id FROM users WHERE username = :username",
                             username=session['username'])[0]['id']
            has_voted = db.execute("SELECT has_voted FROM votes WHERE user_id = :user_id",
                               user_id=user_id)
            if has_voted and has_voted[0]['has_voted']:
                return render_template("login_has_vote.html")
            return render_template("login_success.html")  # Redirect to the login success page
        else:
            return render_template("eror.html",message="OOPS FAILED TO LOGIN CHECK YOUR PASSWORD OR USERNAME AGAIN")
    return render_template("login.html")



@app.route("/election_vote")
def election_vote():
    # Keamanan pemilihan agar hanya yang login bisa memilih
    if 'username' not in session:
        return render_template("login.html")  # Jika belum login, akan diarahkan ke halaman login

    # Mendapatkan informasi apakah pengguna sudah memilih
    user_id = db.execute("SELECT id FROM users WHERE username = :username",
                        username=session['username'])[0]['id']

    has_voted = db.execute("SELECT has_voted FROM votes WHERE user_id = :user_id",
                           user_id=user_id)

    user_has_voted = False
    if has_voted:
        user_has_voted = bool(has_voted[0]['has_voted'])

    return render_template("election_vote.html", user_has_voted=user_has_voted)

# logout user agar nantinya bisa user lain untuk masuk


@app.route("/logout")
def logout():
    # Hapus kunci sesi 'username'
    session.clear()
    # Redirect ke halaman login atau halaman lain yang sesuai
    return render_template("login.html")
# handel login admin


@app.route('/login_admin', methods=['GET', 'POST'])
def login_admin():
    if request.method == "POST":
        session.clear()
    # Handle login logic here
        username = request.form.get("username_admin")
        password = request.form.get("password_admin")
    # cek data admin di database
        admin = db.execute("SELECT * FROM admin WHERE username = :username AND password = :password",
                       username=username, password=password)
        if len(admin) == 1:
            session['admin'] = username  # Store the username in the session
            return redirect(url_for("admin_home"))  # Redirect to the editing the candidate, show result, and delete the candidate
        else:
             return render_template("eror.html", message="OPSS it is not the admin username and password")  # jika bukan admin akan menuju halaman login failed

# render halaman agar bisa di akses
    return render_template("login_admin.html")


@app.route("/admin_home")
def admin_home():
    return render_template("admin_home.html")

@app.route("/edit_candidates")
def edit_candidates():
    return render_template("edit_candidates.html")

# handel untuk mendaftarkan kandidat untuk di pilih


@app.route("/add_candidates", methods=['GET', 'POST'])
def add_candidates():
    if 'admin' not  in session:
        return render_template("index.html")
    # mengecek register jika action dalam mode post
    elif request.method == 'POST':
        # mendapatkan data-data untuk pemilih
        name = request.form.get('name')
        party = request.form.get('party')
        manifesto = request.form.get('manifesto')
        image_url = request.form.get('image_url')

        # menambahkan data tersebut ke dalam data base
        add = db.execute("INSERT INTO candidates (name, party, manifesto, image_url) VALUES (:name, :party, :manifesto, :image_url)",
                         name=name, party=party, manifesto=manifesto, image_url=image_url)
        if add:
            # User or email already exists
            return redirect(url_for('list_candidate'))
        else:
            # jika terjadi ke gagalan
            return "gagal"
    return render_template("add_candidates.html")

# daftar nama candidat


@app.route('/list_candidate')
def list_candidate():
    if 'admin' not  in session:
        return render_template("index.html")
    # Ambil data dari tabel candidates
    candidates = db.execute('SELECT * FROM candidates')

    # render halaman list_candidate, untuk tiap-tiap kandidat
    return render_template('list_candidate.html', candidates=candidates)

# menghaspus kandidat, methods di atur dalam mode POST



from flask import abort

@app.route('/delete_candidate/<int:id>', methods=['POST'])
def delete_candidate(id):
    if 'admin' not  in session:
        return render_template("index.html")
    try:
        # Delete candidate from the database
        db.execute('DELETE FROM candidates WHERE id = :id', id=id)
    except:
        return render_template("eror.html",message="OOPS FAILED TO DELETE CANDIDATE")
    # Render the list_candidate page
    return redirect(url_for('list_candidate'))


# mengedit kandidat method adalah GET dan POST, laman dimanis seusai dengan id dari kandidat


@app.route('/edit_candidate/<int:id>', methods=['GET', 'POST'])
def edit_candidate(id):
    if 'admin' not  in session:
        return render_template("index.html")
    elif request.method == 'GET':
        # Ambil data kandidat berdasarkan ID dari database
        candidate = db.execute('SELECT * FROM candidates WHERE id = :id', id=id)

        # render halaman sesuai dengan candidat dan nomor idnya
        return render_template('edit_candidate.html', candidate=candidate[0])

    # POST untuk update data
    elif request.method == 'POST':
        # Update data kandidat berdasarkan ID
        name = request.form['name']
        party = request.form['party']
        manifesto = request.form['manifesto']
        image_url = request.form['image_url']

        # update data baru ke database
        db.execute("UPDATE candidates SET name = :name, party = :party, manifesto = :manifesto WHERE id = :id",
                   name=name, party=party, manifesto=manifesto, id=id)
    # render list_candidate
    return redirect(url_for('list_candidate'))

######################   handeling voting      #########################
# menampilkan nama-nama kandidat


@app.route('/candidates')
def candidates():
    # mengecek sudah login atau belum dan masih ada dalam session
    if 'username' in session:
        # memanggil nama kandidat
        candidates = db.execute("SELECT * FROM candidates")
        # render halaman candidates
        return render_template('candidates.html', candidates=candidates)
    else:
        # jika belum login, dikembalikan ke halaman login
        return redirect(url_for("login"))

@app.route("/results")
def results():
    return render_template("results.html")

@app.route('/get_vote', methods=['POST'])
def get_vote():
    if 'username' in session:
        user_id = db.execute("SELECT id FROM users WHERE username = :username",
                             username=session['username'])[0]['id']
        candidate_id = request.json.get('candidate_id')

        has_voted = db.execute("SELECT has_voted FROM votes WHERE user_id = :user_id",
                               user_id=user_id)
        if has_voted and has_voted[0]['has_voted']:
            return jsonify({"error": "You've already chosen, so you can't choose again"})

        db.execute("INSERT INTO votes (user_id, candidate_id, has_voted) VALUES (:user_id, :candidate_id, 1)",
                   user_id=user_id, candidate_id=candidate_id)

        # Redirect ke halaman success.html dengan pesan sukses
        success_message = "Thank you for voting!"
        return jsonify({"success": success_message})
    else:
        return jsonify({"error": "please login "})

@app.route('/get_results')
def get_results():
    results = db.execute("""
    SELECT candidates.name, candidates.party,
           (SELECT COUNT(*)
            FROM votes
            WHERE votes.candidate_id = candidates.id AND votes.has_voted = 1) AS total_votes
    FROM candidates
    """)

    return jsonify(results)

@app.route('/admin_status')
def admin_status():
    if 'admin' not in session:
        return render_template("index.html")  # Redirect to login or another page

    # Get status of all users (voted or not voted)
    users_status = db.execute("""
        SELECT users.id, users.username, votes.has_voted
        FROM users
        LEFT JOIN votes ON users.id = votes.user_id
    """)

    return render_template("admin_status.html", users_status=users_status)

@app.route('/reset_vote/<int:user_id>', methods=['POST'])
def reset_vote(user_id):
    if 'admin' not in session:
        flash("You don't have permission to reset votes.", 'error')
        return redirect(url_for('admin_status'))

    try:
        # Delete rows in the votes table where has_voted is 1 for the specified user
        db.execute("DELETE FROM votes WHERE user_id = :user_id AND has_voted = 1", user_id=user_id)
        flash("Vote status reset successfully.")
    except Exception as e:
        print(f"Error resetting vote status: {e}")
        flash("Failed to reset vote status.")

    return redirect(url_for('admin_status'))

@app.route('/delete_user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    if 'admin' not in session:
        flash("You don't have permission to delete users.", 'error')
        return redirect(url_for('admin_status'))

    try:
        # Delete user from the users table
        db.execute("DELETE FROM users WHERE id = :user_id", user_id=user_id)
        flash("User deleted successfully.", 'success')
    except Exception as e:
        print(f"Error deleting user: {e}")
        flash("Failed to delete user.", 'error')

    return redirect(url_for('admin_status'))
