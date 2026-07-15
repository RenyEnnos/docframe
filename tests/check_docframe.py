#!/usr/bin/env python3
"""Verificações estáticas leves do protocolo Docframe."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []

REQUIRED = [
    "README.md", "START_AQUI.md", "CHANGELOG.md",
    "agente/PROMPT_AGENTE.md", "agente/ENTREVISTA_INICIAL.md",
    "agente/ROTEAMENTO_MODOS.md", "agente/MANIFESTO_CONTEXTO.md",
    "core/REGRAS_FIXAS.md", "core/PROTOCOLO_ESTADOS.md",
    "core/SEGURANCA_CONTEUDO_EXTERNO.md", "core/PESQUISA_E_FONTES.md",
    "core/VALIDACAO_E_ENTREGA.md", "core/LATEX.md",
    "core/PDF_E_VERSOES.md", "core/GUIA_ESTILO.md", "core/LGPD_TI.md",
    "projeto/CONTEXTO_TRABALHO.md", "projeto/DECISOES.md",
    "projeto/AFIRMACOES.md", "projeto/REFERENCIAS_CANDIDATAS.md",
    "projeto/RUBRICA.md", "projeto/SCORECARD.md",
    "projeto/CHECKLIST_ENTREGA.md", "projeto/BASE_CONHECIMENTO.md",
    "projeto/REGISTRO_ITERACOES.md",
    "docs/DIAGNOSTICO_INICIAL.md", "docs/ARQUITETURA.md",
    "docs/CONTRATOS_ARQUIVOS.md", "docs/REFERENCIAS_DE_PROJETO.md",
    "docs/MIGRACAO_V2.md", "docs/TESTES_E_CENARIOS.md",
    "docs/EXEMPLOS.md", "docs/GOVERNANCA.md", "docs/DECISOES.md",
    "modos/CURRICULO_PROFISSIONAL.md",
    "modos/PROPOSTA_INSTITUCIONAL_TECNICA.md",
]

STATES = {
    "NAO_INICIADO", "DESCOBERTA", "CONTEXTO_MINIMO", "MODELAGEM",
    "PESQUISA", "PLANEJADO", "EM_PRODUCAO", "EM_VERIFICACAO",
    "AGUARDANDO_USUARIO", "BLOQUEADO", "PRONTO_PARA_REVISAO",
    "PRONTO_PARA_ENTREGA", "ENCERRADO",
}

FORBIDDEN = {
    "nome anterior residual": re.compile(r"\bInfrakit\b", re.I),
    "gate universal PDF": re.compile(r"PDF final foi gerado", re.I),
    "default universal LaTeX/PDF": re.compile(r"LaTeX/PDF, salvo", re.I),
    "default universal LaTeX": re.compile(r"LaTeX é o padrão", re.I),
}


def fail(message: str) -> None:
    ERRORS.append(message)


def read(rel: str) -> str:
    path = ROOT / rel
    if not path.is_file():
        fail(f"arquivo obrigatório ausente: {rel}")
        return ""
    return path.read_text(encoding="utf-8")


def markdown_tables(text: str) -> list[list[tuple[int, list[str]]]]:
    """Agrupa tabelas Markdown, preservando o número original de cada linha."""
    tables: list[list[tuple[int, list[str]]]] = []
    current: list[tuple[int, list[str]]] = []

    for number, line in enumerate(text.splitlines() + [""], 1):
        if line.lstrip().startswith("|"):
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            current.append((number, cells))
        elif current:
            tables.append(current)
            current = []

    return tables


for rel in REQUIRED:
    read(rel)

all_md = list(ROOT.rglob("*.md"))
corpus = "\n".join(p.read_text(encoding="utf-8") for p in all_md)
for label, pattern in FORBIDDEN.items():
    if pattern.search(corpus):
        fail(f"expressão proibida encontrada: {label}")

context = read("projeto/CONTEXTO_TRABALHO.md")
if not context.startswith("---\n"):
    fail("CONTEXTO_TRABALHO.md deve iniciar com front matter YAML")
else:
    end = context.find("\n---", 4)
    if end == -1:
        fail("front matter YAML não foi fechado")
    else:
        front = context[4:end]
        fields: dict[str, str] = {}
        for line in front.splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                fields[key.strip()] = value.strip().strip('"')
        for key in ("docframe_version", "estado", "prontidao", "tipo_entrega", "produto_final", "formato_final"):
            if key not in fields:
                fail(f"campo obrigatório ausente no front matter: {key}")
        if fields.get("estado") not in STATES:
            fail(f"estado inválido no front matter: {fields.get('estado')}")

states_doc = read("core/PROTOCOLO_ESTADOS.md")
for state in STATES:
    if f"`{state}`" not in states_doc:
        fail(f"estado não documentado em PROTOCOLO_ESTADOS.md: {state}")
for gate in ("G0", "G1", "G2", "G3", "G4", "G5", "G6"):
    if gate not in states_doc:
        fail(f"gate não documentado: {gate}")

rubric = read("projeto/RUBRICA.md")
for value in ("ATENDE", "NAO_ATENDE", "NAO_AVALIADO", "NAO_APLICAVEL"):
    if value not in rubric:
        fail(f"resultado de rubrica ausente: {value}")
if "bloqueador" not in rubric.lower():
    fail("rubrica não documenta bloqueadores")
if "evidência" not in rubric.lower():
    fail("rubrica não exige evidência")

claims = read("projeto/AFIRMACOES.md")
for field in ("Origem", "Evidência", "Confiança", "Status", "Onde usada"):
    if field.lower() not in claims.lower():
        fail(f"registro de afirmações sem campo: {field}")

refs = read("projeto/REFERENCIAS_CANDIDATAS.md")
for status in ("ENCONTRADA", "INSPECIONADA", "CONFIAVEL", "INCORPORADA", "CITADA", "DESCARTADA"):
    if status not in refs:
        fail(f"status de fonte ausente: {status}")

path_pattern = re.compile(r"`((?:core|agente|projeto|modos|docs|tests)/[A-Za-z0-9_./-]+)`")
for md in all_md:
    text = md.read_text(encoding="utf-8")
    for rel in path_pattern.findall(text):
        target = ROOT / rel.rstrip(".,;:")
        if not target.exists():
            fail(f"caminho interno quebrado em {md.relative_to(ROOT)}: {rel}")

link_pattern = re.compile(r"\[[^\]]+\]\((?!https?://|#|mailto:)([^)]+)\)")
for md in all_md:
    text = md.read_text(encoding="utf-8")
    for raw in link_pattern.findall(text):
        rel = raw.split("#", 1)[0]
        if rel and not (md.parent / rel).resolve().exists():
            fail(f"link Markdown quebrado em {md.relative_to(ROOT)}: {raw}")

for md in all_md:
    for table in markdown_tables(md.read_text(encoding="utf-8")):
        header = [cell.lower() for cell in table[0][1]]
        weight_indices = [idx for idx, name in enumerate(header) if "peso" in name]
        if not weight_indices:
            continue

        values: list[int] = []
        for _, cells in table[2:]:
            for idx in weight_indices:
                if idx < len(cells):
                    values.extend(int(value) for value in re.findall(r"(?<!\d)(\d{1,3})%", cells[idx]))

        if values and sum(values) != 100:
            fail(f"pesos em {md.relative_to(ROOT)} somam {sum(values)}%, não 100%")

missing_evidence = {"", "-", "preencher", "pendente", "não informada", "nao informada"}
validated_statuses = {"ATENDE", "SUSTENTADA", "VALIDADA"}

for md in all_md:
    for table in markdown_tables(md.read_text(encoding="utf-8")):
        header = [cell.lower() for cell in table[0][1]]
        status_idx = next(
            (idx for idx, name in enumerate(header) if name in {"resultado", "status"} or name.startswith("status ")),
            None,
        )
        evidence_idx = next(
            (idx for idx, name in enumerate(header) if "evidência" in name or "localização" in name),
            None,
        )
        if status_idx is None or evidence_idx is None:
            continue

        for row_num, cells in table[2:]:
            if status_idx >= len(cells) or evidence_idx >= len(cells):
                continue
            status = cells[status_idx].strip().upper()
            evidence = cells[evidence_idx].strip().lower()
            if status in validated_statuses and evidence in missing_evidence:
                fail(f"item validado sem evidência em {md.relative_to(ROOT)}:{row_num}")

if ERRORS:
    print("FALHA — invariantes do Docframe")
    for error in ERRORS:
        print(f"- {error}")
    sys.exit(1)

print(f"OK — {len(REQUIRED)} arquivos obrigatórios, {len(STATES)} estados e invariantes estáticos verificados.")
