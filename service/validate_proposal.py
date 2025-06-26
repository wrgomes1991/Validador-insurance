def validate_proposal(proposal):
    if not proposal.cpf or len(proposal.cpf) != 11 or not proposal.cpf.isdigit():
        return "Rejected: Invalid CPF"

    if proposal.age not in range(18,70):
        return "Rejected: Age not allowed for selected plan"
    
    if proposal.proposal_time.hour in range(0,6):
        return "not allowed during risk window"

    # if proposal.monthly_premium < proposal.coverage_amount * 0.0012:
    #     return "Rejected: Monthly premium below minimum threshold"

    # if proposal.city in ["Rio de Janeiro", "Salvador", "Manaus"]:
    #     return "Rejected: Proposal blocked due to city risk profile"

    # if proposal.has_claim_history:
    #     return "Pending: Requires manual underwriting"

    # if 0 <= proposal.proposal_time.hour <= 5:
    #     return "Rejected: Submissions not allowed during risk window"

    return "Approved"
