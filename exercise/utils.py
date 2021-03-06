import os
import json
from dataclasses import asdict
from exercise.errors import ErrorEmptyResult

RESULTS_FILE = 'results.jsonl'

# Clean the results file
open(RESULTS_FILE, 'w').close()

def handle_result(job):
    # Check if there are results
    if job.result is None:
        raise ErrorEmptyResult('This job has no results')

    # Make sure the results directory exists
    os.makedirs('results', exist_ok=True)

    with open(RESULTS_FILE, 'a+') as file:
        file.write(json.dumps(asdict(job)))
        file.write('\n')
