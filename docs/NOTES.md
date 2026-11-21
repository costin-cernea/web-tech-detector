I created src/models.py and i tested everything to see if the import works with command [python3 -c "import src.models; print('Models loaded OK')"].

---------------------

Now, before jumping to the creation of required functions from DESIGN to make the app's workflow -> Stage 2, i need to install some tools: pyarrow to read the Parquet file provided and httpx to make http requests. -> I PUT THEM IN requirements.txt

-------------

I created a small program dataset_test.py to see the columns, number of rows and the first 5 rows for a quick view.

--------------

Now, i created fetcher.py and i will use urllib for urlparse and urlunparse (that will help me to break the link in pieces and to reasable with the correct format) and httpx to make a request and see if that link uses http or https.

My first solution was this:

```
def normalize_domain(domain: str) -> str | None:
    domain = domain.strip().lower()
    if "://" not in domain:
        parsed = urlparse(f"//{domain}")
    else:
        parsed = urlparse(domain)
    # Now i need to verify if the domain uses https or http accesing the http request. First, verifying if its https and then http
    try:
        response = httpx.get(f"https://{parsed.hostname}", timeout=5, follow_redirects=True)
        return str(response.url)
    except httpx.RequestError:
        try:
            response = httpx.get(f"http://{parsed.hostname}", timeout=5, follow_redirects=True)
            return str(response.url)
        except httpx.RequestError:
            return None
```

Here, i wanted to split the task into more functions, but i saw that its more convenient to normalize and extract the html data in one functions. If I wanted to make the same thing in two function, i needed to make the get request 2 times (one for creating the correct url format, the second time to extract again the same html code, so i wanted to make the whole operation in one place because many aspects (not only the actual html code but also the normalization) was supposed to be redundant ). 

So, i decided to use that function to return the object of the current domain. Now, im thinking to write a function that gets the path of the dataset file, creates a list with all domains and then, i use the modified function "normalize_domain" that i changed the name with  fetch_domain_response to extract the information for each domain from that list.

--------------

I created fetch_domain_response() and process_domains functions


HTTPX response attributes:

.url -> final url after redirects
.status_code -> http status code
.headers -> response headers
.cookies -> cookies received
.text -> html content