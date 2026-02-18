# Configuração (config.json) — em português

O arquivo **config.json** controla o nome da coleção, as descrições, o tamanho das imagens e as URLs usadas nos metadados. Abaixo, o que cada campo significa.

---

## Campos principais

| Campo | Em português | O que é |
|-------|----------------|--------|
| **collection_name** | Nome da coleção | Nome que aparece na OpenSea para a sua coleção (ex.: "Math Formula NFT"). |
| **collection_description** | Descrição da coleção | Texto que descreve a coleção na página da OpenSea. |
| **external_url** | Link externo | Link para a sua coleção na OpenSea (ex.: `https://opensea.io/collection/seu-slug`). Depois de criar a coleção, troque `your-collection-slug` pelo slug real. |

---

## Imagem (image)

| Campo | Em português | O que é |
|-------|----------------|--------|
| **width** | Largura | Largura da imagem em pixels (a OpenSea recomenda pelo menos 3000). |
| **height** | Altura | Altura da imagem em pixels (ex.: 3000 para quadrado). |
| **dpi** | DPI | Resolução usada ao gerar o PNG (ex.: 150). |
| **background_color** | Cor de fundo | Cor de fundo em hexadecimal **sem** o `#` (ex.: `ffffff` = branco). |

---

## URLs base (para quando subir no IPFS/servidor)

| Campo | Em português | O que é |
|-------|----------------|--------|
| **metadata_base_url** | URL base dos metadados | URL da pasta onde estão os JSON dos metadados (ex.: depois de subir no Pinata, algo como `https://gateway.pinata.cloud/ipfs/QmMeta.../`). Cada token terá algo como `{metadata_base_url}1.json`, `{metadata_base_url}2.json`, etc. |
| **image_base_url** | URL base das imagens | URL da pasta onde estão as imagens (ex.: `https://gateway.pinata.cloud/ipfs/QmImages.../`). Nos metadados, a imagem do token 1 será `{image_base_url}1.png`. |

**Quando usar:** Deixe os placeholders (`https://your-ipfs-or-domain.com/...`) enquanto só estiver gerando arquivos localmente. Depois de subir as pastas `build/images` e `build/metadata` no IPFS (ou outro servidor), coloque aqui as URLs reais **com barra no final** e rode de novo `python scripts/generate_metadata.py` para que os JSON apontem para as imagens e links corretos.

---

## Exemplo resumido

- **Só gerar no PC:** pode deixar `metadata_base_url` e `image_base_url` como estão; as imagens e JSON serão gerados em `build/`.
- **Depois de subir no IPFS (ex.: Pinata):**  
  - Coloque em **image_base_url** a URL da pasta das imagens (com `/` no final).  
  - Coloque em **metadata_base_url** a URL da pasta dos metadados (com `/` no final).  
  - Rode `python scripts/generate_metadata.py` de novo.  
  - Use a **metadata_base_url** como base URI no seu contrato (para que `tokenURI(1)` seja `{metadata_base_url}1.json`).

Se quiser, você pode manter o resto do projeto em inglês e usar este arquivo só para consultar o significado dos campos do **config.json** em português.
