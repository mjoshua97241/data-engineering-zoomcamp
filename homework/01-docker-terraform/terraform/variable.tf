variable "project" {
  description = "Project"
  default     = "intense-sled-344301"
}

variable "region" {
  description = "Project region"
  default     = "us-central1"
}

variable "zone" {
  description = "Project zone"
  default     = "us-central1-a"
}

variable "location" {
  description = "Project location"
  default     = "US"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "intense-sled-344301-terra-bucket"
}

variable "bq_dataset_name" {
  description = "My BigQuery dataset name"
  default     = "demo_dataset"
}