# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy.downloadermiddlewares.httpproxy import (
    HttpProxyMiddleware as ProxyMiddleware,
)


class HttpProxyMiddleware(ProxyMiddleware):
    def process_request(self, request, spider):
        super(HttpProxyMiddleware, self).process_request(request, spider)
        if "proxy" not in request.meta:
            return
        proxy = request.meta["proxy"]
        if proxy.startswith("//"):
            request.meta["proxy"] = ":".join(("http", proxy))

    @classmethod
    def from_crawler(cls, crawler):
        if not crawler.settings.getbool("HTTPPROXY_ENABLED"):
            raise NotConfigured
        auth_encoding = crawler.settings.get("HTTPPROXY_AUTH_ENCODING")
        return cls(auth_encoding)
