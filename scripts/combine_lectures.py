"""
combine_lectures.py

BIFS 614 Expert System - Course Content Processing

Combines the 11 individually cleaned BIFS 614 lecture text files
into a single lecture corpus for use by the expert system.

The original cleaned lecture files are read only and are not modified.

Expected input:
    course_content/cleaned_txt/lectures/
        week_01_lecture.txt
        ...
        week_11_lecture.txt

Output:
    course_content/combined/BIFS614_combined_lectures.txt
"""

from pathlib import Path
import sys


# --------------------------------------------------
# CONFIGURATION
# --------------------------------------------------

EXPECTED_WEEKS = 11

# Directory containing this script
SCRIPT_DIR = Path(__file__).resolve().parent

# Repository root (parent of the scripts directory)
REPO_ROOT = SCRIPT_DIR.parent

# Source directory containing manually cleaned lectures
LECTURE_DIR = (
    REPO_ROOT
    / "course_content"
    / "cleaned_txt"
    / "lectures"
)

# Directory for generated combined course content
OUTPUT_DIR = (
    REPO_ROOT
    / "course_content"
    / "combined"
)

# Final combined lecture corpus
OUTPUT_FILE = OUTPUT_DIR / "BIFS614_combined_lectures.txt"


# --------------------------------------------------
# COMBINATION FUNCTION
# --------------------------------------------------

def combine_lectures() -> bool:
    """
    Combine all cleaned BIFS 614 lecture files into one corpus.

    Returns:
        True if the combination succeeds.
        False if an error occurs.
    """

    print("=" * 60)
    print("BIFS 614 LECTURE CORPUS BUILDER")
    print("=" * 60)

    # Verify that the lecture directory exists.
    if not LECTURE_DIR.exists():
        print("\nERROR: Lecture directory was not found:")
        print(LECTURE_DIR)
        return False

    # Find lecture files.
    #
    # Zero-padded filenames (01, 02, ... 11) allow normal
    # alphabetical sorting to preserve chronological order.
    lecture_files = sorted(
        LECTURE_DIR.glob("week_*_lecture.txt")
    )

    print(f"\nLecture files found: {len(lecture_files)}")

    # Verify that all expected lectures are present.
    if len(lecture_files) != EXPECTED_WEEKS:
        print(
            f"\nERROR: Expected {EXPECTED_WEEKS} lecture files, "
            f"but found {len(lecture_files)}."
        )
        return False

    # Verify that the exact expected filenames exist.
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
        print("\nERROR: One or more expected lecture files are missing:")

        for file_name in missing_files:
            print(f"  - {file_name}")

        return False

    # Create the output directory if it does not already exist.
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("\nCombining lectures...\n")

    try:
        with OUTPUT_FILE.open(
            "w",
            encoding="utf-8",
            newline="\n"
        ) as outfile:

            for week, lecture_file in enumerate(
                expected_files,
                start=1
            ):

                print(
                    f"Adding Week {week:02d}: "
                    f"{lecture_file.name}"
                )

                # Read the cleaned lecture.
                lecture_text = lecture_file.read_text(
                    encoding="utf-8"
                ).strip()

                # Verify that the lecture is not empty.
                if not lecture_text:
                    print(
                        f"\nERROR: {lecture_file.name} is empty."
                    )
                    return False

                # Add explicit source boundaries.
                start_marker = (
                    f"<<< START OF BIFS 614 WEEK "
                    f"{week:02d} LECTURE >>>"
                )

                end_marker = (
                    f"<<< END OF BIFS 614 WEEK "
                    f"{week:02d} LECTURE >>>"
                )

                outfile.write(start_marker)
                outfile.write("\n\n")

                outfile.write(lecture_text)

                outfile.write("\n\n")
                outfile.write(end_marker)
                outfile.write("\n\n")

    except (OSError, UnicodeError) as error:
        print("\nERROR: The lecture corpus could not be created.")
        print(f"Details: {error}")
        return False

    # Report output information.
    output_size = OUTPUT_FILE.stat().st_size

    print("\n" + "=" * 60)
    print("COMBINATION SUCCESSFUL")
    print("=" * 60)

    print(f"\nLectures combined: {EXPECTED_WEEKS}")
    print(f"Output size: {output_size:,} bytes")
    print("\nCombined corpus created at:")
    print(OUTPUT_FILE)

    return True


# --------------------------------------------------
# SCRIPT ENTRY POINT
# --------------------------------------------------

if __name__ == "__main__":
    success = combine_lectures()

    if success:
        sys.exit(0)

    sys.exit(1)
