# User profile — {{owner_name}}

<!--
Where this file goes: keep the filled copy as a reference file in your agent's
config directory (Hermes Agent: $HERMES_HOME/USER-PROFILE.md). It is not loaded
automatically. Save the short durable facts (time zone, reply style, approval
rules, off-limits list) with your memory tool; on Hermes they land in
memories/USER.md, which has a small budget (roughly 1,400 characters).
Never publish the filled file.
-->

Filled from the bootstrap interview. Durable facts only. No secrets. Review quarterly or when something changes.

## Business
- Business: {{business_name}}
- What it does / customers: {{business_description}}
- Owner's role: {{owner_role}}
- Top recurring jobs for the agent:
  1. {{job_1}}
  2. {{job_2}}
  3. {{job_3}}
- A good week looks like: {{good_week}}

## Systems
| System | Purpose | Access granted (none / read / read-write) | Production? | Secret location (path or manager entry name, never the value) |
|---|---|---|---|---|
| {{system_1}} | {{purpose_1}} | {{access_1}} | {{prod_1}} | {{secret_location_1}} |
| {{system_2}} | {{purpose_2}} | {{access_2}} | {{prod_2}} | {{secret_location_2}} |
| {{system_3}} | {{purpose_3}} | {{access_3}} | {{prod_3}} | {{secret_location_3}} |

## Approval authority
- Primary approver: {{primary_approver}}
- Delegated approvers and their areas: {{delegated_approvers}}
- Always requires go: {{gated_actions}}
- Allowed without asking: {{autonomous_actions}}
- Approval channel and typical response time: {{approval_channel}}

## Channels and style
- Channels (mark shared vs private): {{channels}}
- Reply length and format: {{reply_style}}
- Time zone / working hours: {{timezone_hours}}
- Escalation path for urgent failures: {{escalation_path}}

## Off-limits
- Data / folders / accounts: {{off_limits_data}}
- People / topics: {{off_limits_people_topics}}
- Legal, contractual, privacy obligations: {{obligations}}

## Open items
- TODO(owner): {{open_items}}
