
# Insurance Validator

Validador de propostas de seguro com foco em regras de negócio críticas, modularidade e escalabilidade evolutiva.

## Objetivo

Este projeto tem como finalidade validar propostas de seguros com base em critérios definidos por negócio, simulando cenários reais de análise automatizada antes da submissão para subscrição. A estrutura foi desenhada visando boas práticas de arquitetura, desacoplamento de responsabilidade e testes unitários.

## Estrutura de Pastas

```
insurance_validator/
├── models/
│   └── proposal.py            # Modelo de domínio: proposta de seguro
├── service/
│   └── validate_proposal.py   # Lógica de validação das regras de negócio
├── tests/
│   └── test_validator.py      # Testes unitários e casos de borda (em desenvolvimento)
└── main.py                    # Execução principal e simulação de submissão
```

## Regras de Negócio Implementadas

- CPF obrigatório, com 11 dígitos numéricos
- Faixa etária entre 18 e 69 anos
- Submissões realizadas entre 00h00 e 06h00 são bloqueadas (janela de risco)
- Pronto para expansão com validações como:
  - Histórico de sinistro
  - Perfil de cidade
  - Análise atuarial de prêmio x cobertura

## Execução

Clone o repositório e execute o `main.py` para simular uma submissão:

```bash
git clone https://github.com/seuusuario/insurance_validator.git
cd insurance_validator
python main.py
```

## Requisitos

- Python 3.9+
- Poetry ou pip para gerenciar dependências (opcional, pois não há pacotes externos ainda)

## Exemplo de Saída

```bash
Status: Approved
Proposal(plan=S750 Amil, name=Arico, age=30, Date=2025-06-29 19:45:21.568201)
```

## Expansões Futuras

- Integração com base de dados externa para blacklist de CPF
- Publicação como microserviço RESTful via FastAPI
- Pipeline de CI/CD com validação automática de regras e testes
- Dashboard de regras negadas/aprovadas via Prometheus/Grafana

## Contribuições

Este projeto foi idealizado para fins de estudo, prototipação de regras e compartilhamento de conhecimento. Feedbacks e PRs são bem-vindos!

## Autor

**William Gomes**  
Analista SRE/DevOps | Foco em sistemas resilientes e modelagem de regras de negócio  
[LinkedIn](https://www.linkedin.com/in/william-gomes-52376473/) | [GitHub](https://github.com/wrgomes1991/)
