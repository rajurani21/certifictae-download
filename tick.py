from flask import Flask, request, render_template_string

app = Flask(__name__)

# User data (Name → PIN & Certificate Link)
users = {
    "John Doe": {"pin": "1234", "certificate_link": "https://drive.google.com/uc?export=download&id=ABC123">Click here to Download</a>
"},
    "Jane Smith": {"pin": "5678", "certificate_link": "https://drive.google.com/file/d/XYZ456/view"}
}

# HTML Template (No need for separate `index.html`)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Certificate Download</title>
</head>
<body>
    <h2>Enter Your Name & PIN to Download Your Certificate</h2>
    <form action="/" method="POST">
        <input type="text" name="name" placeholder="Enter your Name" required><br><br>
        <input type="password" name="pin" placeholder="Enter your PIN" required><br><br>
        <button type="submit">Get Certificate</button>
    </form>
    <br>
    {% if message %}
        <h3>{{ message | safe }}</h3>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    message = None
    if request.method == 'POST':
        name = request.form.get("name")
        pin = request.form.get("pin")

        # Check if Name & PIN match
        if name in users and users[name]["pin"] == pin:
            message = f"✅ Certificate Found! <br> <a href='{users[name]['certificate_link']}' target='_blank'>Click here to Download</a>"
        else:
            message = "❌ Invalid Name or PIN!"

    return render_template_string(HTML_TEMPLATE, message=message)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Certificate Download Page"

@app.route('/download')
def download():
    return "This is the download page."

if __name__ == '__main__':
    app.run(debug=True)
