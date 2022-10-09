import json


matrix = {
    "include": [
        {
            "context": "hasura-cli",
            "image": "hasura-cli:latest"
        },
        {
            "context": "hasura-cli",
            "args": "VERSION=v2.12.0\n",
            "image": "hasura-cli:v2.12.0"
        },

        {
            "context": "hasura-cli",
            "target": "distroless",
            "image": "hasura-cli:distroless"
        },
        {
            "context": "hasura-cli",
            "target": "distroless",
            "args": "v2.12.0\n",
            "image": "hasura-cli:v2.12.0-distroless"
        },

        {
            "context": "hasura-cli",
            "target": "distroless-nonroot",
            "image": "hasura-cli:distroless-nonroot"
        },
        {
            "context": "hasura-cli",
            "target": "distroless-nonroot",
            "args": "v2.12.0\n",
            "image": "hasura-cli:v2.12.0-distroless-nonroot"
        },

        {
            "context": "hasura-wait4x",
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
