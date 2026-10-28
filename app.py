from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Visitor Redirect Demo</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body style="font-family: Arial; max-width: 600px;
                 margin: 60px auto; padding: 20px;">

        <h1>Welcome</h1>

        <p>
            This demonstration may record your connection IP address
            and visit time for website diagnostics.
        </p>

        <button onclick="location.href='/continue'">
            Continue to Chime
        </button>

    </body>
    </html>
    """

@app.route("/continue")
def continue_to_site():
    return redirect("https://www.chime.com", code=302)

@app.route("/visit")
def record_visit():
    ip = request.remote_addr
    print("Visitor IP:", ip)
    return {"message": "Visit recorded for testing"}

if __name__ == "__main__":
    app.run()
