# Cloud Architecture: Banking App

## Overview
This architecture transitions the monolith to a cloud-native, containerized service running on a managed cloud platform (e.g., Google Cloud Run or AWS ECS).

## Infrastructure Stack
- **IaC:** Terraform
- **Runtime:** Docker Container (Python + FastAPI/Flask)
- **Database:** Managed Relational Database (e.g., Cloud SQL)
- **CI/CD:** GitHub Actions

## Component Breakdown

### 1. Database (Cloud SQL)
- Managed instance of MySQL.
- Credentials stored in Secret Manager (not in code).

### 2. Application Service (Cloud Run / ECS)
- Containerized banking application.
- Stateless design: application logic lives in the container, state lives in the DB.

### 3. Networking
- Public-facing load balancer or API Gateway to manage traffic.
- VPC for private database access.

## Proposed Terraform Structure
```text
infrastructure/
├── main.tf        # Provider & core config
├── variables.tf   # Variable definitions
├── outputs.tf     # Terraform outputs
├── provider.tf    # Cloud provider auth
└── network.tf     # VPC & Subnet config
```

## Next Steps
1. Create `infrastructure/` directory.
2. Draft initial `main.tf` for provider configuration.
3. Review and approve the infrastructure blueprint.
