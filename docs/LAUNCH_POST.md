# LinkedIn launch copy

Status: published on 2026-11-22 with the 45-second demo.

Live post: https://lnkd.in/p/e2XQd-Zk

An AI agent can recommend a $4,500 refund. Who authorizes it?

I have released VetoLatch 0.4.0a1, a small Python SDK for recording explicit approval state around proposed agent actions.

Install:
python -m pip install vetolatch

The 45-second demo shows a proposal entering pending_human, a scripted operator approval, and an outcome recorded under the same review_id and action_id. The SDK never calls a bank API or moves money.

The alpha is intentionally narrow. It runs in a trusted local process. Production integrations must authenticate the human, protect the decision APIs and state, and own external execution.

The public SDK is separate from my private UniversalMind cognitive-runtime research. The research continues independently, including a frozen negative result that remains on runtime hold.

I am looking for 3 independent engineers to spend 10 minutes trying the install and review flow. One useful friction report is more valuable to me than a star.

I am also opening a conversation about one paid integration pilot around a single approval boundary.

Code and friction log:
https://github.com/ImanCognitiveArch/vetolatch
Package:
https://pypi.org/project/vetolatch/

Source-available under BUSL-1.1. Evaluation and production rights follow the included terms.

## Evaluator DM template

Status: not sent today. Up to 10 relevant, individually personalized invitations are scheduled for 2026-11-23 at 10:00 America/New_York. Count actual verified sends separately from completed evaluations.

Hi [Name], I noticed your work on [specific relevant workflow].

I have released VetoLatch, a small Python alpha for explicit approval state and local audit records around agent actions. The SDK does not execute the external action.

Would you try the 10-minute local flow and share one point of friction? No model key is needed.

https://github.com/ImanCognitiveArch/vetolatch
