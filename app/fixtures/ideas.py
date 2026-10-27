from app.schemas.idea import BusinessIdea, TeamMember


def coffee_shop_idea() -> BusinessIdea:
    return BusinessIdea(
        title="Neighborhood Roast",
        description="Specialty coffee shop focused on local beans and fast service.",
        target_customer="Urban professionals and students",
        problem="Few convenient specialty coffee options in the area",
        solution="High-quality espresso drinks with subscription refills",
        revenue_model="Beverage and pastry sales plus monthly subscription",
        price_point=6.0,
        currency="USD",
        location="Austin, TX, USA",
        budget=80000.0,
        team=[TeamMember(name="Alex", role="Founder", skills=["operations", "sales"])],
        stage="idea",
    )
