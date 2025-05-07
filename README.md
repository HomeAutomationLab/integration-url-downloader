# URL Downloader

Home Assistant action for downloading URLs

## Services

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
