# Cloud SQL Instance for Banking App
resource "google_sql_database_instance" "banking_db" {
  name             = "banking-db-instance"
  database_version = "MYSQL_8_0"
  region           = var.region

  settings {
    tier = "db-f1-micro"
  }
}

# Database definition
resource "google_sql_database" "database" {
  name     = "banking_app"
  instance = google_sql_database_instance.banking_db.name
}

# Service Account for the Application
resource "google_service_account" "app_sa" {
  account_id   = "banking-app-service-account"
  display_name = "Banking App Service Account"
}

# Cloud Run Service
resource "google_cloud_run_v2_service" "app_service" {
  name     = "banking-app-service"
  location = var.region
  ingress  = "INGRESS_TRAFFIC_ALL"

  template {
    containers {
      image = "gcr.io/cloudrun/hello" # Placeholder image
      env {
        name  = "DB_HOST"
        value = google_sql_database_instance.banking_db.public_ip_address
      }
    }
    service_account = google_service_account.app_sa.email
  }
}
