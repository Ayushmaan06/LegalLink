import { ethers } from 'ethers';
import documentVaultABI from './abi/DocumentVaultABI.json';
import { create as ipfsCreate } from 'ipfs-http-client';
import CryptoJS from 'crypto-js';
import { Buffer } from 'buffer';
const contractAddress = "0xd9145CCE52D386f254917e481eB44e9943F39138";

// Initialize IPFS client (using Infura's IPFS API endpoint as an example)
const ipfs = ipfsCreate({ url: 'https://ipfs.infura.io:5001/api/v0' });

/**
 * Returns a contract instance connected via MetaMask.
 */
export async function getContract() {
  if (window.ethereum) {
    // Request account access if needed
    await window.ethereum.request({ method: 'eth_requestAccounts' });
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    const signer = provider.getSigner();
    return new ethers.Contract(contractAddress, documentVaultABI, signer);
  }
  throw new Error("MetaMask not installed");
}

/**
 * Uploads a file to IPFS and records its metadata on the blockchain.
 * @param {File} file - The file object from an <input type="file"> element.
 * @returns {Object} - Contains ipfsCID, fileHash, and the transaction hash.
 */
export async function uploadDocument(file) {
  // Read file into an ArrayBuffer
  const buffer = await file.arrayBuffer();

  // Upload file to IPFS
  const result = await ipfs.add(Buffer.from(buffer));
  const ipfsCID = result.path;

  // Compute SHA256 hash using crypto-js
  const wordArray = CryptoJS.lib.WordArray.create(buffer);
  const fileHash = CryptoJS.SHA256(wordArray).toString();

  // Get the contract instance and call addDocument on-chain
  const contract = await getContract();
  const tx = await contract.addDocument(ipfsCID, fileHash);
  await tx.wait();

  return { ipfsCID, fileHash, txHash: tx.hash };
}

/**
 * Retrieves a Document from the blockchain by its document ID.
 * @param {number} docId - The document ID.
 * @returns {Object} - The document struct as returned by the contract.
 */
export async function getDocument(docId) {
  const contract = await getContract();
  const document = await contract.getDocument(docId);
  return document;
}