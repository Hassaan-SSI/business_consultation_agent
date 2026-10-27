from __future__ import annotations

from typing import Any

from app.config import settings
from app.schemas.idea import BusinessIdea


class MockStructuredLLM:
    def with_structured_output(self, schema: type[Any]) -> "MockStructuredLLM":
        self._schema = schema
        return self

    def invoke(self, _messages: Any) -> BusinessIdea:
        return BusinessIdea(
            title="Mock Coffee Shop",
            description="A neighborhood specialty coffee shop.",
            target_customer="Urban professionals aged 25-40",
            problem="Limited high-quality coffee options nearby",
            solution="Fast specialty coffee with local sourcing",
            revenue_model="Product sales and subscriptions",
            price_point=5.5,
            location="Austin, TX, USA",
            budget=75000.0,
            stage="idea",
        )


def get_llm(force_live: bool = False):
    if settings.is_mock_llm() and not force_live:
        return MockStructuredLLM()

    from langchain_google_genai import ChatGoogleGenerativeAI

    if not settings.google_api_key:
        raise RuntimeError("GOOGLE_API_KEY is required when LLM_MODE=live")

    return ChatGoogleGenerativeAI(
        model=settings.gemini_model,
        google_api_key=settings.google_api_key,
        temperature=0.2,
    )
