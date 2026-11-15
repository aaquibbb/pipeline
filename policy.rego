package security

deny contains msg if {
    r := input.runs[0].results[_]
    r.level == "error"
    contains(r.message.text, "Severity: CRITICAL")
    msg := sprintf("%s: %s", [r.ruleId, r.message.text])
}
