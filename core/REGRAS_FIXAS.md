# Regras Fixas do Infrakit

Estas regras valem para qualquer tipo de trabalho.

## 1. Formato Final Deve Ser Deliberado

LaTeX é o formato padrão para documentos acadêmicos e técnicos formais, mas o agente deve confirmar o formato final correto antes de configurar ferramentas.

Use LaTeX quando não houver formato obrigatório diferente e quando ele fizer sentido para a entrega.

Use o formato nativo do projeto quando a entrega exigir ou já existir uma stack adequada, como DOCX, HTML/CSS, Markdown, Python, WeasyPrint, Pandoc ou outro gerador.

Se LaTeX for necessário e não estiver instalado ou configurado, o agente deve:

1. verificar a situação;
2. explicar ao usuário o que falta;
3. pedir permissão antes de instalar ou configurar;
4. registrar a decisão.

Se LaTeX não for o formato correto, o agente não deve pedir instalação por reflexo. Ele deve registrar a exceção e validar a stack real.

## 2. O Tipo de Trabalho Não é Assumido

O agente não deve iniciar tratando tudo como TCC. Ele deve primeiro descobrir a natureza da entrega e adaptar os arquivos vivos.

Exemplos de tipos possíveis:

- TCC ou monografia;
- artigo científico;
- relatório técnico;
- relatório de aula prática;
- seminário;
- revisão bibliográfica;
- projeto de pesquisa;
- resumo expandido;
- trabalho de disciplina;
- material de apoio para apresentação.

## 3. Normas Específicas Prevalecem

A ordem de autoridade é:

1. enunciado do professor, edital, modelo ou manual obrigatório;
2. norma da instituição;
3. norma da revista, evento ou disciplina;
4. ABNT ou norma técnica geral;
5. padrão interno do Infrakit.

O agente deve registrar a base normativa adotada em `projeto/CONTEXTO_TRABALHO.md`.

## 4. Linguagem Natural e Autoral

O texto deve parecer escrito por uma pessoa que entende o tema, não por uma resposta genérica de IA.

Isso significa:

- preservar a voz do autor;
- evitar frases artificiais, simétricas demais ou cheias de clichês;
- cortar expressões vazias;
- variar a estrutura das frases;
- preferir precisão a enfeite;
- manter responsabilidade sobre fontes e dados.

O objetivo não é enganar avaliadores. O objetivo é produzir texto autoral, claro, verificável e sem marca de linguagem automática.

## 5. Fontes Precisam Ser Rastreáveis

Nenhuma citação, dado estatístico ou referência bibliográfica pode ser inventado.

Ao pesquisar, o agente deve registrar:

- fonte;
- link ou identificação;
- trecho útil em resumo;
- onde a fonte pode ser usada;
- nível de confiança.

## 6. Mudanças Devem Ser Rastreáveis

Cada sessão relevante deve deixar registro.

Para iterações simples, use `projeto/REGISTRO_ITERACOES.md`.

Para iterações grandes, crie um arquivo em `projeto/logs/` e coloque um resumo no registro principal.

## 7. Menos Bagunça, Mais Estrutura

O agente deve preferir:

- adaptar arquivos existentes em vez de criar arquivos soltos;
- manter nomes estáveis;
- separar regra fixa de conteúdo do trabalho;
- apagar ou substituir apenas com motivo claro;
- registrar decisões que afetem o futuro do projeto.
