from flask import Flask
app = Flask(__name__)  # Note the double underscores on each side!

from flask import render_template # import the render_template for use with html
app = Flask(__name__)

# returns the rendered index.html template
@app.route("/") # connects that function with the root URL of our site,/
def index():
    template = 'index.html'
    return render_template(template)

if __name__ == '__main__':
    # Fire up the Flask test server
    app.run(debug=True, use_reloader=True)

