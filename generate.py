import sys


def page(slug, url):
    with open(slug + ".html", "w") as sys.stdout:
        print(f"<meta http-equiv='refresh' content='0;url={url}' />")


page("index", "https://github.com/libmath/math/issues/1")
page("wiki", "https://github.com/libmath/z/wiki")
page("stack", "https://github.com/libmath/math/issues/1")
