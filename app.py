from flask import Flask, request, redirect
from datetime import datetime, timezone

app = Flask(__name__)

@app.route("/")
def home():
    visitor_ip = request.remote_addr
    visit_time = datetime.now(timezone.utc).isoformat()

    app.logger.info(
        "Homepage visit: ip=%s time=%s",
        visitor_ip,
        visit_time
    )

    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Visitor Redirect Demo</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body style="font-family: Arial; max-width: 600px; margin: 60px auto; padding: 20px;">
        <h1>Welcome</h1>
        <p>
            Redirecting to Chime
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

if __name__ == "__main__":
    app.run()
