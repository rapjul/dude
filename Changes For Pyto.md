# Changes For Pyto


## Change 1: Rename functions

Find: `dude(\n)`
Replace: `dude_pyto$1`

Files to Exclude: `README.*, **/*.md, **/*.yml`


## Change 2: Dependencies

### Make BraveBlock an optional dependency

#### In "base.py"

Remove Line 29

```py
try:
    from braveblock import Adblocker
except ImportError:
    pass
```

Add After Line 74

```py
        try:
            self.adblock = Adblocker()
        except NameError:
            self.adblock = None
```

#### In "./optional/utils.py"

After Line 44

```py
        except AttributeError:
            logger.info("URL %s has been blocked.", url)
            raise httpx.RequestError(message=f"URL {url} has been blocked.", request=request)
```

### Make Playwright an optional dependency

```py
try:
    import playwright
except ImportError:
    pass
```




## Change Lines

Comment out Line 5 in "./dude_pyto/scraper.py"

```py
from .playwright_scraper import PlaywrightScraper
```

Add the above line to Line 73 in "./dude_pyto/scraper.py"
