<template>
    <div class="evault">
      <!-- Reusable Header Navigation -->
      <HeaderNav />
  
      <div class="container">
        <h1>eVault Secure Document Storage</h1>
        
        <!-- File Upload Section -->
        <div class="upload-section">
          <input type="file" @change="onFileChange" />
          <button @click="handleUpload" :disabled="!selectedFile">Upload Document</button>
        </div>
        
        <!-- Message Display -->
        <div v-if="message" class="message">{{ message }}</div>
        
        <!-- Document List (Uploaded Documents) -->
        <div class="document-list" v-if="documents.length">
          <h2>Uploaded Documents</h2>
          <ul>
            <li v-for="(doc, index) in documents" :key="index">
              <strong>Document ID:</strong> {{ doc.id }}<br />
              <strong>CID:</strong> {{ doc.ipfsCID }}<br />
              <strong>File Hash:</strong> {{ doc.fileHash }}<br />
              <strong>Uploader:</strong> {{ doc.uploader }}<br />
              <strong>Timestamp:</strong> {{ doc.timestamp }}
            </li>
          </ul>
        </div>
        
        <!-- Extra Blockchain Diagnostics (Gimmick Section) -->
        <div class="gimmick-section">
          <h2>Blockchain Diagnostics</h2>
          <p>Latest Transaction Hash: <span>{{ latestTxHash }}</span></p>
          <p>Network Status: <span>{{ networkStatus }}</span></p>
          <!-- You can add more technical details as needed -->
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import HeaderNav from '@/components/HeaderNav.vue'
  import { uploadDocument } from '@/blockchain.js'
  
  export default {
    name: 'EvaultPage',
    components: {
      HeaderNav
    },
    data() {
      return {
        selectedFile: null,
        message: '',
        documents: [],
        latestTxHash: '',
        networkStatus: 'Connected' // Gimmick: show a dummy network status
      }
    },
    methods: {
      onFileChange(e) {
        this.selectedFile = e.target.files[0]
      },
      async handleUpload() {
        if (!this.selectedFile) return
  
        try {
          this.message = "Uploading document to IPFS & recording on blockchain..."
          // Call the blockchain.js function that handles IPFS upload and on-chain recording.
          const result = await uploadDocument(this.selectedFile)
          this.latestTxHash = result.txHash
          this.message = "Upload successful! Transaction: " + result.txHash
          
          // For demo purposes, add document details into a local list.
          this.documents.push({
            id: this.documents.length,
            ipfsCID: result.ipfsCID,
            fileHash: result.fileHash,
            uploader: "0xd9145CCE52D386f254917e481eB44e9943F39138", // Replace with actual address if available.
            timestamp: new Date().toLocaleString()
          })
        } catch (error) {
          console.error(error)
          this.message = "Upload failed: " + error.message + " IPFS Failed to Connect at the Moment. Please try again later."
        }
      }
    }
  }
  </script>
  
  <style scoped>
  .evault {
    background-color: #222;
    color: gold;
    min-height: 100vh;
  }
  
  .container {
    width: 80%;
    margin: 0 auto;
    padding: 20px;
  }
  
  h1, h2 {
    margin-bottom: 20px;
  }
  
  .upload-section {
    display: flex;
    gap: 10px;
    align-items: center;
    margin-bottom: 20px;
  }
  
  .upload-section input[type="file"] {
    background-color: #333;
    color: gold;
    border: 1px solid gold;
    padding: 8px;
    border-radius: 4px;
  }
  
  .upload-section button {
    background-color: gold;
    color: #222;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
    border-radius: 4px;
  }
  
  .upload-section button:disabled {
    background-color: #555;
    cursor: not-allowed;
  }
  
  .message {
    margin-bottom: 20px;
    font-size: 1.1em;
  }
  
  .document-list ul {
    list-style: none;
    padding: 0;
  }
  
  .document-list li {
    background-color: #333;
    padding: 15px;
    margin-bottom: 10px;
    border-radius: 4px;
    text-align: left;
  }
  
  .gimmick-section {
    margin-top: 40px;
    padding: 20px;
    background-color: #333;
    border: 1px solid gold;
    border-radius: 4px;
  }
  </style>