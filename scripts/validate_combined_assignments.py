"""
validate_combined_assignments.py

BIFS 614 Expert System - Course Content Validation

Validates the generated combined assignment corpus against the
6 manually cleaned source assignment files.

The script verifies:
    1. All 6 expected cleaned assignment files exist.
    2. The combined assignment corpus exists.
    3. Each assignment has exactly one START marker.
    4. Each assignment has exactly one END marker.
    5. Assignments appear in the correct numerical order.
    6. The content between each pair of markers exactly matches
       its corresponding cleaned source assignment.

No source or combined files are modified.
"""

from pathlib import Path
import sys


# --------------------------------------------------
# CONFIGURATION
# --------------------------------------------------

EXPECTED_ASSIGNMENTS = 6

# Directory containing this script
SCRIPT_DIR = Path(__file__).resolve().parent

# Project root (parent of the scripts directory)
REPO_ROOT = SCRIPT_DIR.parent

# Directory containing the manually cleaned assignment files
ASSIGNMENT_DIR = (
    REPO_ROOT
    / "course_content"
    / "cleaned_txt"
    / "assignments"
)

# Combined assignment corpus
COMBINED_FILE = (
    REPO_ROOT
    / "course_content"
    / "combined"
    / "BIFS614_combined_assignments.txt"
)


# --------------------------------------------------
# VALIDATION FUNCTION
# --------------------------------------------------

def validate_combined_assignments() -> bool:
    """
    Validate the combined assignment corpus against the cleaned
    source assignment files.

    Returns:
        True if all validation checks pass.
        False if any validation check fails.
    """

    print("=" * 60)
    print("BIFS 614 ASSIGNMENT CORPUS VALIDATOR")
    print("=" * 60)

    # Verify that the assignment directory exists.
    if not ASSIGNMENT_DIR.exists():
        print("\nERROR: Assignment directory was not found:")
        print(ASSIGNMENT_DIR)
        return False

    # Build the exact expected assignment filenames.
    expected_files = [
        ASSIGNMENT_DIR
        / f"BIFS614_Assignment_{assignment:02d}_Questions.txt"
        for assignment in range(1, EXPECTED_ASSIGNMENTS + 1)
    ]

    print(f"\nExpected assignment files: {EXPECTED_ASSIGNMENTS}")

    # Check for missing assignment files.
    missing_files = [
        file.name
        for file in expected_files
        if not file.exists()
    ]

    if missing_files:
        print("\nERROR: One or more expected assignment files are missing:")

        for file_name in missing_files:
            print(f"  - {file_name}")

        return False

    print("All expected source assignment files were found.")

    # Verify that the combined corpus exists.
    if not COMBINED_FILE.exists():
        print("\nERROR: Combined assignment corpus was not found:")
        print(COMBINED_FILE)
        print(
            "\nRun combine_assignments.py before running "
            "this validation script."
        )
        return False

    # Read the combined corpus.
    try:
        combined_text = COMBINED_FILE.read_text(
            encoding="utf-8"
        )

    except (OSError, UnicodeError) as error:
        print("\nERROR: Could not read the combined assignment corpus.")
        print(f"Details: {error}")
        return False

    # Verify that the combined corpus is not empty.
    if not combined_text.strip():
        print("\nERROR: Combined assignment corpus is empty.")
        return False

    print("\nCombined assignment corpus found.")
    print("\nValidating assignment content...\n")

    all_valid = True
    previous_end_position = -1

    # --------------------------------------------------
    # VALIDATE EACH ASSIGNMENT
    # --------------------------------------------------

    for assignment, assignment_file in enumerate(
        expected_files,
        start=1
    ):

        assignment_label = f"Assignment {assignment:02d}"

        start_marker = (
            f"<<< START OF BIFS 614 ASSIGNMENT "
            f"{assignment:02d} >>>"
        )

        end_marker = (
            f"<<< END OF BIFS 614 ASSIGNMENT "
            f"{assignment:02d} >>>"
        )

        # Count START and END markers.
        start_count = combined_text.count(start_marker)
        end_count = combined_text.count(end_marker)

        # Verify exactly one START marker.
        if start_count != 1:
            print(
                f"FAIL - {assignment_label}: "
                f"expected 1 START marker, "
                f"found {start_count}"
            )
            all_valid = False
            continue

        # Verify exactly one END marker.
        if end_count != 1:
            print(
                f"FAIL - {assignment_label}: "
                f"expected 1 END marker, "
                f"found {end_count}"
            )
            all_valid = False
            continue

        # Locate START marker.
        start_position = combined_text.find(start_marker)

        # Locate END marker after the START marker.
        end_position = combined_text.find(
            end_marker,
            start_position + len(start_marker)
        )

        # Verify that the END marker occurs after START.
        if end_position == -1:
            print(
                f"FAIL - {assignment_label}: "
                f"END marker could not be located after START marker"
            )
            all_valid = False
            continue

        # Verify assignments appear in numerical order.
        if start_position <= previous_end_position:
            print(
                f"FAIL - {assignment_label}: "
                f"assignment is out of numerical order"
            )
            all_valid = False
            continue

        # Extract the content between START and END markers.
        section_start = start_position + len(start_marker)

        combined_section = combined_text[
            section_start:end_position
        ].strip()

        # Read the corresponding cleaned source assignment.
        try:
            source_text = assignment_file.read_text(
                encoding="utf-8"
            ).strip()

        except (OSError, UnicodeError) as error:
            print(
                f"FAIL - {assignment_label}: "
                f"could not read source file ({error})"
            )
            all_valid = False
            continue

        # Verify that the source assignment is not empty.
        if not source_text:
            print(
                f"FAIL - {assignment_label}: "
                f"source assignment file is empty"
            )
            all_valid = False
            continue

        # Compare the combined section with the cleaned source.
        if combined_section == source_text:
            print(
                f"PASS - {assignment_label}: "
                f"content matches source"
            )
        else:
            print(
                f"FAIL - {assignment_label}: "
                f"content does not match source"
            )
            all_valid = False

        # Save this END position for chronological-order validation.
        previous_end_position = end_position

    # --------------------------------------------------
    # FINAL RESULT
    # --------------------------------------------------

    print("\n" + "=" * 60)

    if all_valid:
        print("VALIDATION PASSED")
        print("=" * 60)

        print(
            f"\nAll {EXPECTED_ASSIGNMENTS} cleaned assignments were "
            f"successfully verified."
        )

        print(
            "The combined assignment corpus exactly matches the "
            "cleaned source files."
        )

        print("\nValidated corpus:")
        print(COMBINED_FILE)

        return True

    print("VALIDATION FAILED")
    print("=" * 60)

    print(
        "\nOne or more validation checks failed. "
        "Review the FAIL messages above."
    )

    return False


# --------------------------------------------------
# SCRIPT ENTRY POINT
# --------------------------------------------------

if __name__ == "__main__":
    success = validate_combined_assignments()

    if success:
        sys.exit(0)

    sys.exit(1)
