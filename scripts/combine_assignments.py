"""
combine_assignments.py

BIFS 614 Expert System - Course Content Processing

Combines the 6 individually cleaned BIFS 614 assignment text files
into a single assignment corpus for use by the expert system.

The original cleaned assignment files are read only and are not modified.

Expected input:
    course_content/assignments/
        BIFS614_Assignment_01_Questions.txt
        ...
        BIFS614_Assignment_06_Questions.txt

Output:
    course_content/combined/BIFS614_combined_assignments.txt
"""

from pathlib import Path
import sys


# --------------------------------------------------
# CONFIGURATION
# --------------------------------------------------

EXPECTED_ASSIGNMENTS = 6

# Directory containing this script
SCRIPT_DIR = Path(__file__).resolve().parent

# Repository root (parent of the scripts directory)
REPO_ROOT = SCRIPT_DIR.parent

# Source directory containing manually cleaned assignments
ASSIGNMENT_DIR = (
    REPO_ROOT
    / "course_content"
    / "cleaned_txt"
    / "assignments"
)

# Directory for generated combined course content
OUTPUT_DIR = (
    REPO_ROOT
    / "course_content"
    / "combined"
)

# Final combined assignment corpus
OUTPUT_FILE = OUTPUT_DIR / "BIFS614_combined_assignments.txt"


# --------------------------------------------------
# COMBINATION FUNCTION
# --------------------------------------------------

def combine_assignments() -> bool:
    """
    Combine all cleaned BIFS 614 assignment files into one corpus.

    Returns:
        True if the combination succeeds.
        False if an error occurs.
    """

    print("=" * 60)
    print("BIFS 614 ASSIGNMENT CORPUS BUILDER")
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

    # Verify that all expected assignment files exist.
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

    # Create the output directory if necessary.
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("\nCombining assignments...\n")

    try:
        with OUTPUT_FILE.open(
            "w",
            encoding="utf-8",
            newline="\n"
        ) as outfile:

            for assignment, assignment_file in enumerate(
                expected_files,
                start=1
            ):

                print(
                    f"Adding Assignment {assignment:02d}: "
                    f"{assignment_file.name}"
                )

                # Read the cleaned assignment.
                assignment_text = assignment_file.read_text(
                    encoding="utf-8"
                ).strip()

                # Verify that the assignment is not empty.
                if not assignment_text:
                    print(
                        f"\nERROR: {assignment_file.name} is empty."
                    )
                    return False

                # Add explicit assignment boundaries.
                start_marker = (
                    f"<<< START OF BIFS 614 ASSIGNMENT "
                    f"{assignment:02d} >>>"
                )

                end_marker = (
                    f"<<< END OF BIFS 614 ASSIGNMENT "
                    f"{assignment:02d} >>>"
                )

                outfile.write(start_marker)
                outfile.write("\n\n")

                outfile.write(assignment_text)

                outfile.write("\n\n")
                outfile.write(end_marker)
                outfile.write("\n\n")

    except (OSError, UnicodeError) as error:
        print("\nERROR: The assignment corpus could not be created.")
        print(f"Details: {error}")
        return False

    # Report output information.
    output_size = OUTPUT_FILE.stat().st_size

    print("\n" + "=" * 60)
    print("COMBINATION SUCCESSFUL")
    print("=" * 60)

    print(f"\nAssignments combined: {EXPECTED_ASSIGNMENTS}")
    print(f"Output size: {output_size:,} bytes")
    print("\nCombined corpus created at:")
    print(OUTPUT_FILE)

    return True


# --------------------------------------------------
# SCRIPT ENTRY POINT
# --------------------------------------------------

if __name__ == "__main__":
    success = combine_assignments()

    if success:
        sys.exit(0)

    sys.exit(1)
