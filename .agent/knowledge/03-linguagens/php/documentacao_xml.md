---json
{
  "id": "documentacao_xml",
  "title": "Documentação XML — Guia Completo",
  "categoria": "03-linguagens",
  "subcategoria": "php",
  "resumo": "**Fonte:** [W3Schools XML](https://www.w3schools.com/xml/default.asp) · [MDN XML](https://developer.mozilla.org/en-US/docs/Web/XML) **Versão:** XML 1.0/1.1",
  "gatilhos": [
    "completo",
    "documentacao",
    "guia",
    "linguagens",
    "php",
    "xml"
  ],
  "perguntas_tipo": [
    "Como utilizar Documentação XML — Guia Completo?",
    "Quais as boas praticas de php?"
  ],
  "nao_cobre": [],
  "target_agent": [
    "general-assistant"
  ],
  "source": {
    "origin": "AllMight Knowledge Base",
    "original_format": "markdown"
  },
  "atualizado_em": "2026-10-15",
  "verificado_em": "2026-10-15",
  "dono": "stack-php",
  "prioridade": 2
}
---

# Documentação XML — Guia Completo

> **Fonte:** [W3Schools XML](https://www.w3schools.com/xml/default.asp) · [MDN XML](https://developer.mozilla.org/en-US/docs/Web/XML)
> **Versão:** XML 1.0/1.1
> **Atualizado:** 2026-02-14

---

## Sumário

1. [Fundamentos](#fundamentos)
2. [Estrutura e Sintaxe](#estrutura-e-sintaxe)
3. [DTD — Validação](#dtd--validação)
4. [XML Schema (XSD)](#xml-schema-xsd)
5. [Namespaces](#namespaces)
6. [XPath](#xpath)
7. [XSLT](#xslt)
8. [Parsing em Linguagens](#parsing-em-linguagens)

---

## Fundamentos

XML (eXtensible Markup Language) é uma linguagem de marcação para armazenar e transportar dados de forma estruturada e legível.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<mensagem>
    <de>Maria</de>
    <para>João</para>
    <assunto>Reunião</assunto>
    <corpo>Reunião às 14h amanhã.</corpo>
</mensagem>
```

### Diferenças XML vs HTML

| XML | HTML |
|---|---|
| Transportar dados | Exibir dados |
| Tags definidas pelo usuário | Tags predefinidas |
| Case sensitive | Case insensitive |
| Fechamento obrigatório | Fechamento opcional |
| Atributos com aspas obrigatórias | Aspas opcionais |

---

## Estrutura e Sintaxe

### Regras Fundamentais

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- Comentário XML -->

<catalogo>
    <!-- Elemento raiz (obrigatório, único) -->

    <!-- Elementos aninhados -->
    <livro id="1" isbn="978-85-123-4567-8">
        <titulo>Guia XML</titulo>
        <autor>Ana Silva</autor>
        <preco moeda="BRL">49.90</preco>
        <publicacao>2026-01-15</publicacao>
        <categorias>
            <categoria>Tecnologia</categoria>
            <categoria>Referência</categoria>
        </categorias>
    </livro>

    <!-- Elemento vazio (self-closing) -->
    <separador/>

    <!-- CDATA (conteúdo literal, sem parsing) -->
    <codigo><![CDATA[
        if (a < b && c > d) {
            return true;
        }
    ]]></codigo>

    <!-- Entidades predefinidas -->
    <!-- &lt; (<)  &gt; (>)  &amp; (&)  &apos; (')  &quot; (") -->
    <nota>Preço &lt; R$50 &amp; frete grátis</nota>
</catalogo>
```

### Regras

1. **Um único elemento raiz**
2. **Tags são case-sensitive** (`<Nome>` ≠ `<nome>`)
3. **Elementos devem ser fechados** (`<br/>` ou `<br></br>`)
4. **Aninhamento correto** (`<a><b></b></a>` ✅, `<a><b></a></b>` ❌)
5. **Valores de atributos entre aspas**

---

## DTD — Validação

```xml
<!-- DTD interna -->
<?xml version="1.0"?>
<!DOCTYPE catalogo [
    <!ELEMENT catalogo (livro+)>
    <!ELEMENT livro (titulo, autor, preco)>
    <!ATTLIST livro id ID #REQUIRED>
    <!ELEMENT titulo (#PCDATA)>
    <!ELEMENT autor (#PCDATA)>
    <!ELEMENT preco (#PCDATA)>
    <!ATTLIST preco moeda CDATA "BRL">
]>
<catalogo>
    <livro id="L1">
        <titulo>XML Básico</titulo>
        <autor>Ana</autor>
        <preco moeda="BRL">39.90</preco>
    </livro>
</catalogo>
```

### Indicadores de Cardinalidade

| Símbolo | Significado |
|---|---|
| (nenhum) | Exatamente 1 |
| `+` | 1 ou mais |
| `*` | 0 ou mais |
| `?` | 0 ou 1 |
| `\|` | OU (alternativa) |

---

## XML Schema (XSD)

```xml
<!-- catalogo.xsd -->
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">

    <xs:element name="catalogo">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="livro" maxOccurs="unbounded">
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element name="titulo" type="xs:string"/>
                            <xs:element name="autor" type="xs:string"/>
                            <xs:element name="preco" type="xs:decimal"/>
                            <xs:element name="publicacao" type="xs:date" minOccurs="0"/>
                        </xs:sequence>
                        <xs:attribute name="id" type="xs:positiveInteger" use="required"/>
                        <xs:attribute name="isbn" type="xs:string"/>
                    </xs:complexType>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>

</xs:schema>
```

### Tipos XSD Comuns

| Tipo | Exemplo |
|---|---|
| `xs:string` | "texto" |
| `xs:integer` | 42 |
| `xs:decimal` | 19.99 |
| `xs:boolean` | true/false |
| `xs:date` | 2026-02-14 |
| `xs:dateTime` | 2026-02-14T15:30:00 |
| `xs:time` | 15:30:00 |
| `xs:anyURI` | https://exemplo.com |

---

## Namespaces

```xml
<?xml version="1.0"?>
<raiz
    xmlns:h="http://www.w3.org/1999/xhtml"
    xmlns:f="https://exemplo.com/financeiro">

    <h:table>
        <h:tr><h:td>HTML Table</h:td></h:tr>
    </h:table>

    <f:table>
        <f:nome>Fatura</f:nome>
        <f:valor>1500.00</f:valor>
    </f:table>
</raiz>

<!-- Default namespace -->
<catalogo xmlns="https://exemplo.com/catalogo">
    <livro>...</livro>
</catalogo>
```

---

## XPath

```xpath
/catalogo/livro             <!-- Filhos diretos -->
//livro                      <!-- Qualquer livro no doc -->
/catalogo/livro[1]          <!-- Primeiro livro -->
/catalogo/livro[last()]     <!-- Último livro -->
//livro[@id='1']            <!-- Atributo igual -->
//livro[preco>30]           <!-- Filtro por valor -->
//livro/titulo/text()       <!-- Texto do título -->
//livro[@isbn]              <!-- Livros com atributo isbn -->
//livro[position()<=3]      <!-- Três primeiros -->
//livro/autor | //livro/titulo  <!-- União -->

<!-- Eixos -->
//livro/child::titulo       <!-- Filho -->
//titulo/parent::livro      <!-- Pai -->
//livro/descendant::*       <!-- Descendentes -->
//titulo/ancestor::catalogo <!-- Ancestral -->
//livro/following-sibling::livro  <!-- Irmãos seguintes -->
```

---

## XSLT

```xml
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:template match="/">
        <html>
        <body>
            <h1>Catálogo</h1>
            <table border="1">
                <tr><th>Título</th><th>Autor</th><th>Preço</th></tr>
                <xsl:for-each select="catalogo/livro">
                    <xsl:sort select="preco" data-type="number" order="ascending"/>
                    <tr>
                        <td><xsl:value-of select="titulo"/></td>
                        <td><xsl:value-of select="autor"/></td>
                        <td>
                            <xsl:if test="preco &gt; 50">
                                <xsl:attribute name="style">color:red</xsl:attribute>
                            </xsl:if>
                            R$ <xsl:value-of select="preco"/>
                        </td>
                    </tr>
                </xsl:for-each>
            </table>
        </body>
        </html>
    </xsl:template>

</xsl:stylesheet>
```

---

## Parsing em Linguagens

### JavaScript (Browser)

```javascript
// Parse string XML
const parser = new DOMParser();
const xml = parser.parseFromString(xmlString, "text/xml");
const titulos = xml.getElementsByTagName("titulo");
for (let t of titulos) console.log(t.textContent);

// Fetch XML
const res = await fetch("dados.xml");
const xml = await res.text();
const doc = new DOMParser().parseFromString(xml, "text/xml");
```

### Python

```python
import xml.etree.ElementTree as ET

# Parse arquivo
tree = ET.parse("catalogo.xml")
root = tree.getroot()

# Parse string
root = ET.fromstring(xml_string)

# Navegar
for livro in root.findall("livro"):
    titulo = livro.find("titulo").text
    preco = float(livro.find("preco").text)
    id = livro.get("id")
    print(f"{titulo}: R${preco}")

# Criar XML
root = ET.Element("catalogo")
livro = ET.SubElement(root, "livro", id="1")
ET.SubElement(livro, "titulo").text = "Guia XML"
tree = ET.ElementTree(root)
tree.write("saida.xml", encoding="utf-8", xml_declaration=True)
```

### PHP

```php
// SimpleXML (leitura)
$xml = simplexml_load_file("catalogo.xml");
foreach ($xml->livro as $livro) {
    echo $livro->titulo . ": R$" . $livro->preco . "\n";
}

// DOMDocument (manipulação completa)
$doc = new DOMDocument();
$doc->load("catalogo.xml");
$livros = $doc->getElementsByTagName("livro");
foreach ($livros as $livro) {
    echo $livro->getAttribute("id") . "\n";
}
```

---

*Fonte: [W3Schools XML](https://www.w3schools.com/xml/) · [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/XML)*
