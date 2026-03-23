---
name: universal-plugin-skill
description: Use when evaluating plugin architectures for multi-host LLM tool ecosystems to ensure portable, upgradeable, and safe plugin layouts across Claude, Qwen, Gemini, OpenCode, and Codex.
---

# Universal Plugin Skill

## Overview
Outlines a portable, layered plugin layout strategy covering core portable manifests, host adapters, and optional runtime implementations. Emphasizes separation of concerns, explicit permissions, and versioned compatibility to enable cross-host interoperability.

## When to Use
- You’re evaluating a proposed plugin structure for multi-host LLMs.
- You need a canonical layout that works across Claude, Qwen, Gemini, OpenCode, and Codex.
- You want safe defaults, explicit permissions, and upgrade/migration guidance.
- You want to ensure portability by keeping core behavior declarative and adapters as generated artifacts.

## Core Pattern
- 3-layer contract:
  1) Core portable layer: markdown + schemas
  2) Adapter layer: host glue
  3) Runtime layer: optional executable
- Portability: core behavior declarative; executable code optional
- Isolation: prompt assets vs tooling assets separated
- Safe defaults: explicit permissions; no network/file/exec access by default
- Multi-host compatibility: unknown fields ignored; basics loadable
- Upgrades: semantic versioning, stable IDs, migration notes

## Quick Reference
- Canonical assets: plugin.json, .claude-plugin/plugin.json, .mcp.json
- Portable view: tools/openapi.yaml
- Adapters: hosts/<host>/...
- Runtime (optional): runtime/
- Discovery: get_capabilities, describe_tool
- Versioning: x-tool-version, semver

## Implementation
- Draft a minimal, declarative core manifest (plugin.json) and host manifests
- Implement tools/openapi.yaml as a portable API view
- Generate hosts/<host> adapters for each supported host
- Keep runtime isolated behind permissions
- Provide on-demand schema discovery (get_capabilities, describe_tool)
- Keep CI gates for OpenAPI, schemas, and golden envelopes

## Common Mistakes
- Encoding host-specific logic in core manifests
- Ignoring unknown fields in hosts
- Forgetting explicit permissions or idempotency on mutating tools
- Relying on large, monolithic tool contracts without discovery hooks

## Real-World Impact
- Enables smoother cross-host deployments
- Reduces drift between agent prompts and tool execution
- Improves security by explicit permission declarations
