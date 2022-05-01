from dude_pyto import select


@select(css="a.url")
async def result_url(element):
    return {"url": element.get_attribute("href")}


@select(css=".title")
async def result_title(element):
    return {"title": element.text}


@select(css=".description")
async def result_description(element):
    return {"description": element.text}


if __name__ == "__main__":
    from pathlib import Path

    import dude_pyto

    html = f"file://{(Path(__file__).resolve().parent / 'dude_pyto.html').absolute()}"
    dude_pyto.run(urls=[html], parser="selenium")
