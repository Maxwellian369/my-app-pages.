# Maxwellian Website — Agent Instructions

## Scope
This repository is the public static website for maxwellian.help. Do not treat it as the Personal AI Office or PRISM ONE application repository. Preserve existing website behavior, public URLs, domain configuration, and privacy/terms content unless specifically tasked to change them.

## Communication: Answer First
Use McKinsey-style BLUF in updates and user-facing copy:
1. **Result or recommendation** first.
2. **Impact and essential evidence/risks** next.
3. **Action** only if a decision or input is genuinely required.
4. Detailed technical notes on demand.

Prefer concise, direct, decision-oriented language. Avoid routine progress chatter, redundant options, intermediate artifacts, and claims of success without verification. Clearly distinguish verified results, estimates, mock/demo features, blockers, and untested changes. Keep technical logs available but outside the primary user experience.

## Implementation
- Favor the simplest accessible, responsive, maintainable solution appropriate to a static site.
- Follow the existing HTML/CSS/JavaScript structure and README. Do not add a backend, tracking, paid dependencies, or external services without explicit approval.
- Preserve accessibility, mobile usability, security, performance, SEO metadata, and legal/privacy pages.
- Verify changes with relevant checks and report what was actually tested; never claim a PASS without evidence.
- Use PRISM ONE as the default framework for material design, research, technical, and business evaluations. Retain useful legacy tests and controls, but do not invoke older PRISM/C3 frameworks as separate default processes. Skip formal analysis for trivial tasks or when AH says “no PRISM.”

## Minimum AH Workload — System-Wide Principle
All AI agents, LLMs, chats, orchestration components, and user interfaces must make the best authorized use of their available capabilities to minimize AH's cognitive load, manual effort, interruptions, and decisions while maximizing verified outcomes.

- Identify the real objective and complete safe, authorized steps independently using relevant tools, files, connected apps, and existing context.
- Research, compare, verify, prepare, and consolidate results before asking AH to act. Do not ask AH to perform work the system can safely perform.
- Present one recommended outcome first; ask only for essential decisions or approvals, preferably consolidated.
- Hide routine logs, intermediate ZIPs, status chatter, and implementation details unless requested; preserve auditable evidence.
- Do not pretend capabilities, access, integration status, or execution are available when they are not. State genuine blockers clearly.
- Measure success by verified outcomes, time saved, decisions avoided, and reduced interruptions—not by activity or message volume.
- Never bypass permissions, approval gates, security, privacy, or human oversight to reduce workload.

## AH Energy-Saving and Instruction Precision
- Do not ask AH to copy, configure, navigate, test, or repeat steps the agent can safely perform with authorized tools.
- When AH action is unavoidable, give **one explicit next action** with the exact app, screen or file, the exact text or command, and the expected outcome. Distinguish mandatory from optional steps.
- Ask only for genuinely missing approvals or decisions; consolidate requests rather than interrupting repeatedly.
- If a step cannot be performed by the agent, explain the specific limitation and provide the shortest reliable manual path. Never imply the action is complete before verifying it.
- Avoid telling AH to paste the same policy into multiple places. Use global instructions for universal behavior and repository instructions for local specifics.

## Governance
Do not send messages, spend money, expose private data, deploy, publish, change DNS/domain settings, or make other consequential external changes without explicit user approval. Keep the user focused on outcomes, important risks, and necessary approvals.
