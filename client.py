"""
sales-post-call-agent-skill: Client SDK
Parses transcripts to automate CRM updates and follow-ups.
"""
from __future__ import annotations
from typing import Optional


class SalesPostCallClient:
    """
    SDK for post-call automation and transcript analysis.
    """

    def analyze_transcript(
        self,
        call_transcript: str,
        customer_name: str,
    ) -> dict:
        transcript_lower = call_transcript.lower()
        
        # Pain points extraction
        pain_points = []
        if "expensive" in transcript_lower or "budget" in transcript_lower or "price" in transcript_lower:
            pain_points.append("Price sensitivity / budget constraints")
        if "hard to use" in transcript_lower or "complex" in transcript_lower:
            pain_points.append("Product setup complexity")
        if "competitor" in transcript_lower or "alternative" in transcript_lower:
            pain_points.append("Evaluating competitors")

        # CRM updates mapping
        crm = {
            "lead_status": "Qualified" if pain_points else "Contacted",
            "deal_size_estimate": 5000 if "enterprise" in transcript_lower else 1000,
            "next_action_date": "Follow-up scheduled"
        }

        # Follow-up email template
        email_body = (
            f"Hi {customer_name},\n\n"
            f"Thank you for taking the time to speak today. "
            f"I noted your concerns regarding: {', '.join(pain_points) if pain_points else 'your current business workflow'}.\n\n"
            f"I will follow up shortly with a proposal tailored to your needs.\n\n"
            f"Best regards,\nSales Team"
        )

        return {
            "summary": "Introduction and discovery call detailing buyer requirements and timelines.",
            "pain_points": pain_points,
            "crm_updates": crm,
            "follow_up_email": email_body
        }
