<template>
  <div class="evault">
    <!-- Reusable Header Navigation -->
    <HeaderNav />

    <!-- LegalSafe Heading -->
    <div class="legalsafe-container">
      <LegalSafe />
    </div>

    <div class="container">
      <!-- Upload Section Wrapper -->
      <div class="upload-wrapper">
        <!-- Left: Fancy Upload -->
        <div class="fancy-upload-container">
          <FancyUpload
            @document-uploaded="handleDocumentUploaded"
            @update-status="handleStatusUpdate"
          />
          <!-- Upload Document and Choose File Button -->
          <div class="upload-action-container">
            <div
              aria-label="Upload Document Button"
              tabindex="0"
              role="button"
              class="user-profile"
              @focus="handleFocus"
              @blur="handleBlur"
              @click="handleUpload"
            >
              <div class="user-profile-inner">
                <p>Upload Document</p>
              </div>
            </div>
          
            <!-- Conditional Message Under Upload Button -->
            <p v-if="message && !selectedFile" class="error-message">{{ message }}</p>
          </div>
        </div>

        <!-- Right: Blockchain Info Cards -->
        <div class="blockchain-card-group">
          <div class="blockchain-card-container">
            <BlockchainCard />
          </div>
          <div class="blockchain-card-container">
            <BlockchainCard1 />
          </div>
          <div class="blockchain-card-container">
            <BlockchainCard2 />
          </div>
          <div class="blockchain-card-container">
            <BlockchainCard3 />
          </div>
        </div>
      </div>

      <!-- Message Display -->
      <div v-if="message" class="message">{{ message }}</div>

      <!-- Document List -->
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

      <!-- Bottom BlockCard -->
      <div class="bottom-blockcard-container">
        <BlockCard />
      </div>
    </div>
  </div>
</template>

<script>
import HeaderNav from '@/components/HeaderNav.vue'
import LegalSafe from '@/components/LegalSafe.vue'
import FancyUpload from '@/components/FancyUpload.vue'
import BlockchainCard from '@/components/BlockchainCard.vue'
import BlockchainCard1 from '@/components/BlockchainCard1.vue'
import BlockchainCard2 from '@/components/BlockchainCard2.vue'
import BlockchainCard3 from '@/components/BlockchainCard3.vue'
import BlockCard from '@/components/BlockCard.vue' // <-- New Import
import { uploadDocument } from '@/blockchain.js'

export default {
  name: 'EvaultPage',
  components: {
    HeaderNav,
    LegalSafe,
    FancyUpload,
    BlockchainCard,
    BlockchainCard1,
    BlockchainCard2,
    BlockchainCard3,
    BlockCard // <-- New Component Registered
  },
  data() {
    return {
      selectedFile: null,
      documents: [],
      message: '',
      latestTxHash: '',
      networkStatus: 'Connected'
    }
  },
  methods: {
    handleDocumentUploaded(newDoc) {
      this.documents.push({
        ...newDoc,
        id: this.documents.length,
        timestamp: new Date().toLocaleString(),
        uploader: "0xd9145CCE52D386f254917e481eB44e9943F39138"
      })
    },
    handleStatusUpdate(newMessage, txHash = '') {
      this.message = newMessage
      if (txHash) this.latestTxHash = txHash
    },
    async handleUpload() {
      if (!this.selectedFile) {
        this.message = ""
        return
      }

      try {
        this.message = "Uploading document to IPFS & recording on blockchain..."
        const result = await uploadDocument(this.selectedFile)
        this.latestTxHash = result.txHash
        this.message = "Upload successful! Transaction: " + result.txHash

        this.documents.push({
          id: this.documents.length,
          ipfsCID: result.ipfsCID,
          fileHash: result.fileHash,
          uploader: "0xd9145CCE52D386f254917e481eB44e9943F39138",
          timestamp: new Date().toLocaleString()
        })
      } catch (error) {
        console.error(error)
        this.message = "Upload failed: " + error.message + " IPFS Failed to Connect at the Moment. Please try again later."
      }
    },
    handleFocus(event) {
      event.target.classList.add('focused')
    },
    handleBlur(event) {
      event.target.classList.remove('focused')
    },
    handleFileChange(event) {
      this.selectedFile = event.target.files[0]
    }
  }
}
</script>

<style scoped>
.evault {
  background-image: url('@/assets/backg.webp');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  color: gold;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.legalsafe-container {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 40px 20px 40px;
  text-align: center;
  width: 85%;
  max-width: 600px;
  margin: 0 auto;
  overflow: hidden;
}

.container {
  width: 80%;
  margin: 0 auto;
  padding: 20px;
}

h1, h2 {
  margin-bottom: 20px;
}

.upload-wrapper {
  display: flex;
  flex-wrap: wrap;
  gap: 30px;
  align-items: flex-start;
  margin-bottom: 20px;
}

.fancy-upload-container {
  max-width: 400px;
  flex: 1;
}

.upload-action-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-top: 20px;
}

.blockchain-card-group {
  display: flex;
  gap: 10px; /* Reduced gap */
  justify-content: flex-start; /* Align items to the left */
}

.blockchain-card-container {
  flex: 1;
  max-width: 220px;
  min-width: 180px;
  margin-bottom: 20px;
}

.user-profile {
  width: 180px;
  height: 51px;
  border-radius: 15px;
  cursor: pointer;
  transition: 0.3s ease;
  background: linear-gradient(to bottom right, #fcdc34 0%, rgba(252, 220, 52, 0) 30%);
  background-color: rgba(252, 220, 52, 0.2);
  display: flex;
  align-items: center;
  justify-content: center;
}

.user-profile.focused,
.user-profile:hover,
.user-profile:focus {
  background-color: rgba(252, 220, 52, 0.7);
  box-shadow: 0 0 10px rgba(252, 220, 52, 0.5);
  outline: none;
}

.user-profile-inner {
  width: 100%;
  height: 47px;
  border-radius: 13px;
  background-color: #1a1a1a;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  font-weight: 600;
}

.error-message {
  color: red;
  font-size: 0.9em;
  margin-top: 10px;
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

.bottom-blockcard-container {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 60px;
  margin-bottom: 40px;
}

/* Responsive Adjustments */
@media (max-width: 1200px) {
  .blockchain-card-group {
    gap: 20px;
  }

  .blockchain-card-container {
    max-width: 200px;
  }
}

@media (max-width: 768px) {
  .blockchain-card-group {
    gap: 15px;
  }

  .blockchain-card-container {
    max-width: 100%;
    flex: 1;
  }
}

@media (max-width: 480px) {
  .blockchain-card-container {
    max-width: 100%;
  }
}
</style>
