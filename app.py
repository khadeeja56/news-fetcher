from flask import Flask, render_template
from news_fetcher import fetch_headlines

app = Flask(__name__)

@app.route('/')
def home():
    headlines = fetch_headlines()
    return render_template('index.html', headlines=headlines)

if __name__ == '__main__':
    app.run(debug=True)




