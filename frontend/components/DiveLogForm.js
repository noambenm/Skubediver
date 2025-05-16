// frontend/src/components/DiveLogForm.js
import React, { useState } from 'react';

const API_BASE = process.env.REACT_APP_DIVE_API_URL;  // e.g., "http://localhost:5001"

function DiveLogForm() {
  const [location, setLocation] = useState('');
  const [depth, setDepth] = useState('');
  const [duration, setDuration] = useState('');
  const [notes, setNotes] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const logEntry = { location, depth: parseFloat(depth), duration: parseInt(duration), notes };
    await fetch(`${API_BASE}/logs`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(logEntry)
    });
    // Reset form or update UI accordingly...
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Log a Dive</h2>
      <div>
        <label>Location:</label>
        <input value={location} onChange={e => setLocation(e.target.value)} required />
      </div>
      <div>
        <label>Depth (m):</label>
        <input type="number" value={depth} onChange={e => setDepth(e.target.value)} required />
      </div>
      <div>
        <label>Duration (min):</label>
        <input type="number" value={duration} onChange={e => setDuration(e.target.value)} required />
      </div>
      <div>
        <label>Notes:</label>
        <input value={notes} onChange={e => setNotes(e.target.value)} />
      </div>
      <button type="submit">Submit Dive</button>
    </form>
  );
}

export default DiveLogForm;
