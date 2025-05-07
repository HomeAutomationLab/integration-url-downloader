import voluptuous as vol

REQUEST_SCHEMA = vol.Schema(
    {
        vol.Required("url"): str,
        vol.Optional("headers"): dict,
        vol.Optional("payload"): dict,
        vol.Optional("params"): dict,
    }
)

GET_SCHEMA = REQUEST_SCHEMA

POST_SCHEMA = REQUEST_SCHEMA.extend(
    {
        vol.Optional("content_type"): str,
    }
)

PUT_SCHEMA = POST_SCHEMA
