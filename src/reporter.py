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

