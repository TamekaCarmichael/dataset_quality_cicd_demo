from __future__ import annotations

from pathlib import Path
# this is a test 
from src.dataset_validator import (
    DATASET_PATH,
    EXPECTED_COLUMNS,
    EXPECTED_ROWS,
    build_validation_report,
    load_cleaned_dataset,
    validate_cleaned_dataset,
)


EXPECTED_DATASET = Path("data/processed/cleaned_customers.csv")


def test_approved_cleaned_dataset_path_is_used() -> None:
    assert DATASET_PATH == EXPECTED_DATASET


def test_cleaned_dataset_has_expected_shape() -> None:
    df = load_cleaned_dataset()
    report = build_validation_report(df)
    assert report.rows == EXPECTED_ROWS
    assert report.columns == EXPECTED_COLUMNS


def test_cleaned_dataset_has_no_missing_values() -> None:
    df = load_cleaned_dataset()
    report = build_validation_report(df)
    assert report.missing_values == 0


def test_cleaned_dataset_has_no_duplicate_rows() -> None:
    df = load_cleaned_dataset()
    report = build_validation_report(df)
    assert report.duplicate_rows == 0


def test_full_cleaned_dataset_validation() -> None:
    df = load_cleaned_dataset()
    report = validate_cleaned_dataset(df)
    assert report.rows == EXPECTED_ROWS
