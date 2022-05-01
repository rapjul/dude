from dude_pyto import select


@select(css="a.url")
def result_url(element):
    return {"url": element.get_attribute("href")}


@select(css=".title")
def result_title(element):
    return {"title": element.text_content()}


@select(css=".description")
def result_description(element):
    return {"description": element.text_content()}


if __name__ == "__main__":
    from pathlib import Path

    import dude_pyto

    html = f"file://{(Path(__file__).resolve().parent / 'dude_pyto.html').absolute()}"
    dude_pyto.run(urls=[html])
