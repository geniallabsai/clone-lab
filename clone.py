#!/usr/bin/env python3
"""CloneLab CLI — orquestra o pipeline de clonagem criativa.

Uso:
  clone.py init <pasta-dataset>                 estrutura + varredura das fotos
  clone.py cenario [--tipo X] [--seed N]        escolhe cenário (SEMPRE 0–15)
  clone.py prompt --nro N [--acao "..."] [--variacoes K] [--slug s]
                                                 monta drafts/<job>/ completo
  clone.py qc <dir-job>                         valida entrega estrutural (16 itens)
  clone.py check                                self-teste: sorteios sempre em 0..15

Global: --root <pasta> (senão procura CLONE-CONFIG.json subindo do cwd)
Python 3 stdlib apenas.
"""
import argparse, hashlib, json, re, struct, sys, unicodedata
from datetime import datetime, timezone
from pathlib import Path

PACOTE = Path(__file__).resolve().parent
CAT = json.loads((PACOTE / "scenarios" / "catalogo.json").read_text(encoding="utf-8"))
NEG = json.loads((PACOTE / "scenarios" / "negativos.json").read_text(encoding="utf-8"))
NAT = CAT.get("naturalismo", {})
N_MAX = CAT["faixa"][1]
FOTOS = {".jpg", ".jpeg", ".png", ".webp"}
SUBDIRS = ["_identity", "drafts", "saida", "state"]


def agora_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def slugify(s):
    s = re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-")
    return s[:40] or "sem-titulo"


def norm(s):
    """minúsculas sem acentos — matching de keywords imune a ç/ã/etc."""
    s = unicodedata.normalize("NFD", str(s).lower())
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def find_root(explicit=None):
    if explicit:
        p = Path(explicit).expanduser().resolve()
        if not (p / "CLONE-CONFIG.json").exists():
            sys.exit(f"--root sem CLONE-CONFIG.json: rode clone.py init em {p}")
        return p
    for cand in [Path.cwd().resolve(), *Path.cwd().resolve().parents]:
        if (cand / "CLONE-CONFIG.json").exists():
            return cand
    sys.exit("workspace não encontrado (procurei subindo do cwd). Rode: clone.py init <pasta>")


def carregar(root):
    return json.loads((root / "CLONE-CONFIG.json").read_text(encoding="utf-8"))


def gravar(root, cfg):
    (root / "CLONE-CONFIG.json").write_text(
        json.dumps(cfg, indent=2, ensure_ascii=False), encoding="utf-8")


def dimensoes(p):
    try:
        b = p.read_bytes()[:65536]
        if b[:8] == b"\x89PNG\r\n\x1a\n":
            w, h = struct.unpack(">II", b[16:24])
            return w, h
        if b[:2] == b"\xff\xd8":
            i = 2
            while i + 9 <= len(b):
                if b[i] != 0xFF:
                    i += 1
                    continue
                m = b[i + 1]
                if m in (0xC0, 0xC1, 0xC2, 0xC3):
                    h, w = struct.unpack(">HH", b[i + 5:i + 9])
                    return w, h
                if m in (0xD8, 0x01) or 0xD0 <= m <= 0xD7:
                    i += 2
                    continue
                seg = int.from_bytes(b[i + 2:i + 4], "big")
                i += 2 + seg
    except Exception:
        pass
    return None


# ---------------- init ----------------
def cmd_init(a):
    raiz = Path(a.pasta).expanduser().resolve()
    raiz.mkdir(parents=True, exist_ok=True)
    made = []
    for d in SUBDIRS:
        p = raiz / d
        if not p.is_dir():
            p.mkdir(parents=True)
            made.append(d + "/")
    fotos, problemas = [], []
    for p in sorted(raiz.iterdir()):
        if p.is_file() and p.suffix.lower() in FOTOS:
            wh = dimensoes(p)
            fotos.append((p.name, wh))
            if wh and min(wh) < 400:
                problemas.append(f"{p.name}: {wh[0]}x{wh[1]} (pequena p/ detalhe facial)")
            elif wh is None:
                problemas.append(f"{p.name}: dimensões ilegíveis")
    idir = raiz / "_identity"
    mapa_t = PACOTE / "identity" / "mapeamento-facial.template.md"
    ident_t = PACOTE / "identity" / "identidade.template.txt"
    mapa = idir / "mapeamento-facial.md"
    ident = idir / "identidade.txt"
    if not mapa.exists():
        mapa.write_text(mapa_t.read_text(encoding="utf-8"), encoding="utf-8")
        made.append("_identity/mapeamento-facial.md (template)")
    if not ident.exists():
        ident.write_text(ident_t.read_text(encoding="utf-8"), encoding="utf-8")
        made.append("_identity/identidade.txt (template)")
    cfg_path = raiz / "CLONE-CONFIG.json"
    cfg = {"dataset": str(raiz), "created": agora_iso(),
           "last_scenarios": [], "entregas": []}
    if cfg_path.exists():
        cfg.update(carregar(raiz))
        cfg["dataset"] = str(raiz)
    gravar(raiz, cfg)
    print(f"[clone-lab] init ok: {raiz}")
    for m in made:
        print("  +", m)
    print(f"[clone-lab] dataset: {len(fotos)} foto(s) encontradas")
    for n, wh in fotos:
        print(f"   · {n} ({wh[0]}x{wh[1]})" if wh else f"   · {n} (?)")
    for pr in problemas:
        print("  WARN", pr)
    if len(fotos) < 3:
        print("  WARN menos de 3 fotos: a análise de identidade ficará fraca; "
              "envie 5+ ângulos diferentes (frente, ¾, perfil, luz variada)")
    print("[clone-lab] próximo: fase 1 (agente 01 analisa e preenche _identity/)")


# ---------------- cenario ----------------
def por_tipo(tipo):
    t = tipo.strip().lower()
    for e in CAT["enarios"]:
        if t == e["nome"].lower() or t in e["aliases"]:
            return e
    return None


def escolher(cfg, tipo=None, seed=None, silencioso=False):
    usados = [n for n in cfg.get("last_scenarios", [])[-3:]]
    if tipo is not None:
        e = por_tipo(tipo)
        if e is None:
            nomes = ", ".join(x["nome"] for x in CAT["enarios"])
            sys.exit(f"tipo '{tipo}' não reconhecido.\nCenários válidos: {nomes}")
        n = e["nro"]
    else:
        s = str(seed) if seed is not None else f"{agora_iso()}-{len(cfg.get('last_scenarios', []))}"
        h = int(hashlib.sha256(s.encode("utf-8")).hexdigest(), 16)
        ordem = sorted((e["nro"] for e in CAT["enarios"]),
                       key=lambda x: (h >> ((x * 7) % 512)) & 0xFFFF)
        n = next((x for x in ordem if x not in usados), ordem[-1])
    assert 0 <= n <= N_MAX, f"numeração fora da faixa: {n}"
    entry = next(e for e in CAT["enarios"] if e["nro"] == n)
    # histórico sempre avança (anti-repetição dos últimos 3)
    cfg.setdefault("last_scenarios", []).append(n)
    cfg["last_scenarios"] = cfg["last_scenarios"][-10:]
    return entry


def cmd_cenario(a):
    root = find_root(a.root)
    cfg = carregar(root)
    e = escolher(cfg, tipo=a.tipo, seed=a.seed)
    gravar(root, cfg)
    print(f"CENÁRIO: {e['nro']} — {e['nome']}")
    print(f"proporção: {e['aspecto']} · quando usar: {e['quando']}")
    log = root / "state" / "cenario-log.jsonl"
    log.parent.mkdir(exist_ok=True)
    log.open("a", encoding="utf-8").write(json.dumps(
        {"ts": agora_iso(), "nro": e["nro"], "tipo": a.tipo, "seed": a.seed},
        ensure_ascii=False) + "\n")


# ---------------- prompt ----------------
def esqueleto_copy(e):
    return (f"# COPY — Cenário {e['nro']:02d} ({e['nome']})\n"
            "plataforma alvo: _(preencher: reels | tiktok | story | feed | linkedin)_\n"
            "tonalidade: _(tom do usuário, do mapeamento)_\n\n"
            f"## HOOK (3 segundos)\n_(template do cenário: {e['hook']}_)\n\n"
            "## LEGENDA\n_(2-6 linhas; valor/provocação antes do CTA)_\n\n"
            "## CTA\n_(UMA ação só)_\n\n"
            "## HASHTAGS\n_(5-10: 2-3 de alcance + 4-6 de nicho)_\n\n"
            "## FORMATO\nproporção: " + e["aspecto"] +
            " · subtítulos: _(sim/não)_ · título externo: _(se houver)_\n")


def esqueleto_qc(e):
    tpl = (PACOTE / "templates" / "qc.template.md").read_text(encoding="utf-8")
    return tpl.replace("{{NN}}", f"{e['nro']:02d}").replace("{{NOME}}", e["nome"])


def esqueleto_negativo(e):
    extra = e["negativos_extra"]
    return (f"# NEGATIVO — Cenário {e['nro']:02d} ({e['nome']})\n\n"
            f"## Base pessoas (imutável)\n{NEG['base']}\n\n"
            f"## Objetos (imutável)\n{NEG['objetos']}\n\n"
            f"## Luz (imutável)\n{NEG['luz']}\n\n"
            f"## Naturalismo (imutável)\n{NEG['naturalismo']}\n\n"
            f"## Extras do cenário {e['nro']:02d}\n{extra}\n\n"
            "## Adições do job\n_(termos específicos desta entrega — somam, nunca substituem)_\n")


def cmd_prompt(a):
    root = find_root(a.root)
    n = a.nro
    if not (0 <= n <= N_MAX):
        sys.exit(f"--nro deve estar em 0..{N_MAX}; veio {n}")
    e = next(x for x in CAT["enarios"] if x["nro"] == n)
    ipath = root / "_identity" / "identidade.txt"
    if ipath.exists():
        ident = ipath.read_text(encoding="utf-8").strip()
        aviso = "" if "[BLOCO CONGELADO" not in ident else "\n[aviso: identidade ainda é template — rode a fase 1]"
    else:
        ident = "(identidade.txt ausente — rode a fase 1)"
        aviso = "\n[aviso: identidade ausente]"
    objs = e.get("objetos", [])
    obj_lines = "\n".join(f"- {o}" for o in objs) if objs else "- nenhum objeto crítico neste cenário (somente pessoa+fundo)"
    nat_mod = NAT.get("modificador", "")
    nat_regra = NAT.get("regra", "")
    nat_pele = NAT.get("pele", "")
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%MZ")
    job = a.slug or f"{stamp}-{n:02d}-{slugify(a.acao or e['nome'])}"
    job = slugify(job)
    jdir = root / "drafts" / job
    jdir.mkdir(parents=True, exist_ok=True)
    k = max(1, min(a.variacoes, 8))
    prompt = f"""# PROMPT — Cenário {n:02d} ({e['nome']})

## IDENTIDADE (congelada — nunca alterar neste bloco)
{ident}{aviso}

## CENÁRIO {n:02d} — {e['nome']}
{e['prompt']}

## LUZ
{e['luz']}
_(agente 03 pode ajustar ângulo/intensidade por ocasião; espectro do cenário se mantém)_

## LUMINOSIDADE (obrigatório — sem número, é chute)
{e.get('luminosidade', 'ver catalogo.json')}
Regra: 1 temperatura dominante (+1 acento SÓ se há prático visível justificando).
Destaques nunca estourados; sombras nunca apagadas.

## OBJETOS-CRÍTICOS (deem geometricamente perfeitos)
{obj_lines}
Descreva cada parte listada acima no prompt final — objeto sem anatomia derrete.

## AÇÃO / CONTEÚDO
{a.acao or e['acao_padrao']}

## FORMATO
proporção: {e['aspecto']} · câmera: {e['camera']}

## NATURALISMO (regra 95/5 — anti-olhar-IA)
{nat_mod}
{nat_regra}
{nat_pele}
A imperfeição que vende ESTE cenário: {e.get('realismo', '')}

## VARIAÇÕES ({k})
Gerar {k} variação(ões) mudando SOMENTE: composição, roupa, adereço/prop, expressão leve.
CONGELADO em todas: rosto, tom de pele, textura da pele, cabelo, silhueta.
Objeto trocado em variação precisa ANATOMIA IGUAL ao original (regra dos objetos-críticos).
V1: _(escrever o que muda)_{''.join(f"\nV{i}: _(escrever o que muda)_" for i in range(2, k + 1))}
"""
    (jdir / "prompt.md").write_text(prompt, encoding="utf-8")
    (jdir / "negativo.md").write_text(esqueleto_negativo(e), encoding="utf-8")
    (jdir / "copy.md").write_text(esqueleto_copy(e), encoding="utf-8")
    (jdir / "qc.md").write_text(esqueleto_qc(e), encoding="utf-8")
    print(f"DRAFT: {jdir}")
    print(f"CENÁRIO: {n:02d} — {e['nome']} · variações: {k} · objetos-críticos: {len(objs)}")
    print("próximo: agente 02 revisa prompt · 03 confere LUZ+LUMINOSIDADE · 04 preenche copy · 05 gera + QC(16)")


# ---------------- qc ----------------
ITENS_QC = ["dedos", "mao", "rost", "olho", "membro", "duplic", "boca",
            "texto", "propor", "fundo", "iluminacao", "pele",
            "objetos criticos", "fisica", "luminos", "naturalismo"]
ÂNCORAS_NEG = [("6 fingers", "base pessoas (dedos)"), ("melted", "base objetos (geometria)")]


def cmd_qc(a):
    d = Path(a.dir).expanduser().resolve()
    errs = []
    for f in ["prompt.md", "negativo.md", "copy.md", "qc.md"]:
        if not (d / f).exists():
            errs.append(f"falta {f}")
    if (d / "negativo.md").exists():
        nt = norm((d / "negativo.md").read_text(encoding="utf-8", errors="replace"))
        for anc, nome in ÂNCORAS_NEG:
            if anc not in nt:
                errs.append(f"negativo sem '{anc}' ({nome})")
    if (d / "copy.md").exists():
        ct = norm((d / "copy.md").read_text(encoding="utf-8", errors="replace"))
        for b in ["hook", "legenda", "cta", "hashtag"]:
            if b not in ct:
                errs.append(f"copy sem bloco {b.upper()}")
    if (d / "qc.md").exists():
        qt = norm((d / "qc.md").read_text(encoding="utf-8", errors="replace"))
        for k in ITENS_QC:
            if k not in qt:
                errs.append(f"checklist sem item '{k}'")
        if not re.search(r"liberado|retrabalho", qt):
            errs.append("veredito ausente (LIBERADO ou RETRABALHO)")
        m = re.search(r"(?:cen[aá]rio)\s+(\d{1,2})", qt)
        if m:
            nv = int(m.group(1))
            if not (0 <= nv <= N_MAX):
                errs.append(f"cenário {nv} fora da faixa 0-{N_MAX}")
    if (d / "prompt.md").exists():
        pt = norm((d / "prompt.md").read_text(encoding="utf-8", errors="replace"))
        for bloco in ["luminosidade", "objetos-criticos", "naturalismo"]:
            if bloco not in pt:
                errs.append(f"prompt sem bloco '{bloco.upper()}' (v1.1)")
    print(f"[clone-lab] qc {d.name}: {len(errs)} problema(s)")
    for e_ in errs:
        print("  ERRO", e_)
    if not errs:
        print("  OK estrutura: 4 arquivos, 16 itens de checklist, veredito, negativo com "
              "base de 4 seções, prompt com LUZ/LUMINOSIDADE/OBJETOS/NATURALISMO.")
        print("  (o julgamento visual dos 16 itens é do agente 05 / humano)")
    sys.exit(1 if errs else 0)


# ---------------- check ----------------
def cmd_check(a):
    cfg = {"last_scenarios": []}
    vistos = set()
    for i in range(a.n):
        e = escolher(cfg, silencioso=True)
        assert 0 <= e["nro"] <= N_MAX
        vistos.add(e["nro"])
    cfg2 = {"last_scenarios": []}
    seq = []
    for i in range(12):
        e = escolher(cfg2, silencioso=True)
        seq.append(e["nro"])
    print(f"[clone-lab] check OK: {a.n}/{a.n} sorteios dentro de 0..{N_MAX}; "
          f"{len(vistos)} números distintos alcançados")
    ok3 = all(not (seq[i] == seq[i + 1] == seq[i + 2]) for i in range(len(seq) - 2))
    print(f"[clone-lab] check anti-repetição: sequência {seq} (sem 3 iguais seguidos: {ok3})")
    sys.exit(0 if ok3 else 1)


def main():
    ap = argparse.ArgumentParser(description="CloneLab CLI")
    ap.add_argument("--root", default=None)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("init", help="cria estrutura e varre o dataset")
    p.add_argument("pasta")
    p.set_defaults(fn=cmd_init)

    p = sub.add_parser("cenario", help="escolhe cenário 0-15 (garantido)")
    p.add_argument("--tipo", default=None, help="PODCAST | POV | NORMAL | ...")
    p.add_argument("--seed", default=None)
    p.set_defaults(fn=cmd_cenario)

    p = sub.add_parser("prompt", help="monta drafts/<job>/ completo")
    p.add_argument("--nro", type=int, required=True)
    p.add_argument("--acao", default=None)
    p.add_argument("--variacoes", type=int, default=1)
    p.add_argument("--slug", default=None)
    p.set_defaults(fn=cmd_prompt)

    p = sub.add_parser("qc", help="valida entrega estrutural (16 itens)")
    p.add_argument("dir")
    p.set_defaults(fn=cmd_qc)

    p = sub.add_parser("check", help="self-teste numérico")
    p.add_argument("-n", type=int, default=100)
    p.set_defaults(fn=cmd_check)

    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
