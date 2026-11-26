from dataclasses import asdict
import json


def convert_results_to_dict(results):
    dict_results = []
    for result in results:
        dict_result = asdict(result)
        dict_results.append(dict_result)

    return dict_results


def save_results_to_json(results, filename):
    dict_results = convert_results_to_dict(results)

    with open(filename, "w") as file:
        json.dump(dict_results, file, indent=2)


def print_summary(results):
    total_domains = len(results)
    successful_domains = sum(1 for result in results if result.status == "success")
    failed_domains = sum(1 for result in results if result.status == "failed")
    technologies = set()
    total_detections = 0

    for result in results:
        for tech in result.technologies:
            technologies.add(tech.name)
            total_detections += 1

    print("\n========== SCAN SUMMARY ==========")
    print(f"Domains processed:       {total_domains}")
    print(f"Successful scans:        {successful_domains}")
    print(f"Failed scans:            {failed_domains}")
    print(f"Unique technologies:     {len(technologies)}")
    print(f"Total detections:        {total_detections}")
    print("================================\n")


