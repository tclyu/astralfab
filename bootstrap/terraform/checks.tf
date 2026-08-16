# Collaborator membership is asserted, never managed. Granting access creates an
# invitation that only the invitee can accept - a two-party act. A module that
# "managed" collaborators would report success at invitation time while the
# membership does not yet exist, and a scaffold built on that would fail at its
# first push, far from the cause.

data "github_collaborators" "all" {
  for_each = var.repositories

  owner       = var.owner
  repository  = each.key
  affiliation = "all"
}

check "collaborators" {
  assert {
    condition = alltrue([
      for r in keys(var.repositories) : contains(
        [for c in data.github_collaborators.all[r].collaborator : c.login
        if c.permission == "admin"],
        var.owner
      )
    ])
    error_message = "The owner must hold admin on every repository in the family."
  }

  assert {
    condition = alltrue([
      for r in keys(var.repositories) : contains(
        [for c in data.github_collaborators.all[r].collaborator : c.login
        if contains(["push", "write", "maintain", "admin"], c.permission)],
        var.automation_login
      )
    ])
    error_message = "The automation account must hold write on every repository. Grant it as the owner, then accept the invitation as the automation account - Terraform cannot perform either half."
  }
}
