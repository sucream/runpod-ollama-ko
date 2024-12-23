import runpod
from typing import Any, TypedDict
import requests
import sys


class HandlerInput(TypedDict):
    """The data for calling the Ollama service."""

    method_name: str
    """The url endpoint of the Ollama service to make a post request to."""

    input: Any
    """The body of the post request to the Ollama service."""


class HandlerJob(TypedDict):
    input: HandlerInput


def handler(job: HandlerJob):
    base_url = "http://localhost:11434"
    input = job["input"]

    # streaming is not supported in serverless mode
    input["stream"] = False
    print(sys.argv)
    model = sys.argv[1]

    response = requests.post(
        url=f"{base_url}{input['api']}",
        headers={"Content-Type": "application/json"},
        json=input["json"],
    )
    response.encoding = "utf-8"

    # TODO: handle errors
    return response.json()


runpod.serverless.start({"handler": handler})
