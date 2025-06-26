from datetime import datetime

class Proposal:
    def __init__(self, cpf: str, name: str, age:int, proposal_time:datetime):
        self.cpf = cpf
        self.name = name
        self.age = age
        # self.plan = plan
        # self.coverage_amount = coverage_amount
        # self.monthly_premium = monthly_premium
        # self.city = city    
        # self.claim_history = claim_history
        self.proposal_time = proposal_time

    def __repr__(self):
        return f"Proposal(cpf={self.cpf}, name={self.name}, age={self.age})"
        