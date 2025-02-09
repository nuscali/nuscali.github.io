import sys


z = {}

z["food"] = "https://azmobileapp.azurewebsites.net/stuffd/tabs/home?method=1&locationId=b805a6f0-0341-4f18-a7cf-b428568f666e&q=s"

for slug, url in z.items():
    with open(slug + ".html", "w") as sys.stdout:
        print(f"<meta http-equiv='refresh' content='0;url={url}' />")
