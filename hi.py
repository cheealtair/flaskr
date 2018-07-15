from flask import Flask, render_template
app = Flask(__name__)

@app.route('/froot')
def hiw():
    return 'Hellowab'


@app.route('/')
def main():
    #return 'Hello Main'
    return render_template("index.html")

@app.route('/test_render_template')
def ftest_test_render_image():
    return render_template("test_render_templateA.html")  # html file must be in 'templates' sub-directory

@app.route('/pass_template_variables')
def fpsas_template_variables():


    return render_template("page_pass_template_variables.html", username="myName")

# If this file is run by python.exe directly, then __name__ is set to '__main__'.
# If this file is run as a module, then __name__ is set to the name of the module.
if __name__ == '__main__':
    app.run()