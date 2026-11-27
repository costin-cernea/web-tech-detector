from src.fetcher import process_domains
from src.extractor import extract_signals
from src.detector import detect_tech
from src.reporter import save_results_to_json, print_summary

def run_pipeline(dataset_path: str, output_filename: str):
    raw_responses = process_domains(dataset_path)
    processed_responses = extract_signals(raw_responses)
    domain_results = detect_tech(processed_responses)
    save_results_to_json(domain_results, output_filename)
    print_summary(domain_results)

if __name__ == "__main__":
    print("Starting website technology detection...")
    print("Please wait while websites are being processed.\n")

    run_pipeline("data/part-00000-66e0628d-2c7f-425a-8f5b-738bcd6bf198-c000.snappy.parquet", "results.json")

    print("\nProcessing completed!")