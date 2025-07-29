from src.local_packages_paths import LocalPackagesPaths
LocalPackagesPaths('windows')

from flask import Flask
import os

from blueprints.home import home
from blueprints.lesxon import lesxon

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = os.urandom(24)

# Register blueprints
app.register_blueprint(home.bp)
app.register_blueprint(lesxon.bp)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=1024)


