from requests import get
from app import app
from flask import render_template, redirect, url_for
from image import is_image, save_image


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/edge_<number>")
def end(number):
    return render_template("end.html", number=number)


@app.route("/number_<number>")
def get_image_page(number):
    local_path = f"static/images/img_{number}.jpg"
    number = int(number)

    try:
        if not is_image(local_path):
            url = f"https://yandex.ru/images/search?text=цифра_{number}&from=tabbar"
            path = get(url).text
            path = "https://" + path.split("src=\"//")[1].split('"')[0]
            save_image(get(path).content, local_path)

        return render_template("basic_page.html", src=local_path, old_number=number, number=number + 1)
    except IndexError:
        return redirect(url_for("end", number=number))
