# Math Formula NFT — Projeto OpenSea (Português)

Criar e publicar **NFTs de fórmulas matemáticas** (Estatística, Matemática, Física) na OpenSea. Imagens simples com fundo branco, do básico ao avançado, com **geração em massa** e **metadados no padrão OpenSea**.

---

## O que este projeto faz

1. **Gera imagens das fórmulas** — **Nome da fórmula em cima**, fórmula embaixo; fundo branco (não precisa instalar LaTeX por padrão).
2. **Gera metadados para a OpenSea** — Nome, descrição, URL da imagem, atributos (categoria, dificuldade, assunto).
3. **Banco de fórmulas** — O arquivo `formulas/database/formulas.csv` reúne **mais de 1000 fórmulas** (matemática, física, estatística), do nível básico ao doutorado; em `formulas/database/SOURCES.md` estão as fontes. Use `python scripts/csv_to_json.py` para exportar para JSON e depois `python scripts/batch_build.py` para gerar as imagens.
4. **Pipeline em lote** — Gerar centenas de fórmulas em uma só execução.
5. **Publicar na OpenSea** — Usar o OpenSea Studio (sem código) ou seu próprio contrato + IPFS.

---

## Estrutura do projeto

```
Math NFT/
├── README.md                 # Este arquivo (inglês)
├── README_PT.md              # Este guia em português
├── requirements.txt         # Dependências Python
├── config.json               # Nome da coleção, descrição, URLs base — veja CONFIG_PT.md
├── formulas/
│   ├── data/                  # JSON usado na geração de imagens
│   │   ├── math.json
│   │   ├── physics.json
│   │   └── statistics.json
│   ├── database/
│   │   ├── formulas.csv      # Banco de fórmulas (muitas entradas)
│   │   └── SOURCES.md        # Fontes: GitHub, referências
│   └── schema.md             # Como adicionar mais fórmulas
├── scripts/
│   ├── generate_images.py    # Fórmula → PNG (fundo branco)
│   ├── generate_metadata.py # Gera JSON OpenSea por token
│   ├── batch_build.py        # Roda todo o pipeline
│   └── csv_to_json.py        # Converte formulas.csv → data/*.json
├── build/                    # Saída gerada (gitignored)
│   ├── images/               # 1.png, 2.png, ...
│   └── metadata/             # 1.json, 2.json, ...
└── docs/
    ├── DEPLOY_OPENSEA.md     # Passo a passo em inglês
    ├── DEPLOY_OPENSEA_PT.md # Passo a passo em português
    └── CONFIG_PT.md          # Explicação do config.json em português
```

---

## Início rápido (passo a passo)

### 1. Configuração inicial

1. Abra o terminal na pasta do projeto.
2. Crie e ative o ambiente virtual e instale as dependências:

```powershell
cd "c:\Users\dopamine\Desktop\Projetos\Math NFT"
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

*(No Mac/Linux use: `source venv/bin/activate`.)*

### 2. Gerar todas as imagens e metadados

No mesmo terminal (com o venv ativado):

```powershell
python scripts/batch_build.py
```

Isso preenche `build/images/` e `build/metadata/` com os arquivos prontos para a OpenSea.

### 3. Publicar na OpenSea

- **Caminho mais fácil:** Use o [OpenSea Studio](https://opensea.io/studio) → Criar coleção → Enviar imagens e preencher nome/descrição (pode copiar dos arquivos em `build/metadata/`).
- **Controle total:** Enviar `build/images` e `build/metadata` para o IPFS (ex.: Pinata), implantar um contrato ERC-721 e cunhar os tokens com as URIs apontando para seus metadados.

Passo a passo detalhado em português: **[docs/DEPLOY_OPENSEA_PT.md](docs/DEPLOY_OPENSEA_PT.md)**.

**Publicar no GitHub (portfólio):** [docs/PUBLISH_GITHUB.md](docs/PUBLISH_GITHUB.md)

---

## Configuração (config.json)

O arquivo **config.json** controla o nome da coleção, a descrição, o tamanho das imagens e as URLs base. Cada campo está explicado em português em: **[docs/CONFIG_PT.md](docs/CONFIG_PT.md)**.

---

## Adicionar mais fórmulas

Edite os JSON em `formulas/data/`:

- **math.json** — Álgebra, cálculo, teoria dos números, etc.
- **physics.json** — Mecânica, eletromagnetismo, termodinâmica, etc.
- **statistics.json** — Distribuições, regressão, testes, etc.

Cada fórmula tem: `name`, `formula` (em mathtext, ex.: `$E = mc^2$`), `description`, `category`, `difficulty` (1–5). O formato exato está em **formulas/schema.md**.

Depois de editar, rode de novo: `python scripts/batch_build.py`.

---

## Reduzir problemas técnicos

- **Sem LaTeX obrigatório** — As imagens usam mathtext do matplotlib (frações, somatórias, integrais, letras gregas). Para LaTeX pesado dá para instalar LaTeX e usar o renderizador "latex" no config.
- **Nomes de arquivo consistentes** — Os tokens são numerados 1, 2, 3… para imagens e metadados ficarem sincronizados.
- **Metadados no padrão OpenSea** — O JSON segue o padrão (name, description, image, attributes).
- **Config em um só lugar** — O `config.json` concentra nome da coleção, descrição, tamanho da imagem e URL base.

---

## Licença

Use e modifique como quiser. Ao publicar na OpenSea, use apenas conteúdo que você tenha direito (fórmulas de livro didático em geral são ok; cite a fonte se necessário).
