---json
{
  "id": "documentacao_struts",
  "title": "Documentação: Apache Struts",
  "categoria": "03-linguagens",
  "subcategoria": "php",
  "resumo": "**Linguagem:** Java (Enterprise) **Tipo:** Framework MVC Action-Based",
  "gatilhos": [
    "apache",
    "documentacao",
    "linguagens",
    "php",
    "struts"
  ],
  "perguntas_tipo": [
    "Como utilizar Documentação: Apache Struts?",
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

# Documentação: Apache Struts

> **Linguagem:** Java (Enterprise)
> **Tipo:** Framework MVC Action-Based
> **Status:** Maduro / Legado
> **Site Oficial:** [struts.apache.org](https://struts.apache.org/)

## O que é?
O Apache Struts é um framework open-source elegante e extensível para criar aplicações web em Java. Ele foi o pioneiro do padrão MVC (Model-View-Controller) no ecossistema Java EE. Embora o Spring MVC tenha ganhado mais popularidade recentemente, o Struts (especialmente a versão Struts 2) ainda é amplamente utilizado em sistemas corporativos robustos.

## Arquitetura (Struts 2)
O Struts 2 é baseado no padrão "Action".
1.  **FilterDispatcher:** O controlador frontal que intercepta todas as requisições.
2.  **Action:** A classe que contém a lógica de negócio para tratar a requisição.
3.  **Result:** Determina o que retornar (JSP, FreeMarker, JSON).
4.  **Interceptors:** Camadas que processam a requisição antes/depois da Action (validação, upload, logging).

## Estrutura Básica (`struts.xml`)
O arquivo de configuração central.

```xml
<struts>
    <package name="default" extends="struts-default">
        <action name="hello" class="com.example.HelloAction">
            <result name="success">/hello.jsp</result>
        </action>
    </package>
</struts>
```

## Exemplo de Action

```java
package com.example;

import com.opensymphony.xwork2.ActionSupport;

public class HelloAction extends ActionSupport {
    private String message;

    public String execute() {
        message = "Olá, Struts!";
        return SUCCESS;
    }

    public String getMessage() {
        return message;
    }
}
```

## OGNL (Object-Graph Navigation Language)
O Struts usa OGNL para ligar dados da View (JSP) às propriedades da Action.

```jsp
<!-- hello.jsp -->
<h1><s:property value="message"/></h1>
```

## Segurança
Devido à sua popularidade e idade, o Struts foi alvo de várias vulnerabilidades de alto perfil no passado.
> **IMPORTANTE:** Sempre mantenha o Struts atualizado para a versão mais recente (atualmente série 6.x ou 7.x) para evitar falhas de execução remota de código (RCE).

## Referências
*   [Getting Started](https://struts.apache.org/getting-started/)
*   [Security Bulletins](https://struts.apache.org/security/)
