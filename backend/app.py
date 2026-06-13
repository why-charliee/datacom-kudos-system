from flask import Flask # type: ignore

app = Flask(__name__)

# Register blueprints
try:
    from routes import kudos_routes  # type: ignore
    app.register_blueprint(kudos_routes, url_prefix="/kudos")
except Exception:
    # If running in a context where imports differ, skip registration
    pass

@app.route("/")
def home():
    return "Kudos System Running"

if __name__ == "__main__":
    app.run(debug=True)