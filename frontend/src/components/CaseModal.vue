<template>
    <div class="modal-overlay">
      <div class="modal">
        <header>
          <h3>Add New Case</h3>
          <button class="close-btn" @click="$emit('close')">X</button>
        </header>
        <form @submit.prevent="submitCase">
          <div class="form-group">
            <label>Against:</label>
            <input type="text" v-model="form.against" required />
          </div>
          <div class="form-group">
            <label>Charges Filed (comma separated):</label>
            <input type="text" v-model="form.chargesInput" placeholder="e.g. Theft, Fraud" />
          </div>
          <div class="form-group">
            <label>Quick Description:</label>
            <input type="text" v-model="form.quickDescription" required />
          </div>
          <div class="form-group">
            <label>Long Description:</label>
            <textarea v-model="form.longDescription" required></textarea>
          </div>
          <div class="form-group">
            <label>Lawyers Associated (comma separated):</label>
            <input type="text" v-model="form.lawyersInput" placeholder="e.g. John Doe, Jane Smith" />
          </div>
          <div class="todo-section">
            <h4>Schedule Case Events</h4>
            <div
              v-for="(event, index) in todos"
              :key="index"
              class="todo-item"
            >
              <label>{{ event.label }} Date & Time:</label>
              <input type="datetime-local" v-model="event.datetime" required />
            </div>
            <div class="todo-buttons">
              <button type="button" @click="addNextHearing" v-if="!verdictAdded">Add Next Hearing</button>
              <button type="button" @click="addVerdict" v-if="!verdictAdded">Add Verdict</button>
            </div>
          </div>
          <div class="form-actions">
            <button type="submit">Submit Case</button>
            <button type="button" @click="$emit('close')">Cancel</button>
          </div>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  export default {
    name: 'CaseModal',
    data() {
      return {
        form: {
          against: '',
          chargesInput: '',
          quickDescription: '',
          longDescription: '',
          lawyersInput: ''
        },
        // The to-do list holds scheduled events.
        todos: [
          { label: 'First Hearing', type: 'first_hearing', datetime: '' }
        ],
        verdictAdded: false
      }
    },
    methods: {
      addNextHearing() {
        // Add a new "Next Hearing" event.
        this.todos.push({ label: 'Next Hearing', type: 'next_hearing', datetime: '' })
      },
      addVerdict() {
        if (this.verdictAdded) return
        this.todos.push({ label: 'Verdict', type: 'verdict', datetime: '' })
        this.verdictAdded = true
      },
      async submitCase() {
        // Compute the case title: "User.name vs [Against]"
        // Replace `User` with actual user info from your state/context if needed.
        const userName = "User"
        const title = `${userName} vs ${this.form.against}`
        
        const chargesArray = this.form.chargesInput
          ? this.form.chargesInput.split(',').map(s => s.trim()).filter(Boolean)
          : []
        const lawyersArray = this.form.lawyersInput
          ? this.form.lawyersInput.split(',').map(s => s.trim()).filter(Boolean)
          : []
        
        const events = this.todos.map(ev => ({
          type: ev.type,
          scheduled_datetime: ev.datetime
        }))
        
        const payload = {
          title: title,
          short_description: this.form.quickDescription,
          full_description: this.form.longDescription,
          charges: chargesArray,
          lawyers: lawyersArray,
          events: events
        }
        
        try {
          const response = await axios.post('http://localhost:8000/api/add-case/', payload, { withCredentials: true })
          if (response.data.status === 'ok') {
            alert('Case added successfully!')
            this.$emit('case-added')
            this.$emit('close')
          } else {
            alert('Error adding case: ' + response.data.message)
          }
        } catch (error) {
          console.error('Error submitting case:', error)
          alert('An error occurred while adding the case.')
        }
      }
    }
  }
  </script>
  
  <style scoped>
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0,0,0,0.5);
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .modal {
    background-color: white;
    padding: 20px;
    border-radius: 8px;
    width: 500px;
    max-width: 90%;
  }
  header {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .close-btn {
    background: none;
    border: none;
    font-size: 18px;
    cursor: pointer;
  }
  .form-group {
    margin-bottom: 15px;
  }
  .form-group label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
  }
  .form-group input,
  .form-group textarea {
    width: 100%;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  .todo-section {
    margin-top: 20px;
  }
  .todo-item {
    margin-bottom: 10px;
  }
  .todo-buttons {
    display: flex;
    gap: 10px;
    margin-bottom: 10px;
  }
  .form-actions {
    display: flex;
    justify-content: flex-end;
    gap: 10px;
    margin-top: 20px;
  }
  .form-actions button {
    padding: 8px 16px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  </style>