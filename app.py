from flask import Flask, render_template

app = Flask(__name__)

ads_enabled = False  # Global flag for ad control

@app.route("/")
def index():
    global ads_enabled
    return render_template("index.html", ads_enabled=ads_enabled)

@app.route("/toggle_ads/<action>")
def toggle_ads(action):
    global ads_enabled
    if action == "start":
        ads_enabled = True
    elif action == "stop":
        ads_enabled = False
    return f"Ads {'enabled' if ads_enabled else 'disabled'}!"

if __name__ == "__main__":
    app.run(debug=True)
