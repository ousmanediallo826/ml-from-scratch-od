# #===========🛠️ Sandbox Challenge: Putting sys to Work===================
#
# import sys
# def main():
#     if len(sys.argv) < 2:
#         sys.stderr.write("CRITICAL ERROR: Missing task parameter argument.\n")
#         sys.stderr.write(f"Usage Guide: python3 {sys.argv[0]} <practice|analytics>\n")
#         sys.exit(1)
#     command = sys.argv[1].lower()
#
#     if command == "practice":
#         sys.stdout.write("Starting campus library book counting protocol...\n")
#     elif command == "analytics":
#         sys.stdout.write("Starting analytics library book counting protocol...\n")
#     else:
#         sys.stdout.write(f"Unknown operation directive: '{command}'\n")
#     sys.exit(0)
#
#
#
#
#
# if __name__ == "__main__":
#     main()

import os
import sys
import subprocess
def create_library_archive(source_dir: str, output_filename: str):
    """
        Uses the native shell 'tar' command to compress a directory.
        Format: tar -czf backup.tar.gz folder_name
        -c : Create a new archive
        -z : Compress the archive using gzip
        -f : Specify the filename of the archive
    """

    print(f"INIT: Commencing automated backup sequence for directory: '{source_dir}'...")

    if not os.path.exists(source_dir):
        sys.stderr.write("ERROR: Source directory does not exist!\n")
        sys.exit(1)
    try:
        result= subprocess.run(
            ["tar", "-czf", output_filename, source_dir],
            check=True,
            capture_output=True,
            text=True
        )
        print(f"SUCCESS: Archive successfully compiled -> '{output_filename}'")
        return True
    except subprocess.CalledProcessError as error:
        sys.stderr.write("SHELL EXECUTION CRASHED!\n")
        sys.stderr.write(f"System Error Output:\n{error.stderr}\n")
        return False


def verify_archive_integrity(archive_filename: str):
    """
        Uses the shell to list the contents of the compressed archive without extracting it.
        This acts as an integrity verification check.
        Format: tar -tzf backup.tar.gz
        -t : List the contents of an archive
    """

    print(f"\nINIT: Verifying archive integrity for '{archive_filename}'...")

    try:
        result = subprocess.run(
            ["tar", "-tzf", archive_filename],
            check=True,
            capture_output=True,
            text=True
        )
        print("--- Verified Archive Manifest ---")
        print(result.stdout.strip())
        print("---------------------------------")
        print("INTEGRITY CHECK: PASSED")
        return True
    except subprocess.CalledProcessError as error:
        sys.stderr.write("INTEGRITY CHECK: FAILED (Archive may be corrupted or unreadable)\n")
        return False

if __name__ == "__main__":
    TARGET_FOLDER = "campus_logs"
    BACKUP_FILE = "library_daily_backup.tar.gz"


    archive_success = create_library_archive(TARGET_FOLDER, BACKUP_FILE)
    if archive_success:
        verify_archive_integrity(BACKUP_FILE)



