# Website Technologies Scraper

## Project Overview

This project detects technologies used by websites based on publicly available information. The goal is to identify technologies that websites use, such as ecommerce platforms, CMSs, analytics tools, payment providers, marketing tools, and other services.

The project processes a dataset containing 200 domains, fetches their web responses, extracts relevant signals, and uses a set of fingerprinting rules to identify technologies.

For each detected technology, the program also stores evidence showing why that technology was identified. The final results are saved in JSON format.

---

## My Approach

I decided to build the solution as a modular Python application with separate stages for fetching websites, extracting signals, detecting technologies, and generating the final results.

One of the main design decisions I made was to avoid making unnecessary HTTP requests. Initially, I considered having separate functions for URL normalization and response extraction, but I realized that I could handle both operations together and reuse the same HTTP response. This also allowed me to retrieve the final URL after redirects, together with the headers, cookies, status code, and HTML content from the same request.

Another important decision was how to handle failed requests. I wanted the final output to contain information about every domain from the input dataset, including websites that could not be accessed. Because of this, I changed the processing model to preserve failed responses and generate results with their corresponding status and error information instead of simply skipping them.

For technology detection, I chose a rule-based approach because it was straightforward to implement, understand, and extend. The rules search for fingerprints in different sources, such as headers, cookies, script URLs, meta tags, and HTML. Whenever a rule matches, I store the evidence that triggered the detection, so the result does not contain only the technology name but also an explanation of why it was identified.

As the number of rules increased, I also decided to organize them into separate category files and combine them through a central aggregator. This avoids having one large file containing all the fingerprints and makes it easier to add or modify technologies without changing the detection engine.

The implementation was developed incrementally. I tested individual components while building them and then tested the complete pipeline using the provided dataset.

---

## Architecture

The application is divided into four main stages:

```text
Input Dataset
     |
     v
   Fetcher
     |
     v
  Extractor
     |
     v
  Detector
     |
     v
  Reporter
     |
     v
  JSON Results
```

### 1. Fetcher

The fetching stage reads the provided dataset and processes the domains individually.

It attempts to retrieve the website response and collects the information needed by the following stages, including:

- Final URL after redirects
- HTTP status code
- Response headers
- Cookies
- HTML content

The fetching logic is implemented in `fetcher.py`.

### 2. Extractor

The extractor processes the fetched responses and extracts signals that can be used for technology detection.

These signals include:

- HTTP headers
- Cookies
- Script source URLs
- Meta tags
- HTML content

The extraction logic is implemented in `extractor.py`.

### 3. Detector

The detector iterates through the technology fingerprinting rules and compares them against the extracted signals.

When a rule matches, the corresponding technology is added to the result together with its category and detection evidence.

The detection logic is implemented in `detector.py`, while the fingerprinting rules are organized inside the `src/rules/` directory.

### 4. Reporter

The reporting stage converts the results into a structured format and saves them as JSON.

It also prints a summary to the terminal containing the number of processed domains, successful and failed requests, unique technologies detected, and total detections.

The reporting logic is implemented in `reporter.py`.

---

## Technology Detection

Technology detection is based on fingerprinting rules.

Each technology contains one or more rules that describe patterns expected to be found in a particular source of information.

For example, a technology might be identified through:

- A specific HTTP header
- A cookie name
- A script URL
- A meta tag
- A pattern found in the HTML

Rules use regular expressions to match these fingerprints against the extracted signals.

The rules are organized into categories to make them easier to maintain:

- Ecommerce
- CMS
- Analytics
- Payment
- Marketing
- Customer Support
- Performance
- SEO

All category rules are combined through a central aggregator in `src/rules/tech_rules.py`.

When a technology is detected, the result contains the technology name, its categories, and proof of the match. The proof includes information about the source where the match occurred and the pattern that triggered the detection.

This makes the results easier to review and helps identify why a technology was detected.

---

## Development Process

I started by creating `src/models.py`, where I defined the main data structures used throughout the application. I tested the imports separately to make sure the module was working before moving on to the next stage.

Before implementing the main workflow, I installed the required dependencies, including `pyarrow` for reading the provided Parquet dataset and `httpx` for making HTTP requests. I added them to `requirements.txt` so they could be installed together.

I also created a small script to inspect the dataset, check its columns and number of rows, and display the first few records. This helped me understand the input data before implementing the fetching logic.

For the fetching stage, I initially considered separating URL normalization and HTTP requests into different functions. However, I realized that this would require making multiple requests to the same domain in order to normalize the URL and then retrieve the response. Since I needed the final URL after redirects, the response headers, cookies, status code, and HTML content, I decided to handle the whole operation in one function, `fetch_domain_response()`, which returns the HTTP response containing all the information needed by the following stages.

I then created `process_domains()`, which reads the dataset, extracts the domains, and processes them individually.

After completing the initial fetching pipeline, I created `extractor.py` with the `extract_signals()` function. This stage extracts the information needed for technology detection, including headers, cookies, script sources, meta tags, and HTML. While working on meta tags, I changed the data structure to store multiple values for the same key, since different tags can use the same attribute and I didn't want useful information to be overwritten.

I tested the fetching and extraction functions separately using test files in the `tests/` directory.

Next, I implemented the initial detection logic in `detector.py` and created the first technology fingerprinting rules. I started with a small rule to verify that the detection logic worked as expected before expanding the number of technologies.

During development, I also identified a problem with how failed HTTP responses were handled. Initially, unsuccessful responses were skipped during signal extraction, which could result in domains being lost from the final output. I decided to modify the processing model so that failed domains were also represented in the pipeline, allowing each input domain to have a corresponding result, including its status and error information.

Once the detection logic was working, I implemented the reporting stage. I converted the `DomainResult` objects into dictionaries using `asdict()` and then serialized them into a JSON file. I also added a terminal summary containing the total number of domains, successful and failed requests, the number of unique technologies, and the total number of detections.

As the number of fingerprinting rules increased, I organized them into separate files based on technology categories. I then created a central aggregator that combines all category rules so that the detector can iterate through them without depending on the individual rule files. This made the rules easier to organize, maintain, and extend.

Finally, I ran the complete pipeline against the provided dataset containing 200 domains. I also added a waiting message to the terminal to provide feedback while the domains were being processed, since the initial implementation took several minutes to complete.

---

## Results

After completing the main implementation, I ran the pipeline against the provided dataset containing 200 domains. The process took a few minutes because websites were fetched individually.

The program successfully processed 184 domains, while 16 domains failed during the fetching stage. The initial run identified 67 unique technologies and generated 621 total detections.

The results are saved in a JSON file, where each domain contains its processing status and, when successful, the technologies detected, their categories, and the proof behind each detection.

After reviewing the initial results, I made some improvements to the detection rules to reduce false positives, remove duplicate technologies, and make certain fingerprints more specific. I also added tests to validate the rules and their structure. These improvements were made after the initial full run, so the reported numbers correspond to that run rather than a new run with all the updated rules.

Although the results show that the detector is working, the detections are not guaranteed to be completely accurate. Some technologies may remain undetected, and some fingerprints may still produce false positives. These are limitations of the current rule-based approach.

---

## Limitations

There are several limitations to the current implementation.

### Technologies may not always be visible

Some websites hide information about the technologies they use, remove identifying fingerprints, or load scripts dynamically. In these cases, the detector may not have enough information to identify a technology.

The detector relies on publicly available signals, so it cannot identify every technology used internally by a website.

### False positives

Some fingerprints are not unique to a particular technology. For example, a generic script URL or HTTP header may be used by multiple services.

Because of this, a fingerprint may match even when the technology is not actually being used in the way the rule expects.

### False negatives

A technology may be present on a website but not detected because its fingerprint is missing, changed, hidden, or not included in the extracted signals.

### Rule maintenance

The detection system depends on manually maintained fingerprinting rules. Technologies can change their scripts, headers, cookies, or other identifying signals, meaning that existing rules may become outdated.

### Fetching limitations

Websites may fail to respond, block automated requests, redirect unexpectedly, or require browser execution to expose their content.

The current implementation fetches websites individually and does not execute JavaScript like a full browser, so some signals may not be available.

---

## Scaling to Millions of Domains

The current implementation processes domains individually, which is sufficient for the provided dataset but would become inefficient for millions of domains.

To scale the system, I would change the fetching stage to use asynchronous HTTP requests or multiple workers so that many domains could be processed concurrently instead of waiting for each request to finish before starting the next one.

I would also introduce a queue-based architecture where domains are placed into a queue and distributed among multiple workers. This would allow the system to scale horizontally by adding more workers when needed.

Additional improvements would include:

- Request timeouts and retry mechanisms
- Rate limiting to avoid overloading websites
- Caching responses to avoid unnecessary repeated requests
- Better handling of failed requests
- Separating fetching, extraction, and detection into independently scalable services
- Storing results in a database instead of relying only on JSON files
- Monitoring processing progress and performance

For a larger system, I would also consider using message queues such as RabbitMQ or Kafka to distribute tasks between different components.

---

## Discovering New Technologies

The current detection system relies on fingerprinting rules that are manually maintained. To discover new technologies and keep the database updated, I would introduce a process for continuously reviewing new signals found during crawling.

For example, I could collect script URLs, cookies, headers, and meta tags that do not currently match any known fingerprint and analyze which signals appear frequently across different websites.

I would also use external technology databases, documentation, technology release information, and websites belonging to technology providers to identify new fingerprints.

The process could include:

1. Collecting signals that are not currently recognized.
2. Identifying recurring patterns across websites.
3. Investigating whether those patterns belong to a new technology.
4. Creating candidate fingerprinting rules.
5. Testing the rules against websites where the technology is known to be present and absent.
6. Reviewing and adding validated rules to the fingerprint database.

In the future, this process could be partially automated to suggest new fingerprinting rules, while keeping manual validation to reduce false positives.

---

## Installation

Clone the repository and install the dependencies:

```bash
pip install -r requirements.txt
```

Make sure the provided dataset is placed in the `data/` directory.

---

## Usage

Run the application from the project root:

```bash
python -m src.main
```

The program will process the domains from the dataset, detect technologies, print a summary to the terminal, and generate the JSON results file.

---

## Project Structure

```text
web-tech-detector/
│
├── data/
│   └── dataset.parquet
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── fetcher.py
│   ├── extractor.py
│   ├── detector.py
│   ├── reporter.py
│   ├── models.py
│   │
│   └── rules/
│       ├── __init__.py
│       ├── tech_rules.py
│       ├── ecommerce_rules.py
│       ├── cms_rules.py
│       ├── analytics_rules.py
│       ├── payment_rules.py
│       ├── marketing_rules.py
│       ├── customer_support_rules.py
│       ├── performance_rules.py
│       └── seo_rules.py
│
├── tests/
│   ├── test_fetcher.py
│   ├── test_extractor.py
│   ├── test_detector.py
│   └── test_rules.py
│
├── requirements.txt
├── README.md
└── results.json
```

