<template>
  <div class="upload-section">
    <div class="folder">
      <div class="front-side">
        <div class="tip"></div>
        <div class="cover"></div>
      </div>
      <div class="back-side cover"></div>
    </div>

    <label class="custom-file-upload">
      <input class="title" type="file" @change="onFileChange" />
      Choose a file
    </label>

    <div v-if="selectedFile" class="filename">
      {{ selectedFile.name }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'FancyUpload',
  data() {
    return {
      selectedFile: null
    };
  },
  methods: {
    onFileChange(e) {
      this.selectedFile = e.target.files[0];
      this.$emit('file-selected', this.selectedFile);
    },
  }
};
</script>

<style scoped>
.upload-section {
  --transition: 350ms;
  --folder-W: 160px;
  --folder-H: 80px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-end;
  padding: 15px;
  background: linear-gradient(135deg, #000000, #1c1c1c);
  border-radius: 15px;
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.4);
  height: calc(var(--folder-H) * 1.7);
  width: calc(var(--folder-W) + 40px);
  position: relative;
  box-sizing: border-box;
  margin: auto;
}

.folder {
  position: absolute;
  top: -20px;
  left: calc(50% - 80px);
  animation: float 2.5s infinite ease-in-out;
  transition: transform var(--transition) ease;
}

.folder:hover {
  transform: scale(1.05);
}

.folder .front-side,
.folder .back-side {
  position: absolute;
  transition: transform var(--transition);
  transform-origin: bottom center;
}

.folder .back-side::before,
.folder .back-side::after {
  content: "";
  display: block;
  background-color: white;
  opacity: 0.5;
  width: var(--folder-W);
  height: var(--folder-H);
  position: absolute;
  transform-origin: bottom center;
  border-radius: 15px;
  transition: transform 350ms;
  z-index: 0;
}

.upload-section:hover .back-side::before {
  transform: rotateX(-5deg) skewX(5deg);
}

.upload-section:hover .back-side::after {
  transform: rotateX(-15deg) skewX(12deg);
}

.folder .front-side {
  z-index: 1;
}

.upload-section:hover .front-side {
  transform: rotateX(-40deg) skewX(15deg);
}

.folder .tip {
  background: linear-gradient(135deg, #ff9a56, #ff6f56);
  width: 80px;
  height: 20px;
  border-radius: 12px 12px 0 0;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
  position: absolute;
  top: -10px;
  z-index: 2;
}

.folder .cover {
  background: linear-gradient(135deg, #ffe563, #ffc663);
  width: var(--folder-W);
  height: var(--folder-H);
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.3);
  border-radius: 10px;
}

.custom-file-upload {
  font-size: 1em;
  color: #ffffff;
  text-align: center;
  background: rgba(255, 255, 255, 0.15);
  border: none;
  border-radius: 10px;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
  cursor: pointer;
  transition: background var(--transition) ease, box-shadow 0.3s ease-in-out;
  display: inline-block;
  width: 100%;
  padding: 10px 35px;
  margin-top: 5px;
  box-sizing: border-box;
}

.custom-file-upload:hover {
  background: rgba(255, 255, 255, 0.3);
  box-shadow: 0 0 15px 5px rgba(255, 204, 0, 0.8);
}

.custom-file-upload input[type="file"] {
  display: none;
}

.filename {
  font-size: 0.8em;
  color: #e0e0e0;
  margin-top: 5px;
  text-align: center;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

@keyframes float {
  0% {
    transform: translateY(0px);
  }

  50% {
    transform: translateY(-20px);
  }

  100% {
    transform: translateY(0px);
  }
}
</style>
