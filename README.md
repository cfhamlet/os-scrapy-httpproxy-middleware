# os-scrapy-httpproxy-middleware

[![Build Status](https://www.travis-ci.org/cfhamlet/os-scrapy-httpproxy-middleware.svg?branch=master)](https://www.travis-ci.org/cfhamlet/os-scrapy-httpproxy-middleware)
[![codecov](https://codecov.io/gh/cfhamlet/os-scrapy-httpproxy-middleware/branch/master/graph/badge.svg)](https://codecov.io/gh/cfhamlet/os-scrapy-httpproxy-middleware)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/os-scrapy-httpproxy-middleware.svg)](https://pypi.python.org/pypi/os-scrapy-httpproxy-middleware)
[![PyPI](https://img.shields.io/pypi/v/os-scrapy-httpproxy-middleware.svg)](https://pypi.python.org/pypi/os-scrapy-httpproxy-middleware)

This project provide middleware to enhance Scrapy built-in [HttpProxyMiddleware](https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#module-scrapy.downloadermiddlewares.httpproxy). You can set proxy without sheme as the following format:

```
[user:password@]proxy:port
```

## Install

```
pip install os-scrapy-httpproxy-middleware
```

You can run example spider directly in the project root path

```
scrapy crawl example
```

## Usage

### Settings

* enable middleware, it is better disable Scrapy built-in HttpProxyMiddleware

    ```
    DOWNLOADER_MIDDLEWARES = {
        "scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware": None,
        "os_scrapy_httpproxy_middleware.middlewares.HttpProxyMiddleware": 750,
    }
    ```


## Unit Tests

```
sh scripts/test.sh
```

## License

MIT licensed.
