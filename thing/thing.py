from flask import Flask, redirect, request
app = Flask(__name__,static_url_path="/static", static_folder=".")

@app.route('/')
def index():
	return str(request.args.get("inputText")).upper()

if __name__ == '__main__':
	app.run('198.110.204.9', 5999, debug = True)
