from dude_pyto import Request, select, start_requests

"""
This example demonstrates how to use custom HTTPX Request object
"""


@start_requests()
def custom_requests():
    for url in ["https://dude_pyto.ron.sh"]:
        yield Request(method="GET", url=url)


@select(css="a.url", priority=2)
def result_url(soup):
    return {"url": soup["href"]}


if __name__ == "__main__":
    import dude_pyto

    dude_pyto.run(urls=[], parser="bs4")
