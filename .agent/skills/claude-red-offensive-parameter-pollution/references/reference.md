## Vulnerabilities

### Common HPP Vulnerabilities

```mermaid
graph LR
    subgraph "HPP Attack Vectors"
    A[HTTP Parameter Pollution] --> B[Access Control Bypass]
    A --> C[Request Forgery Enhancement]
    A --> D[Data Manipulation]
    A --> E[API Vulnerabilities]

    B --> B1[Parameter Override]
    B --> B2[Permission Escalation]

    C --> C1[CSRF Token Bypass]
    C --> C2[SSRF Augmentation]

    D --> D1[SQL Query Manipulation]
    D --> D2[Filter Evasion]

    E --> E1[Parameter Precedence]
    E --> E2[OAuth Manipulation]
    end
```

#### Access Control Bypass

- **Parameter Override**: Overriding security-related parameters
  ```
  https://example.com/admin?access=false&access=true
  ```
- **Permission Escalation**: Adding administrative parameters
  ```
  https://example.com/profile?user=victim&user=admin
  ```

#### Request Forgery Enhancement

- **CSRF Token Bypass**: Duplicating anti-CSRF tokens
  ```
  https://example.com/transfer?token=valid_token&token=random_value&amount=1000
  ```
- **SSRF Augmentation**: Overriding restricted URLs
  ```
  https://example.com/fetch?url=safe.com&url=internal.server
  ```

#### Data Manipulation

- **SQL Query Manipulation**: Influencing SQL queries
  ```
  https://example.com/products?category=1&category=1 OR 1=1
  ```
- **Filter Evasion**: Bypassing input filters
  ```
  https://example.com/search?q=safe_value&q=<script>alert(1)</script>
  ```

#### API Vulnerabilities

- **Parameter Precedence Confusion**: Different parameter precedence between API gateway and backend
- **GraphQL Parameter Pollution**: Duplicate variables in GraphQL queries
- **OAuth Parameter Manipulation**: Manipulating OAuth redirect flows
- **Header/Cookie Pollution**: Conflicting header values across CDN → WAF → app layers

### Impact Scenarios

#### Authentication Bypass

```
# Application authenticates using the first parameter but authorizes using the last
https://example.com/login?role=user&role=admin
```

#### WAF Bypass

```
# WAF checks the first parameter, backend processes the last
https://example.com/search?q=safe&q=<script>alert(1)</script>
```

#### XML External Entity (XXE) via HPP

```
# Bypassing XML filtering by parameter pollution
https://example.com/upload?xml=safe&xml=<!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
```

#### API Gateway vs Backend Precedence

```
# Gateway picks first id, backend picks last id -> IDOR/AC bypass
/api/user?id=123&id=999
```

## Methodologies

### Tools

- **Burp Suite Pro**: Parameter pollution testing via Repeater and Intruder
- **OWASP ZAP**: HTTP fuzzer for parameter testing
- **Param Miner**: Extension for discovering hidden parameters
- **HPP Finder**: Specialized tool for HPP vulnerability detection
- **Burp Repeater (Parallel)**: Validate precedence across layers quickly
- **Schemathesis**: Fuzz OpenAPI-defined endpoints for duplicate-field handling

### Testing Methodology

```mermaid
flowchart TD
    A[HPP Testing Methodology] --> B[Initial Discovery]
    A --> C[Exploit Development]
    A --> D[Impact Assessment]

    B --> B1[Map application parameters]
    B --> B2[Test duplicate parameters]
    B --> B3[Document behavior]

    C --> C1[Access control testing]
    C --> C2[Security control bypass]
    C --> C3[API security testing]

    D --> D1[Authentication bypass]
    D --> D2[Authorization bypass]
    D --> D3[Data manipulation]
```

#### Initial Discovery

1. Map all application parameters (URL, form, cookie, header)
2. Test each parameter with duplicates to observe behavior
3. Document how different application components handle parameter duplication

#### Exploiting HPP for Web Application Testing

1. **Access Control Testing**:

   ```
   # Test privileged parameter override
   https://example.com/admin?admin=false&admin=true

   # Test user context override
   https://example.com/profile?id=attacker&id=victim
   ```

2. **Security Control Bypass**:

   ```
   # Test CSRF token pollution
   token=legitimate&token=fake

   # Test parameter validation bypass
   param=valid_value&param=malicious_value
   ```

3. **API Security Testing**:

   ```
   # Test API parameter handling
   /api/v1/user?id=123&id=456

   # Test with different content types
   Content-Type: application/json
   {"id": "123", "id": "456"}
   ```

4. **HTTP Request Smuggling via HPP**:

   ```
   # Testing inconsistent interpretation
   Transfer-Encoding: chunked
   Transfer-Encoding: identity
   ```

5. **Header/Cookie Pollution**:

```
Cookie: session=abc; session=attacker
X-Forwarded-Proto: http
X-Forwarded-Proto: https
```

### Real-World Test Cases

#### E-commerce Application Testing

```
# Price manipulation
https://shop.com/checkout?price=100&price=1

# Quantity override
https://shop.com/cart?quantity=1&quantity=100
```

#### Banking Application Testing

```
# Amount parameter pollution
https://bank.com/transfer?amount=100&amount=10000

# Recipient override
https://bank.com/transfer?to=legitimate&to=attacker
```

#### CMS Admin Testing

```
# Permission bypass
https://cms.com/edit?permission=read&permission=write

# User impersonation
https://cms.com/admin?user=admin&user=victim
```

#### Social Sharing Button Parameter Pollution

A specific case of parameter pollution that affects social sharing functionality:

1. **Testing Methodology**:

   ```
   # Original share URL
   https://target.com/article

   # Polluted share URL
   https://target.com/article?u=https://attacker.com&text=malicious_text
   ```

2. **Common Parameters**:
   - `u` or `url`: The URL to be shared
   - `text`: Custom text for the share
   - `title`: Title of the shared content
   - `description`: Description for the shared content

3. **Impact**:
   - Redirect users to malicious sites
   - Modify shared content
   - Social engineering attacks
   - Brand reputation damage

4. **Testing Steps**:
   - Identify social sharing functionality
   - Analyze original share parameters
   - Append malicious parameters
   - Test each social platform separately
   - Verify if malicious content appears in share preview

## Real-World Cases and CVEs

### Notable Parameter Pollution Vulnerabilities

1. **CVE-2021-41773 - Apache HTTP Server Path Traversal**:
   - Parameter pollution in URL path normalization
   - Multiple encoded path segments bypassed access controls
   - Impact: Remote code execution via CGI scripts

2. **CVE-2018-8033 - Apache OFBiz**:
   - Parameter pollution in authentication bypass
   - Duplicate parameters in login form bypassed security checks
   - Impact: Administrative access without credentials

3. **HPP in OAuth Implementations (Multiple Vendors)**:
   - Duplicate `redirect_uri` parameters in OAuth flows
   - Gateway checked first parameter, backend used last
   - Impact: Account takeover via malicious redirect

4. **API Gateway vs Backend Precedence (Bug Bounty)**:
   - AWS API Gateway processed first `id` parameter
   - Backend Lambda function processed last `id` parameter
   - Impact: IDOR allowing access to other users' data

5. **GraphQL Rate Limit Bypass (Multiple Platforms)**:
   - Aliased queries bypassed per-query rate limits
   - 100+ identical operations in single request
   - Impact: Account enumeration, resource exhaustion

6. **WAF Bypass via HPP (Generic)**:
   - WAF inspected first parameter for XSS/SQLi
   - Backend processed last parameter
   - Impact: Complete WAF bypass for injection attacks

### Impact Ratings

- **Critical**: HPP enables authentication/authorization bypass or RCE
- **High**: HPP allows WAF bypass, payment manipulation, or privilege escalation
- **Medium**: HPP bypasses rate limiting or validation controls
- **Low**: HPP causes logic errors with minimal security impact

### Common Bug Bounty Targets

- E-commerce checkout flows (price/quantity parameters)
- OAuth/SAML redirect parameters
- API endpoints with pagination/filtering
- File upload with filename/path parameters
- Social sharing functionality
- Payment processing integrations
- Multi-step wizards/forms

## Remediation Recommendations

- **Consistent Parameter Handling**: Implement consistent handling across all application layers
- **Parameter Validation**: Validate parameters before processing
- **Framework Awareness**: Understand how your framework handles duplicate parameters
- **Web Application Firewall**: Configure WAF to detect parameter pollution attempts
- **API Gateway Rules**: Implement rules to reject duplicate parameters
- **Canonicalization**: Convert parameters to a standard form before processing
- **Schema Enforcement**: Use JSON Schema/OpenAPI validation to reject duplicates and unexpected fields
- **Drop Duplicates at the Edge**: Normalize parameters at CDN/API gateway and log events
- **Explicit Parser Settings**: e.g., in Express set a custom query parser and explicitly forbid duplicates without `[]` suffix for arrays
- **GraphQL Query Complexity Limits**: Enforce maximum query depth and alias counts
- **WebSocket Frame Validation**: Parse and validate WS message structures consistently with HTTP parameter handling

