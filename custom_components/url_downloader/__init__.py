from homeassistant.core import SupportsResponse

DOMAIN = "url_downloader"
VERSION = "0.1.0"


def setup(hass, config):
    from .handler import HandleRequest
    from .schemas import GET_SCHEMA, POST_SCHEMA, PUT_SCHEMA

    hass.services.register(
        DOMAIN,
        "get_request",
        HandleRequest.factory("get"),
        schema=GET_SCHEMA,
        supports_response=SupportsResponse.ONLY,
    )

    hass.services.register(
        DOMAIN,
        "post_request",
        HandleRequest.factory("post"),
        schema=POST_SCHEMA,
        supports_response=SupportsResponse.ONLY,
    )

    hass.services.register(
        DOMAIN,
        "put_request",
        HandleRequest.factory("put"),
        schema=PUT_SCHEMA,
        supports_response=SupportsResponse.ONLY,
    )

    return True
