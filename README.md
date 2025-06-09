# URL Downloader

Home Assistant integration that provides [actions](#available-actions) for downloading URLs and getting the response into automation and script variables.

```yaml
    - action: url_downloader.get_request
      metadata: {}
      data:
        url: https://httpbin.org/get
      response_variable: my_response_variable
```

## Installation

### HACS

This integration can be installed using [HACS](https://www.hacs.xyz), a frontend interface for a community-driven directory for Home Assistant. Before clicking the link below, make sure [HACS is installed](https://www.hacs.xyz/docs/use/).

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=HomeAutomationLab&repository=integration-url-downloader)

### Manual

1. Clone this repository.
1. Copy `custom_components/url_downloader` into your `custom_components` directory
1. Add `url_downloader:` into your `configuration.yml` file
1. Restart Home Assistant

## Available Actions

### `get_request`

Performs a GET request

#### Fields

* `url` (required): request URL
* `headers` (optional): JSON-formatted dictionary of additional headers to send with request
* `payload` (optional): JSON-formatted dictionary of the payload to send with the request
* `params` (optional): JSON-formatted dictionary of query params

### `post_request`

Performs a POST request

#### Fields

* `url` (required): request URL
* `headers` (optional): JSON-formatted dictionary of additional headers to send with request
* `payload` (optional): JSON-formatted dictionary of the payload to send with the request
* `params` (optional): JSON-formatted dictionary of query params
* `content_type` (optional): Content type header

### `put_request`

Performs a PUT request

#### Fields

* `url` (required): request URL
* `headers` (optional): JSON-formatted dictionary of additional headers to send with request
* `payload` (optional): JSON-formatted dictionary of the payload to send with the request
* `params` (optional): JSON-formatted dictionary of query params
* `content_type` (optional): Content type header
