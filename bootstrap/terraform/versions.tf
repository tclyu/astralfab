terraform {
  required_version = ">= 1.7.0" # import blocks with for_each

  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 6.13"
    }
  }
}

# Token comes from the GITHUB_TOKEN environment variable.
# Plan (read-only) runs with the automation credential; apply requires the
# owner's admin credential and the owner's explicit authorization.
provider "github" {
  owner = var.owner
}
