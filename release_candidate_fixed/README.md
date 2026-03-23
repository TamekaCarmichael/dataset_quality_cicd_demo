# release_candidate_fixed

This candidate validates a cleaned dataset in CI.

Checks:
- no duplicate rows
- no missing values
- expected row count = 5
- expected column count = 4
- approved cleaned dataset path is used

Run locally:

```bash
python -m pip install -r requirements.txt
python -m pip install -r requirements-dev.txt
PYTHONPATH=. pytest
python src/dataset_validator.py
```
