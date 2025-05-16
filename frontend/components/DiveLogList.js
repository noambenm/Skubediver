// frontend/src/components/DiveLogList.js
import React, { useState, useEffect } from 'react';
const API_BASE = process.env.REACT_APP_DIVE_API_URL;

function DiveLogList() {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    fetch(`${API_BASE}/logs`)
      .then(res => res.json())
      .then(data => setLogs(data));
  }, []);

  return (
    <div>
      <h2>Past Dives</h2>
      <ul>
        {logs.map(log => (
          <li key={log.id}>
            {log.location} – {log.depth}m for {log.duration}min 
            {log.notes ? ` (${log.notes})` : ''}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default DiveLogList;
