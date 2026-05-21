# Entrevista Inicial

Use esta entrevista para adaptar o Infrakit ao trabalho real. O usuário pode responder parcialmente. Se ele disser "não sei", registre como pendência e siga com uma hipótese conservadora.

## Como Perguntar

Não despeje todas as perguntas de uma vez se o usuário estiver inseguro. Comece pelas essenciais. Depois aprofunde.

## Perguntas Essenciais

1. Que tipo de entrega é essa?
   Exemplos: TCC, artigo, relatório, seminário, revisão bibliográfica, resumo expandido, projeto de pesquisa, estudo dirigido, trabalho de disciplina.

2. Qual é o tema ou título provisório?

3. Qual curso, disciplina, instituição ou contexto?

4. Quem vai avaliar?
   Exemplos: professor, banca, orientador, revista, evento, cliente, coordenação.

5. Existe enunciado, edital, manual, PDF, modelo ou rubrica fornecida?
   Se existir, peça o arquivo ou o texto.

6. Qual é o prazo e o tamanho esperado?
   Exemplos: número de páginas, palavras, tempo de apresentação.

7. O usuário já tem textos, dados, referências ou materiais base?

8. O agente deve pesquisar fontes externas ou usar apenas o que foi fornecido?

9. Existe uma norma obrigatória?
   Exemplos: ABNT, manual institucional, modelo do professor, template de evento.

10. O resultado final precisa ser só texto, PDF, apresentação, resumo, artigo ou mais de um produto?

11. Já existe uma ferramenta ou stack de geração do documento?
   Exemplos: LaTeX, Typst, Markdown, HTML/CSS, Python, WeasyPrint, DOCX, Google Docs.

12. O trabalho envolve proposta para uma instituição, setor, direção, coordenação, cliente interno ou órgão público?

13. O trabalho envolve sistema, rede, usuários, login, dados pessoais, servidor, arquivos ou infraestrutura de TI?

14. Há PDFs ou versões parecidas que precisam ser comparadas antes de começar?

## Perguntas de Qualidade

Use quando o contexto básico já estiver claro:

1. Qual nota, aprovação ou resultado o usuário quer atingir?
2. O trabalho deve ter tom mais acadêmico, técnico, didático ou executivo?
3. Há palavras, autores, temas ou abordagens que precisam aparecer?
4. Há algo que o professor proibiu ou criticou antes?
5. O usuário quer que o agente revise um texto existente ou escreva a partir do zero?
6. O texto precisa convencer alguém a tomar uma decisão prática?
7. Há promessas fortes no material atual, como custo zero, sem risco, garantido, 100%, todos os usuários ou total conformidade?

## Saída da Entrevista

Após a entrevista, atualize:

- `projeto/CONTEXTO_TRABALHO.md`
- `projeto/RUBRICA.md`
- `projeto/CHECKLIST_ENTREGA.md`
- `projeto/BASE_CONHECIMENTO.md`, se houver conteúdo técnico
- `projeto/REFERENCIAS_CANDIDATAS.md`, se houver busca ou fontes
- `projeto/REGISTRO_ITERACOES.md`
- módulos ativados conforme `agente/ROTEAMENTO_MODOS.md`

Depois informe ao usuário:

1. o tipo de trabalho entendido;
2. o que ainda está incerto;
3. quais arquivos foram ajustados;
4. qual é o próximo passo recomendado.
