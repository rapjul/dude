from dude_pyto import select


@select(css=".title", group=".custom-group")
def result_title(element):
    return {"title": element.text_content()}


@select(css=".description", group=".custom-group")
def result_description(element):
    return {"description": element.text_content()}


if __name__ == "__main__":
    from pathlib import Path

    import dude_pyto

    html = f"file://{(Path(__file__).resolve().parent / 'example.html').absolute()}"
    dude_pyto.run(urls=[html])
