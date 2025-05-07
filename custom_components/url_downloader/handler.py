from json import JSONDecodeError

import requests
from homeassistant.exceptions import ServiceValidationError


class HandleRequest:
    @classmethod
    def factory(cls, method):
        return cls(method)

    def __init__(self, method):
        self.method = method

    def __call__(self, call, *args, **kwargs):
        url = call.data.get("url", None)
        headers = call.data.get("headers", {})
        params = call.data.get("params", None)
        payload = call.data.get("payload", None)
        content_type = call.data.get("content_type", None)

        requests_method = getattr(requests, self.method, None)
        requests_kwargs = {}

        if not requests_method:
            raise ServiceValidationError(
                f"Method '{self.method}' is not a valid requests function"
            )

        headers["User-Agent"] = self.user_agent

        if content_type:
            headers["Content-Type"] = content_type

        if params:
            requests_kwargs["params"] = params

        if payload and ((content_type and "json" in content_type) or not content_type):
            requests_kwargs["json"] = payload
        elif payload:
            requests_kwargs["data"] = payload

        response = requests_method(url, headers=headers, **requests_kwargs)
        response.raise_for_status()

        try:
            return response.json()
        except JSONDecodeError:
            return response.content.decode()

    @property
    def user_agent(self):
        from . import DOMAIN, VERSION

        return f"home-automation-lab-{DOMAIN} / {VERSION}"
