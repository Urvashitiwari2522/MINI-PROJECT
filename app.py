from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/admin-login', methods=['GET', 'POST'])
def admin_login():
    error = None
    if request.method == 'POST':
        admin_id = request.form.get('admin_id')
        password = request.form.get('password')
        if admin_id == 'admin' and password == 'admin123':
            return redirect(url_for('home'))
        else:
            error = "Incorrect Admin ID or Password"
    return render_template('admin_login.html', error=error)


@app.route('/student-login', methods=['GET', 'POST'])
def student_login():
    error = None
    if request.method == 'POST':
        student_id = request.form.get('student_id')
        password = request.form.get('password')
        if student_id == 'student' and password == 'student123':
            return redirect(url_for('home'))
        else:
            error = "Incorrect Student ID or Password"
    return render_template('student_login.html', error=error)


@app.route('/admin-forgot-password', methods=['GET', 'POST'])
def admin_forgot_password():
    error = success = None
    if request.method == 'POST':
        admin_id = request.form.get('admin_id')
        # Dummy check - replace with actual admin verification and email sending
        if admin_id == 'admin':
            success = "Password reset instructions have been sent to your registered email."
        else:
            error = "Admin ID not found."
    return render_template('admin_forgot_password.html', error=error, success=success)


@app.route('/student-forgot-password', methods=['GET', 'POST'])
def student_forgot_password():
    error = success = None
    if request.method == 'POST':
        student_id = request.form.get('student_id')
        # Dummy check - replace with actual student verification and email sending
        if student_id == 'student':
            success = "Password reset instructions have been sent to your registered email."
        else:
            error = "Student ID not found."
    return render_template('student_forgot_password.html', error=error, success=success)


@app.route('/guest-query', methods=['GET', 'POST'])
def guest_query():
    success = None
    if request.method == 'POST':
        name = request.form.get('guest_name')
        email = request.form.get('guest_email')
        query = request.form.get('guest_query')
        success = "Your query has been sent successfully!"
    return render_template('guest_query.html', success=success)


if __name__ == "__main__":
    app.run(debug=True)
