import json


matrix = {
    "include": [
        {
            "context": "hasura-cli",
            "args": "",
            "image": "hasura-cli:latest"
        },
        {
            "context": "hasura-cli",
            "args": "VERSION=v2.12.0\n",
            "image": "hasura-cli:v2.12.0"
        },

        {
            "context": "hasura-cli/distroless",
            "args": "",
            "image": "hasura-cli:distroless"
        },
        {
            "context": "hasura-cli/distroless",
            "args": "v2.12.0\n",
            "image": "hasura-cli:v2.12.0-distroless"
        },

        {
            "context": "hasura-wait4x",
            "args": "",
            "image": "hasura-wait4x:latest"
        },
        {
            "context": "hasura-wait4x",
            "args": "v2.12.0\n",
            "image": "hasura-wait4x:v2.12.0"
        },
    ]
}

print("::set-output name=matrix::{}".format(json.dumps(matrix)))
