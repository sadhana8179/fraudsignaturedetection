from flask import Flask, render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
from database.database import init_db, save_result, get_all_results

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Initialize DB
init_db()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/comparison', methods=['GET', 'POST'])
def comparison():
    result = None
    if request.method == 'POST':
        original = request.files.get('original')
        test = request.files.get('test')

        if not original or not test:
            flash("Please upload both images.")
            return redirect(request.url)

        orig_filename = secure_filename(original.filename)
        test_filename = secure_filename(test.filename)

        orig_path = os.path.join(app.config['UPLOAD_FOLDER'], orig_filename)
        test_path = os.path.join(app.config['UPLOAD_FOLDER'], test_filename)

        original.save(orig_path)
        test.save(test_path)

        # Simulate similarity score
        import random
        similarity = random.uniform(50, 100)

        save_result(orig_filename, test_filename, similarity)

        # Determine result message
        if similarity >= 80:
            result = f"✅ Match! Similarity Score: {similarity:.2f}%"
        else:
            result = f"❌ Forgery Detected! Similarity Score: {similarity:.2f}%"

    return render_template('comparison.html', result=result)


@app.route('/dashboard')
def dashboard():
    results = get_all_results()
    return render_template('dashboard.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)


