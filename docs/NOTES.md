I created src/models.py and i tested everything to see if the import works with command [python3 -c "import src.models; print('Models loaded OK')"].

---------------------

Now, before jumping to the creation of required functions from DESIGN to make the app's workflow -> Stage 2, i need to install some tools: pyarrow to read the Parquet file provided and httpx to make http requests. -> I PUT THEM IN requirements.txt

-------------

I created a small program dataset_test.py to see the columns, number of rows and the first 5 rows for a quick view.

--------------

Now, i created fetcher.py and i will use urllib for urlparse (that will help me to break the link in pieces and to reasable with the correct format) and httpx to make a request and see if that link uses http or https.

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

------------------

Initial domain fetching pipeline complete. I also tested with a tiny code to see if objects are created (i also like that "final_url" generates the exact link after redirects, so the fial link can be a complete different link from the provided domain). The entire process (because of those 200 domain) take a while and the terminal is frozen for about ~ 3,3 minutes, so its a good idea to add a process loading message later.

------------------------


I created extractor.py with extract_signals function. I've been modifying the code several times and src.models.py -> PageSignals -> meta_tags attribute as well. The reason: i needed to create a dictionary with key[str] and value[list str] to extract more information. Metatags i see contain different key names ("name", "property") and i wanted to store all meta_tags, so i've created a content list to not overwrite useful information with just a simple dictionary. 

I tested the function with a code created in tests.test_extractor.py. The results are good. 

Also, i wanted to create tests.test_fetcher.py as well because the first time i tested those function in terminal only.

--------------------------

I've created detector.py and tech_rules.py . Here, i've created a very small tech_rule and the unfinished logic for detect_tech() just to see how works this prototype. It seems to give me the expected output.