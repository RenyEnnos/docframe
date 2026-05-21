# Política de LaTeX e Formato Final

O Infrakit usa LaTeX como formato principal para documentos acadêmicos e técnicos formais. Essa é a opção padrão quando não há outro formato obrigatório ou stack já definida.

LaTeX não deve ser imposto quando o tipo de entrega, canal de envio ou projeto existente exigir outro formato. Nesses casos, registre a exceção em `projeto/CONTEXTO_TRABALHO.md` e valide a ferramenta real de saída.

## Por Que LaTeX

LaTeX facilita:

- controle de citações;
- sumário automático;
- formatação consistente;
- tabelas e figuras com numeração;
- geração de PDF reprodutível;
- adequação a normas acadêmicas.

## Verificação Inicial

Antes de escrever o documento final, o agente deve verificar qual é o formato final correto.

Use LaTeX quando:

- o trabalho for acadêmico ou técnico formal;
- houver necessidade de citações, sumário e estrutura longa;
- o usuário não tiver outra pipeline definida;
- o PDF final deve ser reprodutível em `.tex`.

Não force LaTeX quando:

- o usuário já tiver uma stack funcional de geração;
- o formato exigido for DOCX, HTML, Markdown, formulário ou modelo institucional;
- o modo ativado declarar outro formato mais adequado;
- a entrega for currículo, perfil, documentação de software ou conteúdo web-first.

Quando LaTeX for o formato correto, verifique se existe uma ferramenta disponível.

Verificações comuns:

```bash
which pdflatex
which latexmk
which xelatex
which lualatex
```

Se nada estiver disponível, o agente deve pedir permissão antes de configurar.

Se LaTeX não for o formato correto, não peça instalação. Valide a stack real, como Python, HTML/CSS, WeasyPrint, Pandoc, Markdown, DOCX ou outra ferramenta declarada.

## Regra de Permissão

O agente não deve instalar pacotes, baixar distribuições ou alterar configuração do sistema sem autorização do usuário.

Mensagem sugerida:

```text
Não encontrei LaTeX configurado. Para gerar o PDF final, preciso configurar uma ferramenta LaTeX. Posso fazer essa configuração?
```

## Preferência de Compilação

Ordem preferida:

1. `latexmk`, quando disponível;
2. `pdflatex` com passagens suficientes;
3. `xelatex` ou `lualatex`, se houver exigência de fonte específica.

## Estrutura Recomendada do Documento

Quando o trabalho já estiver pronto para produção, o agente pode criar uma estrutura como:

```text
trabalho/
  main.tex
  referencias.bib
  secoes/
  figuras/
  tabelas/
  build/
```

Essa estrutura só deve ser criada quando fizer sentido para o projeto. No início, o agente deve primeiro entender a entrega.

## Verificação Antes de Entregar

Antes de dizer que o PDF em LaTeX está pronto, o agente deve verificar:

- compilação sem erro fatal;
- sumário e referências atualizados;
- citações resolvidas;
- figuras aparecendo;
- tabelas dentro da página;
- PDF gerado no local correto;
- checklist de entrega coerente com o tipo de trabalho.

## Verificação de Formato Alternativo

Quando o projeto usar outro formato, o agente deve verificar:

- comando de geração executado sem erro;
- arquivo final criado no local esperado;
- formato abrível pelo usuário ou canal de envio;
- layout conferido visualmente quando houver PDF, HTML ou DOCX;
- checklist coerente com o modo ativado;
- exceção ao LaTeX registrada no contexto.
