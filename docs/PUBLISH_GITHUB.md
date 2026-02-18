# Publicar o projeto no GitHub (portfólio)

Passos para colocar o **Math Formula NFT** no GitHub como repositório público e usar no portfólio.

---

## 1. Criar o repositório no GitHub

1. Acesse [github.com](https://github.com) e faça login.
2. Clique em **New repository** (ou **+** → **New repository**).
3. Preencha:
   - **Repository name:** `math-formula-nft` (ou outro nome, ex.: `math-nft-opensea`)
   - **Description:** ex. *NFT collection of 1000+ math/physics/statistics formulas — batch image generation & OpenSea-ready metadata*
   - **Public**
   - **Não** marque "Add a README" (você já tem um).
4. Clique em **Create repository**.

---

## 2. Inicializar Git e fazer o primeiro push (no seu PC)

No terminal, na pasta do projeto:

```powershell
cd "c:\Users\dopamine\Desktop\Projetos\Math NFT"

# Inicializar repositório (se ainda não for um repo git)
git init

# Adicionar remote (troque YOUR_USERNAME e REPO_NAME pelo seu usuário e nome do repo)
git remote add origin https://github.com/YOUR_USERNAME/math-formula-nft.git

# Adicionar todos os arquivos (build/ e venv/ já estão no .gitignore)
git add .
git status   # confira o que será commitado

# Primeiro commit
git commit -m "Initial commit: Math Formula NFT — 1000+ formulas, image & metadata pipeline, OpenSea-ready"

# Enviar para o GitHub (branch main)
git branch -M main
git push -u origin main
```

Se o GitHub pedir autenticação, use **Personal Access Token** ou **GitHub CLI** conforme a documentação do GitHub.

---

## 3. O que vai (e não vai) para o GitHub

- **Vai:** código-fonte, `formulas/`, `scripts/`, `config.json`, `README.md`, `LICENSE`, `docs/`, `requirements.txt`, `.gitignore`.
- **Não vai (por causa do .gitignore):** pasta `build/` (imagens e metadados gerados), `venv/`, `__pycache__/`, `.env`.

Assim o repositório fica leve e profissional. Quem clonar pode rodar `csv_to_json.py` e `batch_build.py` para gerar as imagens localmente.

---

## 4. Deixar o README ainda mais profissional

- No GitHub, edite o **About** do repositório (engrenagem ao lado de "About"): coloque **description** e **topics**, ex.: `nft`, `opensea`, `python`, `matplotlib`, `formulas`, `blockchain`.
- O **README.md** já está preparado com badges, estrutura e links para OpenSea e documentação em PT.

---

## 5. Link no portfólio

Use o link do repositório no seu portfólio, por exemplo:

- **GitHub:** `https://github.com/YOUR_USERNAME/math-formula-nft`
- **Descrição sugerida:** *Pipeline para criar e publicar NFTs de fórmulas matemáticas na OpenSea: banco de 1000+ fórmulas (matemática, física, estatística), geração em lote de imagens e metadados no padrão OpenSea.*

Depois de publicar na OpenSea, você pode adicionar também o link da coleção no README (em `config.json` → `external_url` e na descrição do projeto).
