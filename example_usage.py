"""
example_usage.py -- Demonstrates SalesPostCallClient
"""
from client import SalesPostCallClient

def main():
    client = SalesPostCallClient()
    result = client.analyze_transcript(
        call_transcript="We find our current system too complex. Also we are evaluating a cheaper competitor.",
        customer_name="John Doe"
    )
    print("[Sales Post-Call Result]")
    print(f"Pain Points: {result['pain_points']}")
    print(f"CRM Update: {result['crm_updates']}")
    print(f"Email:\n{result['follow_up_email']}")

if __name__ == "__main__":
    main()
