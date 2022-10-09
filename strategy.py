import json
import sys

def imageGenerator(context, version="", variant=""):
    variant = version and variant and f"{version}-{variant}" or version or variant or "latest"
    return f"{context}:{variant}"

matrix = {
    "include": []
}

if len(sys.argv) > 1:
    input = json.loads(sys.argv[1])

    images = [{
        "context": input.get("context"),
        "versions": input.get("versions").split(";"),
        "variants": input.get("variants").split(";")
    }]
else:
    images = json.load(open("supported.json", "r"))

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

print("::set-output name=matrix::{}".format(json.dumps(matrix)))
