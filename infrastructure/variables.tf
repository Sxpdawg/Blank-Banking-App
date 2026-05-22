variable "project_id" {
  description = "The Google Cloud Project ID"
  type        = string
}

variable "region" {
  description = "The deployment region"
  type        = string
  default     = "us-central1"
}
