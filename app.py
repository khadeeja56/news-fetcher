from news_fetcher import fetch_headlines
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def home():
    headlines = fetch_headlines()
    print(headlines)  # Check if the headlines are being fetched
    return render_template('index.html', headlines=headlines)
if __name__ == "__main__":
    app.run(debug=True)



