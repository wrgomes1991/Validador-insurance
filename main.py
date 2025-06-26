from datetime import datetime
from Models.proposal import Proposal
from service.validate_proposal import validate_proposal

if __name__ == "__main__":
    proposal = Proposal(cpf="38452398832", name="Arico", age=30, proposal_time=datetime.now())

    status = validate_proposal(proposal)
    print(f"Status: {status}")

