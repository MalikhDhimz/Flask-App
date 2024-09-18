<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Grade Calculator</title>
</head>
<body>
    <h1>Grade Calculator</h1>
    <form method="POST" action="/">
        <label for="prelim">Enter your Prelim Grade:</label>
        <input type="text" id="prelim" name="prelim" required>
        <input type="submit" value="Calculate">
    </form>

    {% if get_flashed_messages() %}
    <ul>
        {% for message in get_flashed_messages() %}
        <li>{{ message }}</li>
        {% endfor %}
    </ul>
    {% endif %}

    {% if prelim %}
    <h2>Results</h2>
    <p>Prelim Grade: {{ prelim }}</p>
    <p>Required Midterm Grade: {{ midterm_grade }}</p>
    <p>Required Final Grade: {{ final_grade }}</p>
    <p>{{ pass_status }}</p>
    <p>To be a Dean’s Lister, you need:</p>
    <ul>
        <li>Midterm: {{ dl_midterm }}</li>
        <li>Final: {{ dl_final }}</li>
    </ul>
    {% endif %}
</body>
</html>

