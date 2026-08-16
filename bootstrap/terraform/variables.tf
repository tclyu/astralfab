variable "owner" {
  description = "GitHub account that owns the repository family. Its admin credential is required at apply."
  type        = string
}

variable "automation_login" {
  description = "Machine account that authors branches and pull requests. Must already hold write access; the grant and its acceptance are a two-party act this module only asserts, never performs."
  type        = string
}

variable "repositories" {
  description = "The repository family. Exactly one member is the tracker (has_issues = true)."
  type = map(object({
    has_issues = bool
  }))

  validation {
    condition     = length([for r in values(var.repositories) : r if r.has_issues]) == 1
    error_message = "Exactly one repository must carry the family's issue tracker."
  }
}

variable "tracker_repository" {
  description = "Name of the repository that carries the family's single issue tracker."
  type        = string
}

variable "working_branch" {
  description = "The working line. Default branch; every change arrives by reviewed, squash-merged pull request."
  type        = string
  default     = "integration"
}

variable "frozen_branch" {
  description = "The ledger line the working branch is cut from. Protected identically and never pushed at this stage."
  type        = string
  default     = "main"
}
