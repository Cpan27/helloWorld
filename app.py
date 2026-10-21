from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Cassie Pan! I am adding my first code change.'

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about-css')
def about_css():
    return render_template('about-css.html')

@app.route('/favorite-course')
def favorite_course():
    subject=request.args.get('subject')
    course_number=request.args.get('course_Number')
    return render_template('favorite-course.html', subject=subject, course_number=course_number)

@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        print('First name entered: ' + request.form.get('first_name'))
        print('Middle initial entered: ' + request.form.get('middle_initial'))
        print('Last name entered: ' + request.form.get('last_name'))
        print('Email address entered: ' + request.form.get('email'))
        return render_template('contact.html', form_submitted=True)
    return render_template('contact.html')

if __name__ == '__main__':
    app.run()
