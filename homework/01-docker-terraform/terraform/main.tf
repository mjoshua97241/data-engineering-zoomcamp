# Connect to gcp using ADC (identity verification)
provider "google" {
  project = var.project
  region  = var.region
  zone    = var.zone
}

# add these data blocks 

# This data source gets a temporary token for the service account
data "google_service_account_access_token" "default" {
  provider               = google
  target_service_account = "terraform-runner@intense-sled-344301.iam.gserviceaccount.com"
  scopes                 = ["https://www.googleapis.com/auth/cloud-platform"]
  lifetime               = "3600s"
}

# This second provider block uses that temporary token and does the real work
provider "google" {
  alias        = "impersonated"
  access_token = data.google_service_account_access_token.default.access_token
  project      = var.project
  region       = var.region
  zone         = var.zone
}

# GCP bucket
resource "google_storage_bucket" "demo-bucket" {
  name          = var.gcs_bucket_name
  location      = var.location
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}

# Big Query Dataset
resource "google_bigquery_dataset" "demo-dataset" {
  dataset_id = var.bq_dataset_name
  location   = var.location
}