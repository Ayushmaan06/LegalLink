<template>
    <div class="card">
      <div class="card__border"></div>
      <div class="card_title__container">
        <span class="card_title">Blockchain Diagnostics</span>
      </div>
      <hr class="line" />
      <ul class="card__list">
        <li class="card__list_item">
          <span class="check">
            <svg class="check_svg" viewBox="0 0 16 16">
              <path
                d="M12.416 3.376a.75.75 0 0 1 .208 1.04l-5 7.5a.75.75 0 0 1-1.154.114l-3-3a.75.75 0 0 1 1.06-1.06l2.353 2.353 4.493-6.74a.75.75 0 0 1 1.04-.207Z"
              />
            </svg>
          </span>
          <span class="list_text">Latest Transaction Hash:</span>
        </li>
        <li class="card__list_item">
          <span class="check">
            <svg class="check_svg" viewBox="0 0 16 16">
              <path
                d="M12.416 3.376a.75.75 0 0 1 .208 1.04l-5 7.5a.75.75 0 0 1-1.154.114l-3-3a.75.75 0 0 1 1.06-1.06l2.353 2.353 4.493-6.74a.75.75 0 0 1 1.04-.207Z"
              />
            </svg>
          </span>
          <span class="list_text">Network Status: Connected</span>
        </li>
      </ul>
    </div>
  </template>
  
  <style scoped>
  .card {
    --white: hsl(0, 0%, 100%);
    --black: hsl(240, 15%, 9%);
    --paragraph: hsl(0, 0%, 83%);
    --line: hsl(240, 9%, 17%);
    --primary: rgba(255, 240, 89, 1);
  
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 0.4rem;
  
    width: 16rem;
    height: 7 rem;
    padding: 0.6rem;
    border-radius: 0.75rem;
  
    background-color: hsla(240, 15%, 9%, 1);
    background-image: radial-gradient(
        at 88% 40%, hsla(240, 15%, 9%, 1) 0px, transparent 85%
      ),
      radial-gradient(at 49% 30%, hsla(240, 15%, 9%, 1) 0px, transparent 85%),
      radial-gradient(at 14% 26%, hsla(240, 15%, 9%, 1) 0px, transparent 85%),
      radial-gradient(at 0% 64%, rgba(251, 240, 124, 1) 0px, transparent 85%),
      radial-gradient(at 41% 94%, rgba(251, 240, 124, 1) 0px, transparent 85%),
      radial-gradient(at 100% 99%, rgba(255, 240, 89, 1) 0px, transparent 85%);
    box-shadow: 0px -12px 16px 0px rgba(255, 255, 255, 0.2) inset;
  }
  
  .card__border {
    position: absolute;
    z-index: -10;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: calc(100% + 2px);
    height: calc(100% + 2px);
    border-radius: 0.75rem;
    background-image: linear-gradient(0deg, hsl(0, 0%, 100%) -50%, hsl(0, 0%, 40%) 100%);
    overflow: hidden;
    pointer-events: none;
  }
  
  .card__border::before {
    content: "";
    position: fixed;
    z-index: 200;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) rotate(0deg);
    transform-origin: left;
    width: 200%;
    height: 8rem;
    background-image: linear-gradient(
      0deg,
      hsla(0, 0%, 100%, 0) 0%,
      rgba(251, 240, 124, 1) 40%,
      rgba(255, 232, 0, 1) 60%,
      hsla(0, 0%, 40%, 0) 100%
    );
    animation: rotate 8s linear infinite;
  }
  
  @keyframes rotate {
    to {
      transform: rotate(360deg);
    }
  }
  
  .card_title__container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 2rem;
  }
  
  .card_title {
    font-size: 0.95rem;
    font-weight: bold;
    color: var(--white);
    text-align: center;
  }
  
  .line {
    height: 1px;
    background-color: var(--line);
    border: none;
    margin: 0.2rem 0;
  }
  
  .card__list {
    display: flex;
    flex-direction: column;
    gap: 0.3rem;
    padding-left: 0.25rem;
  }
  
  .card__list_item {
    display: flex;
    align-items: center;
    gap: 0.4rem;
    font-size: 0.65rem;
    color: var(--white);
  }
  
  .check {
    width: 0.9rem;
    height: 0.9rem;
    background-color: var(--primary);
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .check_svg {
    width: 0.6rem;
    height: 0.6rem;
    fill: var(--black);
  }
  </style>
  