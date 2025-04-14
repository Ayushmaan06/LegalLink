
<template>
    <div class="container">
      <div class="left-side">
        <div class="card">
          <div class="card-line"></div>
          <div class="buttons"></div>
        </div>
        <div class="post">
          <div class="post-line"></div>
          <div class="screen">
            <div class="dollar">Safe</div>
          </div>
          <div class="numbers"></div>
          <div class="numbers-line2"></div>
        </div>
      </div>
      <div class="right-side">
        <div class="new">LegalSafe</div>
      </div>
    </div>
  </template>
  
  <style scoped>
  .container {
    background-color: rgba(56, 56, 56, 1);
    display: flex;
    width: 460px;
    height: 120px;
    position: relative;
    border-radius: 6px;
    transition: 0.3s ease-in-out;
  }
  
  .container:hover {
    transform: scale(1.03);
    width: 220px;
  }
  
  .container:hover .left-side {
    width: 100%;
  }
  
  .left-side {
    background-color: rgba(0, 0, 0, 1);
    width: 130px;
    height: 120px;
    border-radius: 4px;
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    transition: 0.3s;
    flex-shrink: 0;
    overflow: hidden;
  }
  
  .right-side {
    width: calc(100% - 130px);
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    cursor: pointer;
    white-space: nowrap;
    transition: 0.3s;
  }
  
  .right-side:hover {
    background-color: rgba(56, 56, 56, 1);
  }
  
  .new {
    font-size: 38px;
    font-weight: bold;
    font-family: "Lexend Deca", sans-serif;
    color: #FFF059;
  }
  
  .card {
    width: 70px;
    height: 46px;
    background-color: rgba(58, 58, 58, 1);
    border-radius: 6px;
    position: absolute;
    display: flex;
    z-index: 10;
    flex-direction: column;
    align-items: center;
    -webkit-box-shadow: 9px 9px 9px -2px rgba(77, 200, 143, 0.72);
    -moz-box-shadow: 9px 9px 9px -2px rgba(255, 241, 107, 1);
    -webkit-box-shadow: 9px 9px 9px -2px rgba(255, 241, 107, 1);
  }
  
  .card-line {
    width: 65px;
    height: 13px;
    background-color: rgba(255, 232, 4, 1);
    border-radius: 2px;
    margin-top: 7px;
  }
  
  @media only screen and (max-width: 480px) {
    .container {
      transform: scale(0.7);
    }
  
    .container:hover {
      transform: scale(0.74);
    }
  
    .new {
      font-size: 30px;
    }
  }
  
  .buttons {
    width: 8px;
    height: 8px;
    background-color: rgba(0, 0, 0, 1);
    box-shadow: 0 -10px 0 0 rgba(0, 0, 0, 1), 0 10px 0 0 rgba(0, 0, 0, 1);
    border-radius: 50%;
    margin-top: 5px;
    transform: rotate(90deg);
    margin: 10px 0 0 -30px;
  }
  
  .container:hover .card {
    animation: slide-top 0.8s cubic-bezier(0.645, 0.045, 0.355, 1) both;
  }
  
  .container:hover .post {
    animation: slide-post 0.8s cubic-bezier(0.165, 0.84, 0.44, 1) both;
  }
  
  @keyframes slide-top {
    0% {
      transform: translateY(0);
    }
  
    50% {
      transform: translateY(-70px) rotate(90deg);
    }
  
    60% {
      transform: translateY(-70px) rotate(90deg);
    }
  
    100% {
      transform: translateY(-8px) rotate(90deg);
    }
  }
  
  .post {
    width: 63px;
    height: 75px;
    background-color: rgba(50, 50, 50, 1);
    position: absolute;
    z-index: 11;
    bottom: 10px;
    top: 120px;
    border-radius: 6px;
    overflow: hidden;
  }
  
  .post-line {
    width: 47px;
    height: 9px;
    background-color: #545354;
    position: absolute;
    border-radius: 0px 0px 3px 3px;
    right: 8px;
    top: 8px;
  }
  
  .post-line:before {
    content: "";
    position: absolute;
    width: 47px;
    height: 9px;
    background-color: #757375;
    top: -8px;
  }
  
  .screen {
    width: 47px;
    height: 23px;
    background-color: rgba(0, 0, 0, 1);
    position: absolute;
    top: 22px;
    right: 8px;
    border-radius: 3px;
  }
  
  .numbers {
    width: 12px;
    height: 12px;
    background-color: #838183;
    box-shadow: 0 -18px 0 0 #838183, 0 18px 0 0 #838183;
    border-radius: 2px;
    position: absolute;
    transform: rotate(90deg);
    left: 25px;
    top: 52px;
  }
  
  .numbers-line2 {
    width: 12px;
    height: 12px;
    background-color: #aaa9ab;
    box-shadow: 0 -18px 0 0 #aaa9ab, 0 18px 0 0 #aaa9ab;
    border-radius: 2px;
    position: absolute;
    transform: rotate(90deg);
    left: 25px;
    top: 68px;
  }
  
  @keyframes slide-post {
    50% {
      transform: translateY(0);
    }
  
    100% {
      transform: translateY(-70px);
    }
  }
  
  .dollar {
    position: absolute;
    font-size: 16px;
    font-family: "Lexend Deca", sans-serif;
    width: 100%;
    left: 0;
    top: 0;
    color: rgba(255, 240, 89, 1);
    text-align: center;
  }
  
  .container:hover .dollar {
    animation: fade-in-fwd 0.3s 0.8s backwards;
  }
  
  @keyframes fade-in-fwd {
    0% {
      opacity: 0;
      transform: translateY(-5px);
    }
  
    100% {
      opacity: 1;
      transform: translateY(0);
    }
  }
  </style>
  