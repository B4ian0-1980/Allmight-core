# SKILL: File Upload Vulnerabilities

## Metadata
- **Skill Name**: file-upload
- **Folder**: offensive-file-upload
- **Source**: https://github.com/SnailSploit/offensive-checklist/blob/main/file-upload.md

## Description
Unrestricted and insecure file upload testing checklist: arbitrary file upload discovery, extension validation bypass (double extensions, null byte, alternate extensions), Content-Type spoofing, magic byte manipulation, path traversal in filename, polyglot files, image-based web shells, race condition execution, and server-side impact escalation (RCE, defacement, stored XSS, SSRF).

## Trigger Phrases
Use this skill when the conversation involves any of:
`file upload, unrestricted upload, webshell, shell upload, mime bypass, magic bytes, extension bypass, double extension, upload RCE, avatar upload bypass, SVG XSS`

## Instructions for Claude

When this skill is active:
1. Load and apply the full methodology below as your operational checklist
2. Follow steps in order unless the user specifies otherwise
3. For each technique, consider applicability to the current target/context
4. Track which checklist items have been completed
5. Suggest next steps based on findings

---

## Full Methodology

# Unrestricted & Insecure File Upload

## Shortcut

- Identify all endpoints accepting file uploads (avatars, attachments, media, resumes, archives).
- Test basic upload with direct executable extensions (`.php`, `.jsp`, `.aspx`, `.py`).
- If restricted by extension, test bypass techniques (alternative extensions, double extensions, case variations, path traversal).
- If restricted by Content-Type header, spoof header with allowed MIME types (`image/jpeg`, `image/png`).
- If restricted by file contents (magic bytes), prepend legitimate magic bytes to payload.
- Verify file storage location: is it web-accessible? Is directory execution enabled?
- Escalation: attempt code execution (Web Shell), stored XSS (SVG/HTML), or file overwrites.

## Mechanisms

Insecure file upload occurs when an application accepts files from users without adequate validation of filename, file type, file size, or content, permitting attackers to upload executable code directly to the server filesystem.

### Attack Vectors & Bypass Matrix

| Protection Mechanism | Bypass Technique |
| :--- | :--- |
| **Blacklist Extension** | Alternative extensions (`.phtml`, `.php5`, `.phar`, `.jspx`, `.ashx`, `.config`) |
| **Case Sensitivity** | `.PhP`, `.jSp`, `.AsPx` |
| **Trailing Dots / Spaces (Windows)** | `shell.php.`, `shell.php `, `shell.asp::$DATA` |
| **Null Byte Injection (Legacy)** | `shell.php%00.jpg`, `shell.php\x00.png` |
| **Client-Side Validation Only** | Intercept HTTP request with Burp Suite / proxy and alter payload |
| **MIME / Content-Type Check** | Change `Content-Type: application/x-php` to `image/jpeg` |
| **Magic Byte Header Check** | Prepend `GIF89a;` or `\xFF\xD8\xFF\xE0` before payload |
| **Embedded Polyglots** | Embed PHP code inside EXIF comment metadata of valid JPEG/PNG |
| **Filename Path Traversal** | Set filename to `../../shell.php` to write outside upload directory |
| **Archive Slip (Zip Slip)** | Archive containing `../../evil.sh` extracted on server |
