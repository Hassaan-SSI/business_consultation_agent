from app.schemas.analysis import AspectAnalysis, Citation


def market_analysis() -> AspectAnalysis:
    return AspectAnalysis(
        aspect="market",
        summary="Moderate demand in urban specialty coffee segment.",
        findings=[
            "Three established competitors within 2 miles",
            "Price sensitivity for daily commuters",
        ],
        metrics={
            "tam_usd": 2_400_000_000,
            "sam_usd": 48_000_000,
            "som_usd": 480_000,
            "suggested_price_low": 4.5,
            "suggested_price_mid": 6.0,
            "suggested_price_high": 8.0,
            "competitors": ["Blue Bottle Lite", "Corner Grind", "Bean & Go"],
        },
        score=7.2,
        confidence=0.65,
        citations=[Citation(source="stub market scan", snippet="Placeholder benchmark data")],
        status="stub",
    )


def technical_analysis() -> AspectAnalysis:
    return AspectAnalysis(
        aspect="technical",
        summary="MVP is operationally focused with light software.",
        findings=["POS and inventory tooling required", "No custom mobile app needed for MVP"],
        metrics={
            "stack": ["Square POS", "QuickBooks", "Notion ops"],
            "complexity_score": 3,
            "mvp_cost_usd": 22000,
            "timeline_weeks": 10,
        },
        score=8.0,
        confidence=0.7,
        status="stub",
    )


def compliance_analysis() -> AspectAnalysis:
    return AspectAnalysis(
        aspect="compliance",
        summary="Standard food-service and business registration requirements apply.",
        findings=["Food handler permits required", "Sales tax registration needed"],
        metrics={"license_count_estimate": 3},
        score=6.5,
        confidence=0.55,
        citations=[Citation(source="stub compliance guide", snippet="Placeholder regulation summary")],
        status="stub",
    )
