# Security

## Current security boundary

The first public UniversalMind Governance SDK is a local reference implementation. It has no authentication and must remain bound to a loopback interface (`127.0.0.1`, `localhost`, or `::1`).

Do not expose the built-in server to a public network.

The SDK does not execute external actions. A production integration must independently enforce authentication, authorization, secure persistence, audit retention, transport security, and the external dispatch boundary.

## Reporting

Please report security issues privately to the project maintainer rather than opening a public exploit report.

GitHub maintainer: https://github.com/ImanCognitiveArch
