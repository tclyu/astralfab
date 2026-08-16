locals {
  protected_refs = [
    "refs/heads/${var.working_branch}",
    "refs/heads/${var.frozen_branch}",
  ]
}

# The repositories pre-existed this module (created by hand during the bootstrap
# window); import blocks adopt them so state is disposable and re-derivable.
import {
  for_each = var.repositories
  to       = github_repository.repo[each.key]
  id       = each.key
}

resource "github_repository" "repo" {
  for_each = var.repositories

  name       = each.key
  visibility = "public"

  has_issues      = each.value.has_issues
  has_wiki        = false
  has_projects    = false
  has_discussions = false

  allow_squash_merge          = true
  allow_merge_commit          = false
  allow_rebase_merge          = false
  squash_merge_commit_title   = "PR_TITLE"
  squash_merge_commit_message = "PR_BODY"
  delete_branch_on_merge      = true
  allow_auto_merge            = false
  allow_update_branch         = true

  web_commit_signoff_required = false

  lifecycle {
    prevent_destroy = true
  }
}

# The working line is cut from the frozen line's current tip. This must exist
# before any ruleset activates: the ruleset forbids the very ref-write that
# creates it (ordering carried by the dependency graph, not by a runbook).
resource "github_branch" "working" {
  for_each = var.repositories

  repository    = github_repository.repo[each.key].name
  branch        = var.working_branch
  source_branch = var.frozen_branch
}

resource "github_branch_default" "default" {
  for_each = var.repositories

  repository = github_repository.repo[each.key].name
  branch     = github_branch.working[each.key].branch
}

# Everyone, owner included, reaches the protected lines only through a reviewed,
# squash-merged pull request. Zero bypass actors.
resource "github_repository_ruleset" "protected_lines" {
  for_each = var.repositories

  name        = "protected-lines"
  repository  = github_repository.repo[each.key].name
  target      = "branch"
  enforcement = "active"

  conditions {
    ref_name {
      include = local.protected_refs
      exclude = []
    }
  }

  rules {
    deletion         = true
    non_fast_forward = true

    pull_request {
      required_approving_review_count   = 1
      dismiss_stale_reviews_on_push     = true
      require_code_owner_review         = false
      require_last_push_approval        = true
      required_review_thread_resolution = true
      allowed_merge_methods             = ["squash"]
    }
  }

  depends_on = [github_branch_default.default]
}

# Only the repository admin role may update the protected refs, and only via a
# pull request. This is what removes the automation account's ability to merge:
# personal repositories have no role or setting between read and write that can
# express it, but this ruleset can.
resource "github_repository_ruleset" "owner_merges_only" {
  for_each = var.repositories

  name        = "owner-merges-only"
  repository  = github_repository.repo[each.key].name
  target      = "branch"
  enforcement = "active"

  conditions {
    ref_name {
      include = local.protected_refs
      exclude = []
    }
  }

  bypass_actors {
    actor_id    = 5 # repository role: admin
    actor_type  = "RepositoryRole"
    bypass_mode = "pull_request"
  }

  rules {
    update = true
  }

  depends_on = [github_branch_default.default]
}

# Labels carry facet dimensions only, one MECE dimension per prefix. The repo
# facet is derived mechanically from the family map; absence of a repo label on
# an issue means family-wide. No label duplicates the issue hierarchy's domain
# dimension - that would be a second source of truth.
resource "github_issue_label" "repo_facet" {
  for_each = var.repositories

  repository  = var.tracker_repository
  name        = "repo:${each.key}"
  color       = "1f6feb"
  description = "Facet: concerns the ${each.key} repository"

  depends_on = [github_repository.repo]
}

resource "github_repository_milestone" "bootstrap" {
  owner       = var.owner
  repository  = var.tracker_repository
  title       = "bootstrap"
  description = "Everything required to reach the estate's initial governed state."

  depends_on = [github_repository.repo]
}
