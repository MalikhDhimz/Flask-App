from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "secret_key"

# Validate if input is a number between 0-100
def validate_prelim_grade(prelim):
    try:
        grade = float(prelim)
        if 0 <= grade <= 100:
            return True, grade
        else:
            return False, "Grade should be between 0 and 100."
    except ValueError:
        return False, "Invalid input. Please enter a number."

# Function to calculate required midterm and final grades
def calculate_required_grades(prelim_grade):
    passing_grade = 75
    required_midterm = (passing_grade - (prelim_grade * 0.2)) / 0.8 * 0.3
    required_final = (passing_grade - (prelim_grade * 0.2)) / 0.8 * 0.5

    # Dean's lister criteria (90%+ overall grade)
    dean_lister_midterm = (90 - (prelim_grade * 0.2)) / 0.8 * 0.3
    dean_lister_final = (90 - (prelim_grade * 0.2)) / 0.8 * 0.5

    return required_midterm, required_final, dean_lister_midterm, dean_lister_final

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        prelim = request.form["prelim"]
        is_valid, prelim_grade_or_error = validate_prelim_grade(prelim)
        
        if not is_valid:
            flash(prelim_grade_or_error)
            return redirect(url_for('index'))
        
        prelim_grade = prelim_grade_or_error
        midterm_grade, final_grade, dl_midterm, dl_final = calculate_required_grades(prelim_grade)

        # Determine if the student can still pass
        if prelim_grade < 75:
            pass_status = "It is difficult to pass."
        else:
            pass_status = "You have a chance to pass!"

        return render_template("index.html", 
                               prelim=prelim_grade,
                               midterm_grade=midterm_grade,
                               final_grade=final_grade,
                               pass_status=pass_status,
                               dl_midterm=dl_midterm,
                               dl_final=dl_final)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
