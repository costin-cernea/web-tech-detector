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
    run_pipeline("data/domains.csv", "results.json")