from client import SalesPipelineDealOutcomeForecasterClient

def main():
    client = SalesPipelineDealOutcomeForecasterClient()
    deals = [
        {"deal_id": "DEAL_801", "amount": 120000, "stage": "PROPOSAL_SENT", "days_in_stage": 12},
        {"deal_id": "DEAL_802", "amount": 250000, "stage": "SECURITY_REVIEW", "days_in_stage": 5}
    ]
    res = client.forecast_outcomes(deals, "Q3_2026")
    print(f"Projected Revenue: ${res['projected_quarterly_revenue_usd']}")
    print(f"Win Probability: {res['win_probability_pct']}%")
    print(f"High Risk Deals: {res['high_risk_deals_count']}")

if __name__ == "__main__":
    main()
