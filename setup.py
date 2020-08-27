from flask import Flask, jsonify, request, render_template, redirect
import random
from mailjet_rest import Client

api_key = 'd64116652c3d342f88ee0b559f988549'
api_secret = '45bd6bd40733e6d8bb67333808f94710'
mailjet = Client(auth=(api_key, api_secret), version='v3.1')

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)

@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def home():
  if request.method == 'GET':
      return render_template('index.html')
  else:
    name = request.form['Name']
    email = request.form['Email']
    data = {
    'Messages': [
        {
          "From": {
            "Email": "yossitz1302@gmail.com",
            "Name": "yossi"
          },
          "To": [
            {
              "Email": "yz1356@sm.amalnet.k12.il",
              "Name": "yossi"
            }
          ],
          "Subject": "Student joined edmodo",
          "TextPart": "Student: " + name + " joined with email: " + email,
        }
      ]
    }
    result = mailjet.send.create(data=data)
    print (result.status_code)
    print (result.json())
    return redirect("https://new.edmodo.com/login?utm_source=main&utm_campaign=logged-out-pages&utm_medium=visitor-site&utm_content=landing-page-topnav", code=302)


@app.route('/donate', methods=['GET', 'POST'])
def donate():
  if request.method == 'GET':
      return render_template('donate.html')
  else:
    name = request.form['Name']
    email = request.form['Email']
    return redirect("https://new.edmodo.com/login?utm_source=main&utm_campaign=logged-out-pages&utm_medium=visitor-site&utm_content=landing-page-topnav", code=302)


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
		port=random.randint(2000, 9000),  # Randomly select the port the machine hosts on.
    debug=True
	)