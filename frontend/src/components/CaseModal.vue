<template>
  <div class="add-case-page">
    <div class="modal-overlay">
      <div class="modal">
        <header>
          <h3>Add New Case</h3>
          <button class="close-btn" @click="closeModal">X</button>
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
            <button type="button" @click="closeModal">Cancel</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'AddCasePage',
  data() {
    return {
      isEdit: false,
      form: {
        against: '',
        chargesInput: '',
        quickDescription: '',
        longDescription: '',
        lawyersInput: ''
      },
      todos: [
        { label: 'First Hearing', type: 'first_hearing', datetime: '' }
      ],
      verdictAdded: false
    }
  },
  created() {
    const caseId = this.$route.params.caseId;
    if (caseId) {
      this.isEdit = true;
      this.fetchCaseDetails(caseId);
    }
  },
  methods: {
    addNextHearing() {
      this.todos.push({ label: 'Next Hearing', type: 'next_hearing', datetime: '' });
    },
    addVerdict() {
      if (!this.verdictAdded) {
        this.todos.push({ label: 'Verdict', type: 'verdict', datetime: '' });
        this.verdictAdded = true;
      }
    },
    async fetchCaseDetails(caseId) {
    try {
      const response = await axios.get(`http://localhost:8000/api/case/${caseId}/`, { withCredentials: true });
      console.log("Fetched case data:", response.data); // Log data for debugging
      const data = response.data;
      // Ensure that the keys here match what your API returns.
      this.form.against = data.against;
      this.form.chargesInput = (data.charges || []).join(", ");
      this.form.quickDescription = data.short_description;
      this.form.longDescription = data.full_description;
      this.form.lawyersInput = (data.lawyers || []).join(", ");
      this.todos = (data.events || []).map((event) => ({
        label: event.type === 'first_hearing' ? 'First Hearing' :
              event.type === 'next_hearing' ? 'Next Hearing' : 'Verdict',
        type: event.type,
        datetime: event.scheduled_datetime,
      }));
      // Mark verdict as added if applicable
      if (this.todos.some(ev => ev.type === 'verdict')) {
        this.verdictAdded = true;
      }
    } catch (error) {
      console.error('Error fetching case details:', error);
    }
  },
    async submitCase() {
      const userName = "User";
      const title = `${userName} vs ${this.form.against}`;
  
      const chargesArray = this.form.chargesInput.split(',').map(s => s.trim()).filter(Boolean);
      const lawyersArray = this.form.lawyersInput.split(',').map(s => s.trim()).filter(Boolean);
      const events = this.todos.map(ev => ({
        type: ev.type,
        scheduled_datetime: ev.datetime
      }));
  
      const payload = {
        title,
        short_description: this.form.quickDescription,
        full_description: this.form.longDescription,
        charges: chargesArray,
        lawyers: lawyersArray,
        events
      };
  
      try {
        if (this.isEdit) {
          // Update existing case
          const response = await axios.put(`http://localhost:8000/api/case/${this.$route.params.caseId}/`, payload, { withCredentials: true });
          if (response.data.status === 'ok') {
            alert('Case updated successfully!');
            this.resetForm();
            this.$router.push('/home');
          } else {
            alert('Error: ' + response.data.message);
          }
        } else {
          // Create new case
          const response = await axios.post('http://localhost:8000/api/add-case/', payload, { withCredentials: true });
          if (response.data.status === 'ok') {
            alert('Case added successfully!');
            this.resetForm();
            this.$router.push('/home');
          } else {
            alert('Error: ' + response.data.message);
          }
        }
      } catch (error) {
        console.error(error);
        alert('An error occurred while processing the case.');
      }
    },
    resetForm() {
      this.form = {
        against: '',
        chargesInput: '',
        quickDescription: '',
        longDescription: '',
        lawyersInput: ''
      };
      this.todos = [{ label: 'First Hearing', type: 'first_hearing', datetime: '' }];
      this.verdictAdded = false;
    },
    closeModal() {
      this.resetForm();
      this.$router.push('/home');
    }
  }
}
</script>
<style scoped>
.add-case-page {
  height: 100vh;
  overflow: hidden;
}

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
  overflow: hidden;
}

.modal {
  background-color: #fff;
  padding: 20px;
  border-radius: 10px;
  width: 90%;
  max-width: 500px;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
}

header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}

header h3 {
  margin: 0;
  font-size: 20px;
  font-weight: 600;
  color: #333;
  text-align: left;
}

.close-btn {
  background: none;
  border: none;
  font-size: 20px;
  font-weight: bold;
  cursor: pointer;
  color: #999;
}

.form-group {
  margin-bottom: 14px;
  text-align: left;
}

.form-group label {
  display: block;
  margin-bottom: 4px;
  font-weight: 500;
  font-size: 14px;
  color: #444;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 8px 10px;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-size: 14px;
}

textarea {
  min-height: 70px;
  resize: vertical;
}

.todo-section {
  margin-top: 18px;
  text-align: left;
}

.todo-section h4 {
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 10px;
  color: #333;
}

.todo-item {
  margin-bottom: 10px;
  text-align: left;
}

.todo-item label {
  display: block;
  margin-bottom: 4px;
  font-weight: 500;
  font-size: 14px;
  color: #555;
}

.todo-item input[type="datetime-local"] {
  width: 250px;
  max-width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-size: 14px;
}

.todo-buttons {
  display: flex;
  gap: 10px;
  margin-top: 8px;
  margin-bottom: 10px;
}

.todo-buttons button {
  background-color: #f0f0f0;
  color: #333;
  padding: 7px 12px;
  border: none;
  border-radius: 6px;
  font-size: 13px;
  cursor: pointer;
}

.form-actions {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
}

.form-actions button {
  padding: 9px 16px;
  font-size: 14px;
  font-weight: 500;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}

.form-actions button[type="submit"] {
  background-color: #ffcc00;
  color: #222;
}

.form-actions button[type="button"] {
  background-color: #eee;
  color: #333;
}
</style>
