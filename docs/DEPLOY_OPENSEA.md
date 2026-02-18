# Deploy Math Formula NFTs on OpenSea

Two paths: **OpenSea Studio** (no code, no contract) or **your own contract + IPFS** (full control, batch minting).

---

## Path A: OpenSea Studio (simplest)

Best if you want to mint from your wallet without writing smart contracts.

1. **Generate assets**
   - Run: `python scripts/batch_build.py`
   - You get `build/images/` (1.png, 2.png, …) and `build/metadata/` (1.json, 2.json, …).

2. **Create collection**
   - Go to [OpenSea Studio](https://opensea.io/studio).
   - Connect your wallet (MetaMask, etc.).
   - Create a new collection (name, description, image, chain e.g. Polygon).

3. **Add items**
   - For each token you want to mint:
     - Upload the image (e.g. `build/images/1.png`).
     - Name and description can be taken from `build/metadata/1.json` (copy-paste).
     - Add attributes if the UI supports it (Category, Difficulty, Subject from the JSON).
   - Mint into your wallet (you pay gas once per mint on the chain you chose).

4. **Selling**
   - List your NFTs on OpenSea from your profile.

**Limitation:** OpenSea Studio doesn’t support bulk upload of hundreds of files in one click. For large batches you may need to use a CSV/API if available, or consider Path B.

---

## Path B: Smart contract + IPFS (batch minting)

Best if you want to mint many tokens in one go and have a single collection contract.

### 1. Host images and metadata

- **Option A — Pinata (IPFS)**
  1. Sign up at [Pinata](https://pinata.cloud).
  2. Upload the `build/images` folder → get a CID (e.g. `QmImages...`).
  3. Upload the `build/metadata` folder → get a CID (e.g. `QmMeta...`).
  4. Base URLs:
     - Images: `https://gateway.pinata.cloud/ipfs/QmImages.../`
     - Metadata: `https://gateway.pinata.cloud/ipfs/QmMeta.../`
  5. In `config.json`, set `image_base_url` and `metadata_base_url` to these URLs (with trailing slash), then re-run `python scripts/generate_metadata.py` so each `tokenURI` points to the right image URL inside the metadata.

- **Option B — NFT.Storage**
  - Upload images and metadata to [NFT.Storage](https://nft.storage); use the returned IPFS URLs the same way in `config.json` and metadata.

After re-generating metadata, each `build/metadata/{id}.json` should have an `image` field like `https://gateway.pinata.cloud/ipfs/QmImages.../1.png`.

### 2. Deploy ERC-721 contract

- Use a template (e.g. OpenZeppelin ERC721 + base URI pointing to your metadata base).
- Set base URI so `tokenURI(tokenId)` returns `https://gateway.pinata.cloud/ipfs/QmMeta.../` + `tokenId` + `.json` (or your actual pattern).
- Deploy on a chain OpenSea supports (Ethereum, Polygon, etc.).

### 3. Mint tokens

- Call `mint(to, tokenId)` for each token (or a batch mint if your contract has it).
- OpenSea will read metadata from `tokenURI(tokenId)` and show name, description, image, and attributes.

### 4. Verify on OpenSea

- Open your contract on OpenSea (e.g. `https://opensea.io/assets/CHAIN/CONTRACT_ADDRESS/TOKEN_ID`).
- If something is wrong, use [OpenSea’s refresh metadata](https://docs.opensea.io/reference/refresh_nft) or fix metadata and re-upload to IPFS, then refresh.

---

## Checklist to avoid common issues

- [ ] **Image size:** OpenSea recommends at least 3000×3000 px. Our generator uses this by default in `config.json`.
- [ ] **Metadata JSON:** Must include `name`, `description`, `image` (full URL after you host). Optional: `attributes`, `external_url`, `background_color` (6 hex chars, no `#`).
- [ ] **CORS:** If you host metadata on your own server, allow CORS so OpenSea can fetch it.
- [ ] **IPFS:** After uploading, use the same gateway (e.g. Pinata) in both your metadata `image` URLs and your contract’s base URI so OpenSea can resolve them.

---

## After deployment

- Share your collection link (e.g. `https://opensea.io/collection/your-collection-slug`).
- Update `config.json` → `external_url` with that link and re-run metadata generation if you use it in token metadata.
