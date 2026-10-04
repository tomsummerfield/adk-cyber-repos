import logging
import argparse

logger = logging.getLogger(__name__)


def submit_diagnostic_bundle(bundle_path: str, remote_endpoint: str):
    """
    Submits the diagnostic bundle to the specified API endpoint.

    Args:
        bundle_path: Path to the diagnostic bundle file.
        remote_endpoint: The remote endpoint URL to submit the bundle.
    """
    try:
        with open(bundle_path, "rb") as bundle_file:
            file = bundle_file.read()
            print(f"Submitting diagnostic bundle {file} to {remote_endpoint}")
            logging.info(f"Submitting diagnostic bundle {file} to {remote_endpoint}")

    except Exception as e:
        print(f"An error occurred while submitting the diagnostic bundle: {e}")
        logging.error(f"An error occurred while submitting the diagnostic bundle: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Submit diagnostic bundle to remote endpoint."
    )
    parser.add_argument(
        "--bundle_path", type=str, help="Path to the diagnostic bundle file."
    )
    parser.add_argument(
        "--remote_endpoint",
        type=str,
        help="The remote endpoint URL to submit the bundle.",
    )

    args = parser.parse_args()
    submit_diagnostic_bundle(args.bundle_path, args.remote_endpoint)
