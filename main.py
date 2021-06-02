from flask import Flask, render_template
import requests
from post import Post

blog_url = "https://api.npoint.io/5c8481429e622108ecd0"
response = requests.get(url = blog_url)
all_posts = response.json()
post_objects = []
for post in all_posts:
    post_objects.append(post)
print(post_objects)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts = all_posts)

@app.route('/post/<int:index>')
def read_blog_post(index):
    requested_post = None 
    for number_of_blogpost in post_objects:
        print(number_of_blogpost)
        print(number_of_blogpost["id"])
        if number_of_blogpost["id"] == index:
            requested_post = number_of_blogpost
    return render_template("post.html", post= requested_post)

if __name__ == "__main__":
    app.run(debug=True)