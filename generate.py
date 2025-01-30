import sys


z = {}

z["index"] = "https://github.com/libmath/math/issues/1"
z["wiki"] = "https://github.com/libmath/z/wiki"
z["stack"] = "https://github.com/libmath/math/issues/1"
z["mods"] = (
    "https://docs.google.com/spreadsheets/d/1_6HvZEyN8qOcKPjzuB2e7hyQtPOQKUUcr2r0WQdD99k/edit?gid=1740291173"
)

for slug, url in z.items():
    with open(slug + ".html", "w") as sys.stdout:
        print(f"<meta http-equiv='refresh' content='0;url={url}' />")
