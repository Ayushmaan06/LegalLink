<template>
    <div class="card">
      <div class="first-content">
        <span>OCR & Search</span>
      </div>
      <div class="second-content">
        <span>Easy document search with Optical Character Recognition (OCR).</span>
      </div>
    </div>
  </template>
  
  <style scoped>
  .card {
    width: 150px;
    height: 224px;
    background: rgba(0, 0, 0, 1);
    transition: all 0.4s;
    border-radius: 10px;
    box-shadow: 0px 0px 10px 5px rgba(255, 211, 29, 0.8);
    font-size: 30px;
    font-weight: 900;
  }
  
  .card:hover {
    border-radius: 15px;
    cursor: pointer;
    transform: scale(1.2);
    box-shadow: 0px 0px 10px 5px rgba(255, 211, 29, 0.8);
    background: rgba(32, 32, 32, 1);
  }
  
  .first-content {
    height: 100%;
    width: 100%;
    transition: all 0.4s;
    display: flex;
    justify-content: center;
    align-items: center;
    opacity: 1;
    border-radius: 15px;
  }
  
  .card:hover .first-content {
    height: 0px;
    opacity: 0;
  }
  
  .second-content {
    height: 0%;
    width: 100%;
    opacity: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 15px;
    transition: all 0.4s;
    font-size: 0px;
    transform: rotate(90deg) scale(-1);
  }
  
  .card:hover .second-content {
    opacity: 1;
    height: 100%;
    font-size: 1.8rem;
    transform: rotate(0deg);
  }
  
  .first-content span,
  .second-content span {
    color: rgba(255, 242, 115, 1);
    text-shadow: 0px 0px 10px 5px rgba(255, 211, 29, 0.8);
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 10px;
  }
  .first-content span,
  .second-content span {
    font-family: 'Poppins', sans-serif;
    font-size: 1rem;
    line-height: 1.4;
  }
  </style>
  