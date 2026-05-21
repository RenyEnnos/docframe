# Modo: Currículo Profissional

Use este modo quando o trabalho for melhorar, revisar ou produzir um currículo, CV, perfil profissional, carta de apresentação, LinkedIn ou material de candidatura.

Exemplos:

- currículo para estágio;
- currículo para emprego;
- CV acadêmico/profissional;
- perfil do LinkedIn;
- carta de apresentação;
- versão curta de currículo para WhatsApp, e-mail ou formulário.

## Princípio do Modo

Currículo não é artigo acadêmico. O documento precisa ser claro, verdadeiro, rápido de ler e adequado à vaga ou oportunidade.

O agente deve melhorar a apresentação dos fatos do usuário, mas não inventar experiência, curso, resultado, habilidade ou certificação.

## Entrevista Complementar

Além da entrevista inicial, pergunte o mínimo necessário:

1. Qual oportunidade o currículo quer atingir?
2. O foco é estágio, emprego, seleção acadêmica, bolsa, extensão, pesquisa ou outro?
3. Qual área, cargo, setor ou tipo de instituição é o alvo?
4. O usuário já tem currículo, PDF, DOCX, HTML, LinkedIn ou texto base?
5. Existe uma stack de geração já usada?
6. O resultado precisa ser PDF, DOCX, HTML, Markdown, texto curto ou mais de um formato?
7. Quais experiências são confirmadas e podem aparecer?
8. Quais cursos, eventos, estágios, projetos e habilidades são comprováveis?
9. Há algo que não deve aparecer?
10. O tom deve ser mais direto, acadêmico, rural/técnico, corporativo ou institucional?

## Formato de Saída

Use o formato mais adequado ao canal real de envio.

Para currículo, PDF e DOCX costumam ser mais úteis do que LaTeX. Se o projeto já tiver uma stack funcional, como Python + HTML/CSS + WeasyPrint ou `python-docx`, registre essa stack em `projeto/CONTEXTO_TRABALHO.md` e valide a saída nativa.

Não force LaTeX quando:

- o currículo já é gerado por uma pipeline existente;
- o usuário precisa de DOCX editável;
- a vaga exige upload em formato específico;
- a identidade visual depende de HTML/CSS;
- a entrega é web-first.

## Base de Verdade

Antes de reescrever, monte uma base factual:

| Fato | Status | Evidência ou origem |
|---|---|---|
| preencher | confirmado pelo usuário / comprovado / pendente | preencher |

Classifique como pendente qualquer informação que pareça boa, mas não esteja confirmada.

## Estrutura Recomendada

Adapte ao perfil e à vaga, mas comece por:

1. Nome e contato
2. Objetivo ou perfil profissional curto
3. Formação
4. Experiências práticas, estágios, projetos ou vivências
5. Cursos, eventos e capacitações
6. Habilidades técnicas
7. Informática, idiomas e ferramentas
8. Informações complementares relevantes

Para estudante ou início de carreira, experiências acadêmicas, extensão, monitoria, eventos e atividades práticas podem ter mais peso que emprego formal.

## Rubrica Sugerida

| Dimensão | Peso sugerido | Evidência esperada |
|---|---:|---|
| Adequação à oportunidade | 20% | currículo aponta para estágio/vaga/setor correto |
| Verdade factual | 20% | experiências e habilidades confirmadas, sem invenção |
| Clareza de leitura | 15% | recrutador entende o perfil em poucos segundos |
| Impacto profissional | 15% | atividades descritas com relevância, ação e contexto |
| Organização visual | 10% | hierarquia clara, PDF/DOCX limpo, sem excesso |
| Linguagem | 10% | texto direto, natural, sem tom inflado ou genérico |
| Compatibilidade de formato | 10% | saída adequada ao canal, validada e abrível |

## Checklist Específico

- [ ] Oportunidade alvo registrada
- [ ] Público leitor identificado
- [ ] Formato final definido
- [ ] Stack de geração registrada, se houver
- [ ] Experiências inventadas removidas
- [ ] Habilidades não comprovadas marcadas como pendência ou removidas
- [ ] Perfil profissional específico, sem frase genérica
- [ ] Formação clara
- [ ] Experiências com verbo de ação, contexto e resultado quando houver
- [ ] Cursos e eventos organizados por relevância
- [ ] Informações sensíveis ou desnecessárias removidas
- [ ] PDF final gerado e conferido
- [ ] DOCX gerado e abrível, se solicitado
- [ ] Layout legível em uma leitura rápida
- [ ] Versão final pronta para o canal de envio

## Linguagem Recomendada

Prefira:

- frases curtas;
- verbos de ação;
- contexto específico;
- termos reais da área;
- descrição proporcional à experiência do usuário.

Evite:

- "profissional altamente qualificado" sem evidência;
- "proativo, dinâmico e comunicativo" como lista genérica;
- habilidades que o usuário não confirmou;
- exagerar senioridade;
- transformar participação pontual em experiência consolidada.

## Critérios de Pronto

Classifique o estado final:

| Status | Significado |
|---|---|
| pronto para revisão do usuário | texto e layout coerentes, aguardando confirmação factual |
| pronto para candidatura | fatos confirmados, arquivo final gerado e canal de envio definido |
| pronto para revisão por terceiro | adequado para professor, orientador, colega ou profissional revisar |

Não chame de pronto para candidatura se ainda houver experiência, curso, contato ou formato pendente.
