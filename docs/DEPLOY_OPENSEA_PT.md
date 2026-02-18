# Publicar os NFTs de Fórmulas na OpenSea (passo a passo em português)

Há dois caminhos: **OpenSea Studio** (sem código, sem contrato) ou **seu próprio contrato + IPFS** (controle total e cunhagem em lote).

---

## Caminho A: OpenSea Studio (mais simples)

Melhor se você quer cunhar direto da sua carteira, sem escrever contratos.

### Passo 1 — Gerar os arquivos

1. No terminal, na pasta do projeto, com o venv ativado:
   ```powershell
   python scripts/batch_build.py
   ```
2. Você terá as pastas:
   - **build/images/** — 1.png, 2.png, 3.png, …
   - **build/metadata/** — 1.json, 2.json, 3.json, …

### Passo 2 — Criar a coleção

1. Acesse o [OpenSea Studio](https://opensea.io/studio).
2. Conecte sua carteira (MetaMask, etc.).
3. Crie uma nova coleção: escolha nome, descrição, imagem da coleção e a blockchain (ex.: Polygon).

### Passo 3 — Adicionar os itens (NFTs)

Para cada token que quiser cunhar:

1. Envie a imagem (ex.: `build/images/1.png`).
2. Nome e descrição: você pode copiar do arquivo correspondente em `build/metadata/` (ex.: abra `1.json` e copie o que está em `"name"` e `"description"`).
3. Se a interface permitir, adicione os atributos (Category, Difficulty, Subject) que estão dentro de `"attributes"` no mesmo JSON.
4. Cunhe o NFT na sua carteira (você paga a taxa de rede “gas” uma vez por NFT na blockchain escolhida).

### Passo 4 — Vender

- Na sua página de perfil na OpenSea, liste os NFTs que quiser à venda.

**Limitação:** O OpenSea Studio não faz upload em massa de centenas de arquivos de uma vez. Para muitos itens, pode ser preciso usar planilha/API se existir, ou usar o Caminho B (contrato + IPFS).

---

## Caminho B: Contrato inteligente + IPFS (cunhagem em lote)

Melhor se você quer cunhar muitos tokens de uma vez e ter um único contrato da coleção.

### Passo 1 — Hospedar imagens e metadados

**Opção A — Pinata (IPFS)**

1. Crie uma conta em [Pinata](https://pinata.cloud).
2. Envie a pasta **build/images** → anote o CID (ex.: `QmImages...`).
3. Envie a pasta **build/metadata** → anote o CID (ex.: `QmMeta...`).
4. Monte as URLs base (com barra no final):
   - Imagens: `https://gateway.pinata.cloud/ipfs/QmImages.../`
   - Metadados: `https://gateway.pinata.cloud/ipfs/QmMeta.../`
5. No **config.json**, preencha:
   - **image_base_url** com a URL das imagens.
   - **metadata_base_url** com a URL dos metadados.
6. Rode de novo: `python scripts/generate_metadata.py`  
   Assim, cada JSON em `build/metadata/` passará a ter o campo `"image"` com a URL correta (ex.: `https://gateway.pinata.cloud/ipfs/QmImages.../1.png`).

**Opção B — NFT.Storage**

- Envie imagens e metadados em [NFT.Storage](https://nft.storage) e use as URLs IPFS retornadas do mesmo jeito no **config.json** e nos metadados.

Depois de regerar os metadados, cada `build/metadata/{id}.json` deve ter o campo `image` com a URL completa da imagem.

### Passo 2 — Implantar o contrato ERC-721

- Use um modelo (ex.: OpenZeppelin ERC721) com a base URI apontando para a URL base dos metadados.
- Ajuste para que `tokenURI(tokenId)` retorne:  
  `https://gateway.pinata.cloud/ipfs/QmMeta.../` + número do token + `.json`
- Implante em uma blockchain suportada pela OpenSea (Ethereum, Polygon, etc.).

### Passo 3 — Cunhar os tokens

- Chame `mint(to, tokenId)` para cada token (ou use uma função de “batch mint” se o contrato tiver).
- A OpenSea lê os metadados via `tokenURI(tokenId)` e exibe nome, descrição, imagem e atributos.

### Passo 4 — Verificar na OpenSea

- Abra seu contrato na OpenSea (ex.: `https://opensea.io/assets/CHAIN/ENDEREÇO_DO_CONTRATO/TOKEN_ID`).
- Se algo aparecer errado, use a opção de “refresh metadata” da OpenSea ou corrija os metadados, suba de novo no IPFS e atualize.

---

## Checklist para evitar problemas

- [ ] **Tamanho da imagem:** OpenSea recomenda pelo menos 3000×3000 px. O gerador já usa isso por padrão no **config.json**.
- [ ] **JSON de metadados:** Deve ter `name`, `description`, `image` (URL completa depois de hospedar). Opcional: `attributes`, `external_url`, `background_color` (6 caracteres hex, sem `#`).
- [ ] **CORS:** Se hospedar metadados no seu próprio servidor, permita CORS para a OpenSea conseguir buscar o JSON.
- [ ] **IPFS:** Use o mesmo gateway (ex.: Pinata) nas URLs de `image` nos metadados e na base URI do contrato.

---

## Depois de publicar

- Compartilhe o link da coleção (ex.: `https://opensea.io/collection/seu-slug`).
- Se quiser, atualize no **config.json** o campo **external_url** com esse link e rode de novo a geração de metadados, para que os próximos tokens já saiam com o link certo.
