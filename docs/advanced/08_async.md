# Asynchronous Support

Handler functions can be converted to async.
It is not possible to mix async and sync handlers since Playwright does not support this.
It is however, possible to have async and sync storage handlers at the same time since this is not connected to Playwright anymore.

=== "Python"

    ```python
    from dude_pyto import save, select


    @select(css=".title")
    async def result_title(element):
        return {"title": await element.text_content()}


    @save("json")
    async def save_json(data, output) -> bool:
        ...
        return True


    @save("xml")
    def save_xml(data, output) -> bool: # (1)
        ...
        return True
    ```

    1. Sync storage handler can be used on sync and async mode

## Examples

A more extensive example can be found at [examples/async.py](https://github.com/roniemartinez/dude/tree/master/examples/async.py).
