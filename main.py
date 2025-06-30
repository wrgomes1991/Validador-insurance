from datetime import datetime
from Models.proposal import Proposal
from service.validate_proposal import validate_proposal

if __name__ == "__main__":
    proposal = Proposal(cpf="14752353832", plan="S750 Amil", name="Arico", age=30, proposal_time=datetime.now())

    status = validate_proposal(proposal)
    print(f"Status: {status}")
    print(proposal)

