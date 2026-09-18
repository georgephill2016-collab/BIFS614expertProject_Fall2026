"""
validate_combined_lectures.py

BIFS 614 Expert System - Course Content Validation

Validates the generated combined lecture corpus against the
11 manually cleaned source lecture files.

The script verifies:
    1. The expected 11 source lecture files exist.
    2. The combined corpus exists.
    3. Each lecture has exactly one START marker.
    4. Each lecture has exactly one END marker.
    5. Each lecture appears in the correct order.
    6. The text contained between each pair of markers exactly
       matches its corresponding cleaned source lecture.

No source or combined files are modified.
"""

from pathlib import Path
import sys


# --------------------------------------------------
# CONFIGURATION
# --------------------------------------------------

EXPECTED_WEEKS = 11

SCRIPT_DIR = Path(__file__).resolve().parent

REPO_ROOT = SCRIPT_DIR.parent

LECTURE_DIR = (
    REPO_ROOT
    / "course_content"
    / "cleaned_txt"
    / "lectures"
)

COMBINED_FILE = (
    REPO_ROOT
    / "course_content"
    / "combined"
    / "BIFS614_combined_lectures.txt"
)


# --------------------------------------------------
# VALIDATION FUNCTION
# --------------------------------------------------

def validate_combined_lectures() -> bool:
    """
    Validate the combined lecture corpus against the cleaned
    source lecture files.

    Returns:
        True if all validation checks pass.
        False if any validation check fails.
    """

    print("=" * 60)
    print("BIFS 614 LECTURE CORPUS VALIDATOR")
    print("=" * 60)

    # Verify source lecture directory.
    if not LECTURE_DIR.exists():
        print("\nERROR: Lecture directory was not found:")
        print(LECTURE_DIR)
        return False

    # Build the exact expected file list.
    expected_files = [
        LECTURE_DIR / f"week_{week:02d}_lecture.txt"
        for week in range(1, EXPECTED_WEEKS + 1)
    ]

    missing_files = [
        file.name
        for file in expected_files
        if not file.exists()
    ]

    if missing_files:
        print("\nERROR: Expected lecture files are missing:")

        for file_name in missing_files:
            print(f"  - {file_name}")

        return False

    # Detect unexpected additional lecture files.
    discovered_files = sorted(
        LECTURE_DIR.glob("week_*_lecture.txt")
    )

    if len(discovered_files) != EXPECTED_WEEKS:
        print(
            f"\nERROR: Expected exactly {EXPECTED_WEEKS} "
            f"lecture files, but found "
            f"{len(discovered_files)}."
        )
        return False

    print(
        f"\nSource lecture files found: "
        f"{len(discovered_files)}"
    )

    # Verify combined corpus exists.
    if not COMBINED_FILE.exists():
        print("\nERROR: Combined lecture corpus was not found:")
        print(COMBINED_FILE)
        print(
            "\nRun combine_lectures.py before running "
            "this validation script."
        )
        return False

    # Read combined corpus.
    try:
        combined_text = COMBINED_FILE.read_text(
            encoding="utf-8"
        )

    except (OSError, UnicodeError) as error:
        print("\nERROR: Could not read the combined corpus.")
        print(f"Details: {error}")
        return False

    if not combined_text.strip():
        print("\nERROR: Combined lecture corpus is empty.")
        return False

    print("\nValidating lecture content...\n")

    all_valid = True
    previous_end_position = -1

    # --------------------------------------------------
    # VALIDATE EACH LECTURE
    # --------------------------------------------------

    for week, lecture_file in enumerate(
        expected_files,
        start=1
    ):

        week_label = f"Week {week:02d}"

        start_marker = (
            f"<<< START OF BIFS 614 WEEK "
            f"{week:02d} LECTURE >>>"
        )

        end_marker = (
            f"<<< END OF BIFS 614 WEEK "
            f"{week:02d} LECTURE >>>"
        )

        # Verify marker counts.
        start_count = combined_text.count(start_marker)
        end_count = combined_text.count(end_marker)

        if start_count != 1:
            print(
                f"FAIL - {week_label}: "
                f"expected 1 START marker, "
                f"found {start_count}"
            )
            all_valid = False
            continue

        if end_count != 1:
            print(
                f"FAIL - {week_label}: "
                f"expected 1 END marker, "
                f"found {end_count}"
            )
            all_valid = False
            continue

        # Locate marker positions.
        start_position = combined_text.find(start_marker)
        end_position = combined_text.find(
            end_marker,
            start_position + len(start_marker)
        )

        if end_position == -1:
            print(
                f"FAIL - {week_label}: "
                f"END marker occurs before START marker "
                f"or could not be located correctly"
            )
            all_valid = False
            continue

        # Verify chronological order.
        if start_position <= previous_end_position:
            print(
                f"FAIL - {week_label}: "
                f"lecture is out of chronological order"
            )
            all_valid = False
            continue

        # Extract lecture text between its markers.
        section_start = start_position + len(start_marker)

        combined_section = combined_text[
            section_start:end_position
        ].strip()

        # Read corresponding cleaned source lecture.
        try:
            source_text = lecture_file.read_text(
                encoding="utf-8"
            ).strip()

        except (OSError, UnicodeError) as error:
            print(
                f"FAIL - {week_label}: "
                f"could not read source file ({error})"
            )
            all_valid = False
            continue

        # Compare exact content.
        if combined_section == source_text:
            print(
                f"PASS - {week_label}: "
                f"content matches source"
            )
        else:
            print(
                f"FAIL - {week_label}: "
                f"content does not match source"
            )
            all_valid = False

        previous_end_position = end_position

    # --------------------------------------------------
    # FINAL RESULT
    # --------------------------------------------------

    print("\n" + "=" * 60)

    if all_valid:
        print("VALIDATION PASSED")
        print("=" * 60)
        print(
            f"\nAll {EXPECTED_WEEKS} cleaned lectures were "
            f"successfully verified."
        )
        print(
            "The combined lecture corpus matches the "
            "cleaned source files."
        )

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
    success = validate_combined_lectures()

    if success:
        sys.exit(0)

    sys.exit(1)
