import json
import os

def imageGenerator(context, version="", variant=""):
    variant = version and variant and f"{version}-{variant}" or version or variant or "latest"
    return f"{context}:{variant}"

matrix = {
    "include": []
}

if os.getenv("context"):
    images = [{
        "context": os.getenv("context"),
        "versions": os.getenv("versions").split(";") if os.getenv("versions") else [],
        "variants": os.getenv("variants").split(";") if os.getenv("variants") else []
    }]
else:
    images = json.load(open("supported.json", "r"))

print(f"[DEBUG] Images: {images}")

for image in images:
    context = image.get("context")
    versions = [""] + image.get("versions", [])
    variants = [""] + image.get("variants", [])

    for variant in variants:
        for version in versions:
            matrix["include"].append({
                "context": context,
                "args": f"VERSION={version}\n" if version else "",
                "target": variant,
                "image": imageGenerator(context, version, variant)
            })

print("matrix={}".format(json.dumps(matrix)))
